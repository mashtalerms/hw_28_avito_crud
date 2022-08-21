import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from ads.models.location import Location
from my_project import settings
from users.models import User


@method_decorator(csrf_exempt, name="dispatch")
class UserView(ListView):
    """User List view"""

    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        users = self.object_list.annotate(
            ads_published=Count('ad', filter=Q(ad__is_published__gte=True))).select_related('location')

        paginator = Paginator(users, settings.TOTAL_ON_PAGE)
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        items = []
        for user in page_obj:
            items.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "role": user.role,
                "age": user.age,
                "location_id": user.location_id,
                "location": user.location.name,
                "ads_published": user.ads_published,
            })

        response = {
            "items": items,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    """User create View"""
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            password=user_data['password'],
            role=user_data['role'],
            age=user_data['age'],
        )

        location, created = Location.objects.get_or_create(name=user_data['location'])
        user.location = location
        user.save()

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "location_id": user.location_id,
            "location": str(user.location),
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name="dispatch")
class UserDetailView(DetailView):
    """User detail View"""

    model = User

    def get(self, request, *args, **kwargs):

        user = self.get_object()

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "location_id": user.location_id,
            "location": str(user.location),
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    """User update View"""
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)

        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.username = user_data["username"]
        self.object.password = user_data["password"]
        self.object.age = user_data["age"]

        location, created = Location.objects.get_or_create(name=user_data["location"])
        self.object.location = location

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "role": self.object.role,
            "age": self.object.age,
            "location_id": self.object.location_id,
            "location": str(self.object.location),
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    """User delete View"""

    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

#TODO следующие шаги
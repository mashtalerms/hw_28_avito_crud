import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from ads.models.ad import Ad
from my_project import settings


@method_decorator(csrf_exempt, name="dispatch")
class AdView(ListView):
    """Ads List view"""

    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        ads = self.object_list.select_related("author").select_related("category").order_by('-price')

        paginator = Paginator(ads, settings.TOTAL_ON_PAGE)
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        items = []
        for ad in page_obj:
            items.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": str(ad.author),
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "category": str(ad.category),
                "image": ad.image.url if ad.image else None,
            })

        response = {
            "items": items,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdDetailView(DetailView):
    """Ad detail View"""

    model = Ad

    def get(self, request, *args, **kwargs):

        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": str(ad.author),
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": str(ad.category),
            "image": ad.image.url if ad.image else None,
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    """Ad create View"""
    model = Ad
    fields = ["name", "author", "price", "description"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data['name'],
            author=ad_data['author'],
            price=ad_data['price'],
            description=ad_data['description'],
        )
        ad.is_published = True

        ad.save()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": str(ad.author),
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    """Ads update View"""

    model = Ad
    fields = ["name", "author", "price", "description", ""]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data["name"]
        self.object.author = ad_data["author"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": str(self.object.author),
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
        }, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    """Ads delete View"""

    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateImageView(UpdateView):
    """Ads update image View"""

    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category,
            "image": self.object.image.url if self.object.image else None,
        }, json_dumps_params={'ensure_ascii': False})

from django.conf.urls.static import static
from django.urls import path
from ads.views.ad import AdDetailView, AdView, AdCreateView, AdUpdateView, AdDeleteView, AdUpdateImageView
from ads.views.category import CategoryDetailView, CategoryListView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView
from ads.views.index import index
from my_project import settings

urlpatterns = [
    path('', index, name="index"),

    path('ad/', AdView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUpdateImageView.as_view()),

    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('about_us', views.about_us, name='about_us'),
    path('manufacturer/<int:manufacturer_id>/', views.manufacturer_products, name='manufacturer_products')


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import home, category_services,service_detail,service_search

urlpatterns = [
    path('home/', home, name='home'),
    path('category/<slug:slug>/', category_services, name='category_services'),
    path('service/<int:service_id>/', service_detail, name='service_detail'),
    path('search/', service_search, name='service_search'),
]


from django.urls import path
from .views import workers_list, workers_detail, orders_list, orders_detail, jobtitles_list, jobtitles_detail
urlpatterns = [
    path('workers/', workers_list),
    path('workers/<int:pk>/', workers_detail),
    path('orders/', orders_list),
    path('orders/<int:pk>/', orders_detail),
    path('jobtitles/', jobtitles_list),
    path('jobtitles/<int:pk>/', jobtitles_detail),



]

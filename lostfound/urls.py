from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/<str:status>/', views.report_item, name='report_item'),
    path('found-items/', views.found_items_list, name='found_items_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/matches/', views.find_matches, name='find_matches'),
    path('item/<int:pk>/claim/', views.submit_claim, name='submit_claim'),
]
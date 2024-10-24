from django.urls import path
from . import views

urlpatterns = [
    path('application/create/<int:property_id>/', views.rental_application_create, name='rental_application_create'),
    path('applications/', views.rental_application_list, name='rental_application_list'),
    path('application/<int:pk>/update/', views.rental_application_update, name='rental_application_update'),
    path('agreement/create/<int:application_id>/', views.rental_agreement_create, name='rental_agreement_create'),
    path('agreement/<int:pk>/', views.rental_agreement_detail, name='rental_agreement_detail'),
    path('payment/create/<int:agreement_id>/', views.payment_create, name='payment_create'),
    path('payment/history/<int:agreement_id>/', views.payment_history, name='payment_history'),
]
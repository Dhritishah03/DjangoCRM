from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete_record'),
    path('addrecord/', views.add_record, name='add_record'),
    path('updaterecord/<int:pk>', views.update_record, name='update_record'),
    # Example view for the customer app
    # Add other URL patterns here
]

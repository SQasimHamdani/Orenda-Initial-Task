from django.urls import path

from . import views


urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='home'),
    # path('create', views.EmployeeCreateView.as_view(), name='create'),
    path('create_employee', views.create_employee, name='create'),
    path('<id>/delete', views.delete_employee),
    path('<id>/edit', views.edit_employee),
    # path('create', views.home_view , name='create'),
    # path('create', views.EmployeeCreateView.as_view(), name='create'),
]
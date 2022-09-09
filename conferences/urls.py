from django.urls import path
from conferences import views

urlpatterns = [
    path('', views.conferences_home, name='conferences_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ConfDetailView.as_view(), name='conf_detail'),
    path('<int:pk>/edit', views.ConfEditView.as_view(), name='conf_edit'),
    path('<int:pk>/delete', views.ConfDeleteView.as_view(), name='conf_delete')
]
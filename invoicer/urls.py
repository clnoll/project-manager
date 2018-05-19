from django.urls import path

from . import views


urlpatterns = [
    # ex: /invoicer/
    path('', views.index, name='index'),
    # ex: /invoicer/client/5/
    path('<int:client_id>/', views.get_client, name='client'),
    # ex: /invoicer/project/5/
    path('<int:project_id>/', views.get_project, name='project'),
    # ex: /invoicer/task/5/
    path('<int:task_id>/', views.get_task, name='task'),
    # ex: /invoicer/invoice/5/
    path('<int:invoice_id>/', views.get_invoice, name='invoice'),
    # ex: /invoicer/work/5/
    path('<int:work_id>/', views.get_work, name='work'),
]

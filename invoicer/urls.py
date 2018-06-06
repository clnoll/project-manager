from django.urls import path

from . import views


app_name = 'invoicer'


urlpatterns = [
    # ex: /invoicer/
    path('', views.index, name='index'),

    # ex: /invoicer/client/5/
    path('client/<int:client_id>/', views.get_client, name='get_client'),

    # ex: /invoicer/client/create/
    path('client/create/', views.create_client, name='create_client'),

    # ex: /invoicer/client_group/5/
    path('client_group/<int:client_group_id>/', views.get_client_group, name='get_client_group'),

    # ex: /invoicer/client_group/5/
    path('client_group/create/', views.create_client_group, name='create_client_group'),

    # ex: /invoicer/project/5/
    path('project/<int:project_id>/', views.get_project, name='get_project'),

    # ex: /invoicer/project/create/
    path('project/create/', views.create_project, name='create_project'),

    # ex: /invoicer/task/5/
    path('task/<int:task_id>/', views.get_task, name='get_task'),

    # ex: /invoicer/task/create/
    path('task/create/', views.create_task, name='create_task'),

    # ex: /invoicer/invoice/5/
    path('invoice/<int:invoice_id>/', views.get_invoice, name='get_invoice'),

    # ex: /invoicer/invoice/create/
    path('invoice/create/', views.create_invoice, name='create_invoice'),

    # ex: /invoicer/work/5/
    path('work/<int:work_id>/', views.get_work, name='get_work'),

    # ex: /invoicer/work/create/
    path('work/create/', views.create_work, name='create_work'),
]

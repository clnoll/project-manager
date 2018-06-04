from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Client, ClientGroup, Project


def index(request):
    latest_project_list = Project.objects.all()[:5]
    context = {
        'latest_project_list': latest_project_list,
    }
    return render(request, 'invoicer/index.html', context)


def client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    return render(request, 'invoicer/client.html', {'client': client})


def client_group(request, client_group_id):
    try:
        client_group = ClientGroup.objects.get(pk=client_group_id)

    except ClientGroup.DoesNotExist:
        raise Http404("Client Group does not exist")
    return render(request, 'invoicer/client_group.html', {'client_group': client_group, 'clients': client_group.clients.all()})    


def project(request, project_id):
    return HttpResponse("project_id: %s." % project_id)


def task(request, task_id):
    return HttpResponse("task_id: %s." % task_id)


def invoice(request, invoice_id):
    return HttpResponse("invoice_id: %s." % invoice_id)


def work(request, work_id):
    return HttpResponse("work_id: %s." % work_id)

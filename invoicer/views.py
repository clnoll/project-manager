from django.http import HttpResponse

from .models import Project


def index(request):
    import ipdb ; ipdb.set_trace()
    latest_project_list = Project.objects.all()[:5]
    output = ', '.join([p for p in latest_project_list])
    return HttpResponse(output)


def get_client(request, client_id):
    return HttpResponse("client_id: %s." % client_id)


def get_project(request, project_id):
    return HttpResponse("project_id: %s." % project_id)


def get_task(request, task_id):
    return HttpResponse("task_id: %s." % task_id)


def get_invoice(request, invoice_id):
    return HttpResponse("invoice_id: %s." % invoice_id)


def get_work(request, work_id):
    return HttpResponse("work_id: %s." % work_id)

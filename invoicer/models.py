from django.db import models


class BaseClient(models.Model):

    def __str__(self):
        return self.__dict__


class BaseProject(models.Model):
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.__dict__


class BaseTask(models.Model):
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.__dict__


class BaseWork(models.Model):
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.__dict__


class BaseInvoice(models.Model):

    def __str__(self):
        return self.__dict__

    
class Client(BaseClient):
    email = models.CharField(max_length=200)
    is_primary = models.BooleanField()
    name = models.CharField(max_length=200)
    primary_phone = models.CharField(max_length=50)
    secondary_phone = models.CharField(max_length=50)


class ClientGroup(BaseClient):
    clients = models.ManyToManyField(Client)

    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)

    
class ProjectStatus(BaseProject):
    pass


class ProjectType(BaseProject):
    pass

    
class Project(BaseProject):
    client_group = models.ForeignKey(ClientGroup, on_delete=models.CASCADE)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    start = models.DateTimeField()
    

class TaskStatus(BaseTask):
    pass


class TaskType(BaseTask):
    default_cost = models.FloatField()


class Task(BaseTask):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    start = models.DateTimeField()


class Invoice(BaseInvoice):
    amount_paid = models.FloatField()
    date_sent = models.DateTimeField()
    date_paid = models.DateTimeField()
    status = models.BooleanField()
    total = models.FloatField()

    
class Work(BaseWork):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    minutes_billed = models.IntegerField()
    rate = models.FloatField()

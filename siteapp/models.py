from django.db import models

class complaints(models.Model):
    name=models.CharField(max_length=50)
    service=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    regdate=models.DateTimeField()
    donedate=models.DateTimeField()
    status=models.CharField(max_length=20)


    def __str__(self):

        return self.name

class completed(models.Model):
    name=models.CharField(max_length=50)
    service=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    regdate=models.DateTimeField()
    donedate=models.DateTimeField()
    status=models.CharField(max_length=20)


    def __str__(self):

        return self.name


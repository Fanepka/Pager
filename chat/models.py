from django.db import models

# Create your models here.


class User(models.Model):
    
    id = models.AutoField()


class Chat(models.Model):

    id = models.AutoField(verbose_name="Идентификатор")
    
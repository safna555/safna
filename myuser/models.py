from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/',null=True)

class Register(models.Model):
    name =  models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=8)
    image = models.ImageField(upload_to='profile/', null=True)

    class Meta:
       db_table ="register"
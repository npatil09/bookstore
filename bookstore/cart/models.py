from django.db import models
from django.contrib.auth.models import User
from store.models import Books

# Create your models here.
class Cart(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    book_type = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='store',default='')
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)
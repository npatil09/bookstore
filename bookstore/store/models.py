from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    book_type = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    book_desc = models.CharField(max_length=2000 ,default='')
    book_image = models.ImageField(upload_to='images',default='')

class Review(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=50,null=True,blank=True,default='')
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_name} on {self.book_id.book_name}"
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

class Blog(models.Model):
    name = models.CharField(max_length=100)
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text="write your blog")
    post_date =models.DateField(default=date.today)
    slug = models.CharField(max_length=1000, null= True, blank=True)
    
    def __str__(self):
        return self.name + " ==> " + str(self.auther)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.post_date))
        return super().save(*args, **kwargs)
    
    
class BlogComment(models.Model):
    description = models.TextField(help_text="write your comment")
    auther = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.blog) + " ==> " + "(" + str(self.auther) + ")"
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.IntegerField()
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)
    
    


    

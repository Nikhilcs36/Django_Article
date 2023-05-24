from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Blog(models.Model):
    name = models.CharField(max_length=100)
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text="write your blog")
    post_date =models.DateField(default=date.today)
    
    def __str__(self):
        return self.name + " ==> " + str(self.auther)
    
class BlogComment(models.Model):
    description = models.TextField(help_text="write your comment")
    auther = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.blog) + " ==> " + "(" + str(self.auther) + ")"
    


    

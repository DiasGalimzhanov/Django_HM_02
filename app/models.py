from django.db import models

class Post(models.Model):                               # Table name
    title = models.CharField(max_length=255)            # Column
    body = models.TextField()                           # Column 
    price = models.IntegerField()                       # Column
    published = models.DateTimeField(auto_now_add=True) # Column
    
    def __str__(self):
        return self.title
    
# title
# published
# completed (Boolean)
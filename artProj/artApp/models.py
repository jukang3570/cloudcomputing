from django.db import models

# Create your models here.
class Post(models.Model):
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.pk} 게시물'
    
    @property
    def update_counter(self):
        self.like += 1
        self.save()
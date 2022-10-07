from django.db import models

class Tasks(models.Model):
    id = models.AutoField(primary_key=True,  auto_created = True,)
    title = models.CharField(max_length=240)
    number = models.IntegerField()
    text = models.TextField(max_length=240)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

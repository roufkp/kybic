from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#testimonials

# Create your models here.
# Create your models here.
class Testimonials(models.Model):    
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200,null=True,blank=True)
    paragraph = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

#testimononials end



#blog


class Blog(models.Model):
    heading =models.CharField(max_length=200)
    paragraph = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)


    def save(self,*args, **kwargs):
        if not self.id:
            self.cearted_at =timezone.now()
        return super().save(*args, **kwargs)
        

    def __str__(self):
        return self.heading
    
#blogend



class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    

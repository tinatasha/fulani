from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=300)
    image_caption = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True, max_length=700)
    time = models.DateTimeField(default=timezone.now)
    
    @classmethod
    def search_results(cls, search_term):
        images = cls.objects.filter(image_name__icontains=search_term)
        return images
    
    def __str__(self):
        return self.image_name
  
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)  
    
class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name="profile", on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="profile/", max_length=255, null=True, blank=True, default=""
    )
    general_location = models.TextField(null=True,max_length=600)
    neighborhood_name = models.TextField(null=True, max_length=600)
    phone = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    bio = models.TextField()
    projects = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Page(models.Model):
    # use models.URLField()
    name = models.CharField(max_length=255, blank=False, unique=False)
    audio = models.URLField()
    video = models.URLField()
    article = models.URLField()
    question = models.URLField()
    form = models.URLField()
    owner = models.ForeignKey('auth.User',
        related_name='pages', 
        on_delete=models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)   

class Week(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    owner = models.ForeignKey('auth.User',
        related_name='weeks', 
        on_delete=models.CASCADE) 
    pages = models.ManyToManyField(Page)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Program(models.Model):
  """This class represents the bucketlist model."""
  name = models.CharField(max_length=255, blank=False, unique=True)
  description = models.TextField()
  image = models.CharField(max_length=255, blank=False, unique=False)
  weeks = models.ManyToManyField(Week, blank=False)
  owner = models.ForeignKey('auth.User',
    related_name='programs', 
    on_delete=models.CASCADE) 
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    """Return a human readable representation of the model instance."""
    return "{}".format(self.name)
    
    # This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
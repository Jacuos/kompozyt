from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    #TO DO: Connect user with his projects/tasks! Should user store it or a project/task?

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

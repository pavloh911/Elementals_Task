from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SLink(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=350)
    count = models.IntegerField(editable=False, default=0, blank=True, null=True)

    def __str__(self):
        return str(self.User)

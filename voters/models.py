from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField()
    ip = models.CharField(verbose_name='ip głosującego',
        max_length=settings.MAX_USER_INFO_FIELDS_LENGTH,
        null=True,
        unique=False,
        blank=True
    )
    user_agent = models.CharField(verbose_name='przeglądarka głosującego',
        max_length=settings.MAX_USER_INFO_FIELDS_LENGTH,
        null=True,
        unique=False,
        blank=True
    )

    
    def __str__(self):
        return u'{0}'.format(self.user)


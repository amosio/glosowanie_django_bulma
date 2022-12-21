from django.db import models

class Option(models.Model):
    option_name = models.CharField(max_length=250, default=None)

    def __str__(self):
        return u'{0}'.format(self.option_name)



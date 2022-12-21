from django.db import models
from options.models import Option
from voters.models import Voter
# from django.utils import timezone

class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)


    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
        # if not self.id:
        #     self.created = timezone.now()
        # self.modified = timezone.now()
        # return super(Vote, self).save(*args, **kwargs)
        # 
    
    def __str__(self):
        return u'{0}'.format(self.option)

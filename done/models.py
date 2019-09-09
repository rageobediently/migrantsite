from django.db import models

class ThisDone(models.Model):
    nameser = models.CharField(max_length = 100)
    done = models.BooleanField()


    def __str__(self):
        return "№ {},{}, готовность = {}".format(self.id,self.nameser,self.done)

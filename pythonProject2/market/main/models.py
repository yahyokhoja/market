from django.db import models




class Task(models.Model):
    nom = models.CharField('ном' ,max_length= 50)
    harid = models.CharField('харид' ,max_length= 50)
    furush = models.CharField('фуруш' ,max_length= 50)


    def __str__(self):
        return self.nom


    class Meta:
            verbose_name = 'харид'
            verbose_name_plural = 'харидхо'





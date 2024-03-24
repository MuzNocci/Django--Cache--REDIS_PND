from django.db import models



class Users(models.Model):


    name = models.CharField(max_length=50)
    mail = models.EmailField()


    class Meta:

        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


    def __str__(self):

        return self.name
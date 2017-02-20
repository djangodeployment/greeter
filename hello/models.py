from django.db import models


class Greetee(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models


class Greetee(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class VisitorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    greetee = models.ForeignKey(Greetee, null=True, blank=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return '{} ({})'.format(self.timestamp.isoformat(),
                                self.greetee.name if self.greetee else 'world')

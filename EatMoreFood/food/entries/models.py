from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'

class NewFood(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    comments = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)

    class Meta:
            verbose_name_plural = 'newfoods'

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class NewFood(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=5)
    comments = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID#{}>'.format(self.id)

    class Meta:
            verbose_name_plural = 'newfoods'

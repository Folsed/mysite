from django.db import models
from django_countries.fields import CountryField


class Conference(models.Model):
    title = models.CharField('Title', max_length=255)
    date = models.DateTimeField('Date')
    lat = models.FloatField('Latitude', max_length=50)
    lng = models.FloatField('Longitude', max_length=50)
    country = CountryField(blank_label='Country')
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/conferences/{self.id}'
    
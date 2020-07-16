from django.db import models

# Create your models here.


class Value(models.Model):
    value_name = models.CharField(max_length=50)
    related_feature_name = models.CharField(max_length=100)
    # feature_name = models.CharField(max_length=100)
    def __str__(self):
        return self.value_name

class Feature(models.Model):
    feature_name = models.CharField(max_length=100)
    values = models.ManyToManyField(Value)
    def __str__(self):
        return self.feature_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.tag_name
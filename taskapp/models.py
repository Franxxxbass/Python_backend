from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=64)

exit


class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField()
    still_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Album(models.Model):
    title = models.CharField(max_length=128)
    release_date = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    band = models.ForeignKey(
        'Band',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title

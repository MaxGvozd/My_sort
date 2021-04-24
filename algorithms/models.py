from django.db import models


class Execution(models.Model):
    METHODS = [
        ('Bubble', 'Bubble'),
        ('Insertion', 'Insertion'),
        ('Merge', 'Merge'),
        ('Quick_sort', 'Quick sort'),
    ]
    name = models.CharField(max_length=255, blank=True)
    method = models.CharField(max_length=20, choices=METHODS)
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

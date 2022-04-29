from django.db import models

#  Models


class Employee(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    address = models.TextField(default='')
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

from django.db import models

from django_bulk_update.manager import BulkUpdateManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    title = models.CharField(max_length=50)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)


class User(models.Model):
    email = models.EmailField()


class Inscription(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE)


class ProgressVideo(models.Model):
    minutes_daily_play = models.IntegerField()
    course = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    dia = models.DateField()
    category = models.CharField(max_length=50)
    id_inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    objects = BulkUpdateManager()

    # def migration(self):
    #     self.course = self.id_inscription.id_course.title
    #     self.user = self.id_inscription.id_user.email
    #     self.category = self.id_category.name

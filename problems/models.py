from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    new = models.BooleanField()
    description = models.CharField(max_length=500)
    hair_type = models.CharField(max_length=100)

    def __repr__(self):
        return f"<{self.name} {self.new} {self.description} {self.hair_type}>"


class CTFUser(models.Model):
    email = models.CharField(max_length=100)
    solved = models.JSONField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    specialization = models.CharField(max_length=40, blank=False)
    experience = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room(models.Model):
    number = models.IntegerField(blank=False)
    department = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return str(self.number)

class Patient(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=False)
    diagnosis = models.CharField(max_length=40, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return f'/patient/{self.pk}/'
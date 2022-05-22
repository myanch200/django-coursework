from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(User, related_name='modules')

    def __str__(self):
        return self.name

class Exam(models.Model):
    module = models.ForeignKey(Module, related_name="exams", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    exam_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def user_registered_for_exam(self, the_user):
        return self.applications.filter(user=the_user).exists()

    def humanize_date(self):
        return self.exam_date.strftime("%d.%m.%Y %H:%M")

class ExamRegistration(models.Model):
    PAYMENT_CHOICES = (
      ('cash', 'В брой'),
      ('card', 'С карта'),
      ('bank transfer', 'Банков превод'),
    )

    exam = models.ForeignKey(Exam, related_name="applications", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="exam_applications", on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='cash')

    def __str__(self):
        return self.user.username + " - " + self.exam.name

    

    

    
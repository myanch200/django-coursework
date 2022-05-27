from django.utils.timezone import now
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
"""
Тук се намират моделите ни за курс, изпит и регистрация към изпит
Наследявайки от models.Model използваме методите на него за да ги определим какви данни ще имаме в моделите
CharField - поле за въвеждане на текст, което за разлика от TextField съдържа малко на брой символи
TextField служи за запаване на много дълги текстове
ManyToManyField - създава many to many връзки между моделите също чрез related_name определяме как ще изпиваме тези курсове през потребителя
в този случай ще бъде  user.module.all()
ForeignKey - поле за връзка към друг модел, с което определяме,че един курс може да има повече от един изпит
DateTimeField - поле за въвеждане на дата и час
функцията __str__ определя какво ще изписва при извикване на модела без да достъпваме някое от полетата му
ако не определим __str__ ще изпише ClassName object (id)

CharField - също приема параметър choices, което ни позволява да ограничим вариантите за отговор от потребителя


"""
class Module(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(User, related_name='modules', blank=True)

    def __str__(self):
        return self.name

class Exam(models.Model):
    module = models.ForeignKey(Module, related_name="exams", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    exam_date = models.DateTimeField()

    def __str__(self):
        return self.name
    # функция която проверя дали потребител се е регистрирал за изпита
    def user_registered_for_exam(self, the_user):
        return self.applications.filter(user=the_user).exists()
    # функция която форматирата датата
    def humanize_date(self):
        return self.exam_date.strftime("%d.%m.%Y %H:%M")
    # проверява дали моделът е валиден и е валиден ако датата на изпита е в бъдещето и има име и описание
    def is_valid(self):
        return datetime.strptime(self.exam_date, "%Y-%m-%d %HH:mm") > now() and self.name and self.description
class ExamRegistration(models.Model):
    PAYMENT_CHOICES = (
      ('cash', 'В брой'),
      ('card', 'С карта'),
      ('bank transfer', 'Банков превод'),
    )

    exam = models.ForeignKey(Exam, related_name="applications", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="exam_applications", on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='cash')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + " - " + self.exam.name
    # форматиране на метода за плащане
    def get_payment_method_display(self):
        return dict(self.PAYMENT_CHOICES).get(self.payment_method)

    

    

    
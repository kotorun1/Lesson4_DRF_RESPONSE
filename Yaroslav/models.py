from django.db import models
from django.utils import timezone

# Create your models here.


class JobTitles(models.Model):
    name = models.CharField(verbose_name="Название должности", max_length=100)

    def __str__(self):
        return self.name
    
    
class Workers(models.Model):
    firstname = models.CharField(verbose_name="Имя", max_length=100)
    lastname = models.CharField(verbose_name="Фамилия", max_length=100)
    surname = models.CharField(verbose_name="Отчество", max_length=100)
    login = models.CharField(verbose_name="Никнейм", max_length=100)
    password = models.CharField(verbose_name="Пароль", max_length=100)
    photo = models.ImageField(verbose_name="Фото",upload_to= 'media/')
    job_title = models.ForeignKey(JobTitles, on_delete=models.CASCADE, verbose_name="Должность")

    def __str__(self):
        return self.login + ':' + self.job_title.name


class Orders(models.Model):

    STATUS = (
        ('Added', 'Добавлен'),
        ('Paid', 'Оплачен'),
        ('Full', 'Выполненяеться'),
        ('Completed', 'Выполнен'),
        ('Ruin', 'Отменён'),
    )
    table_number = models.IntegerField(verbose_name="Номер стола")
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name="Работник")
    time_create = models.TimeField(auto_now_add=True, verbose_name="Время Создания")
    cost = models.IntegerField(verbose_name="Цена")
    status = models.CharField('Статус', max_length=20, choices=STATUS)

    def __str__(self):
        return str(self.table_number) + ' столик, создан ' + str(self.time_create) + ' для ' + self.worker.login + ':' + self.status

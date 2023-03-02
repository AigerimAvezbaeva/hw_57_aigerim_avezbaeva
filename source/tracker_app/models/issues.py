from django.db import models
from django.db.models import TextChoices


class Type(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Тип'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    def __str__(self):
        return self.name


class StatusChoice(TextChoices):
    NEW = 'New', 'новый'
    IN_PROCESS = 'In process', 'в процессе'
    DONE = 'Done', 'выполнено'


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=True,
        blank=False,
        verbose_name="Заголовок")
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Описание")
    status = models.CharField(
        verbose_name='Статус',
        choices=StatusChoice.choices,
        max_length=20,
        default=StatusChoice.NEW)
    types = models.ForeignKey(
        Type,
        related_name='type',
        blank=True,
        on_delete=models.PROTECT
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Время создания")
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата и время обновления")


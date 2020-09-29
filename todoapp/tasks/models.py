from django.db import models
from django.urls import reverse


class ToDoItem(models.Model):
    description = models.CharField(max_length=64)
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('tasks:details', args=[self.pk])

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ('-created',)

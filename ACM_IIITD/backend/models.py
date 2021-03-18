from django.db import models
from django.db.models.deletion import CASCADE


class position(models.IntegerChoices):
    first = 1
    second = 2
    third = 3
    runner_up_1 = 4
    runner_up_2 = 5


class event(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    link = models.URLField()
    description = models.TextField()
    def __str__(self) -> str:
        return self.name

class detail(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)


class prize(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    cash = models.PositiveIntegerField()
    position = models.IntegerField(choices=position.choices)
    other_details = models.CharField(max_length=200)


class image(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self) -> str:
        return self.image.name
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class media(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    file = models.FileField()
    def __str__(self) -> str:
        return self.file.name
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

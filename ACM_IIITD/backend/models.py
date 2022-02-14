from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

def upload_path(obj, file):
    return f'{obj.container.id}/{file}'

class Container(models.Model):
    heading = models.CharField(max_length=100, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.heading


class Paragraph(models.Model):
    content = models.TextField()
    container = models.ForeignKey(
        Container, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f""


class Image(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    content = models.ImageField(upload_to=upload_path)

    def __str__(self) -> str:
        return self.content.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class Media(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    content = models.FileField(upload_to=upload_path)

    def __str__(self) -> str:
        return self.content.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class TeamMember(models.Model):
    def upload_path(instance, filename):
        return f"team/{filename}"

    designation = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_path)
    batch = models.CharField(max_length=200, blank=True, default='')
    def __str__(self) -> str:
        return self.name

class Blog(Container):
    author = models.ForeignKey(TeamMember,null=True,blank=True, on_delete=models.SET_NULL)
    pass

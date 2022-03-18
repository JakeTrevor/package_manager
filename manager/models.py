from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank = True, null = True, default="")

    def __str__(self):
        return self.user.username

class Package(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tags = models.TextField(blank=True)

    package_name = models.CharField(max_length=120, unique=True)
    current_version = models.TextField(default="")

    downloads = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    public = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.package_name

class File(models.Model):
    readme = models.BooleanField(default=False)
    code_file = models.FileField()

class Version(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    version_ID = models.CharField(max_length=20, unique=True)
    

    
    code_files = models.ManyToManyField(File)

    comment = models.TextField(default="")
    dependencies = models.TextField(default="")
    
    def __str__(self) -> str:
        return self.package + ":" + self.version_ID


class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    text = models.TextField()

    posted_at = models.DateField()
    likes = models.IntegerField()
    def __str__(self) -> str:
        return self.text[:10]
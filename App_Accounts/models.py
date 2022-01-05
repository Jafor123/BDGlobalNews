from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from App_Author.models import EditorList
from App_News.models import *
CHOICES= (
('UK', 'United Kingdom'),
('US', 'United States'),
('BD', 'Bangladesh'),
('Others', 'Others'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_author=models.BooleanField(default=False)
    is_editor=models.BooleanField(default=False)
    about=models.TextField(blank=True)
    phone = models.CharField(max_length=11, blank=True)
    country = models.CharField(max_length=50,choices=CHOICES, blank=True)
    city = models.CharField(max_length=50, blank=True)
    photo=models.ImageField(upload_to="Profile/",default="profile.png")
    address = models.CharField(max_length=100, blank=True)
    fb_id=models.URLField(blank=True)
    tw_id=models.URLField(blank=True)
    linkd_id=models.URLField(blank=True)
    instra_id=models.URLField(blank=True)

    def __str__(self):
        return str(self.user)

    def get_comment_count_by_user(self):
        n=News.objects.filter(author=self.user)
        return n

    def get_total_publish_news(self):
        n = News.objects.filter(author=self.user,publish=True,publish_date__lte=date.today())
        return n

    def get_total_daft_news(self):
        n = News.objects.filter(author=self.user,draft=True)
        return n

    def get_total_schedule_news(self):
        n = News.objects.filter(author=self.user,publish_date__gte=date.today())
        return n

    def get_total_editor_no(self):
        n = EditorList.objects.filter(author=self.user)
        return n


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Subscriber(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="subscriber")
    status=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return str(self.user)
from datetime import date

from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q


class Sliderimage(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField(blank=True)
    photo = models.ImageField(upload_to="Slider/", blank=False)

    def __str__(self):
        return '{}'.format(self.title)


class Categoryapply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}-{}'.format(self.user, self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_nav = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_en_category_news(self):
        news_items = News.objects.filter(category=self, publish=True, publish_date__lte=date.today())
        return news_items

    def category_post_count(self):
        news_count = News.objects.filter(category=self, publish=True, publish_date__lte=date.today())
        return news_count

    def get_subcategory_by_category(self):
        subs = Subcategory.objects.filter(category=self)
        return subs


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategoryapply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '{}-{}'.format(self.category, self.name)


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = RichTextUploadingField(null=True)
    short_description = models.TextField(default="")
    thumbnail = models.ImageField(upload_to="thumbnail/", default='default.jpg')
    publish = models.BooleanField(default=True)
    draft = models.BooleanField(default=False)
    like = models.ManyToManyField(User, related_name="like", blank=True)
    spam = models.ManyToManyField(User, related_name="spam", blank=True)
    publish_date = models.DateField(auto_now=False, default=date.today, auto_now_add=False, null=True, blank=True)
    post_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.news_title, self.post_date.date())

    def like_count(self):
        return self.like.count()

    def count_comment(self):
        posts = Comment.objects.filter(post=self)
        return len(posts)

    def get_category_wise_comments(self):
        comments_list = Comment.objects.filter(post=self)
        return comments_list


class UserVerify(models.Model):
    email = models.EmailField(max_length=60)
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{}-{}'.format(str(self.email), self.status)


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name="replies")
    content = models.TextField(max_length=160)
    status = models.BooleanField(default=True)
    spam = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.news_title, str(self.post.author))

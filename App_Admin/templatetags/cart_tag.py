from django import template
from django.contrib.auth.models import User

from App_Accounts.models import Profile
from App_News.models import News

register = template.Library()


@register.filter('user_total')
def user_total(user):
    user_count = User.objects.all().exclude(username=user).count()
    return user_count


@register.filter('total_news')
def total_news(user):
    news_count = News.objects.filter(publish=True).count()
    return news_count


@register.filter('total_author')
def total_author(user):
    author_count = Profile.objects.filter(is_author=True).exclude(user=user).count()
    return author_count


@register.filter('total_draft')
def total_draft(user):
    draft_count = News.objects.filter(draft=True).count()
    return draft_count

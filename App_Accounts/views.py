import json
import urllib

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from App_Author.forms import NewsForm
from App_Author.models import *
from App_News.models import *
from App_Accounts.decorators import unauthenticated_user
from App_Accounts.forms import *
from bdglobalnews import settings


@unauthenticated_user
def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('App_News:index')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'App_Accounts/signup.html', context)


@unauthenticated_user
def loginview(request):
    if request.method == "POST":
        user_name = request.POST.get('username_field')
        password = request.POST.get('password_field')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            if request.user.profile.is_author:
                return redirect('App_Author:author_dashboard')
            elif request.user.profile.is_editor or request.user.is_authenticated:
                return redirect('App_Account:subscriber_dashboard')
            else:
                return redirect('App_News:index')
        else:
            messages.info(request, "Enter correct username and password", extra_tags="login_error")
            return redirect('App_Account:login')
    return render(request, 'App_Accounts/login.html')


def logoutview(request):
    logout(request)
    return redirect('App_Account:login')


@login_required(login_url="App_Account:login")
def Dashboard(request):
    if request.user.is_authenticated and request.user.profile.is_author == False:
        return render(request, 'Subscriber/dashboard.html')
    if request.user.is_authenticated and request.user.profile.is_author:
        return redirect('App_Author:author_dashboard')



def UpdateProfile(request):
    try:
        if request.method == "POST":
            form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
            form_2 = UserUpdateForm(request.POST or None, instance=request.user)
            if form.is_valid() and form_2.is_valid():
                form.save()
                form_2.save()
                messages.success(request, "Profile Update Successfully", extra_tags="profit")
                return redirect('App_Account:subscriber_update')
        else:
            form = ProfileUpdateForm(instance=request.user.profile)
            form_2 = UserUpdateForm(instance=request.user)
    except:
        return redirect('App_Account:subscriber_update')
    context = {
        'form': form,
        'form_2': form_2,
        'profile_pic': Profile.objects.get(user=request.user),
    }
    return render(request, 'Subscriber/update_profile.html', context)


@login_required(login_url="App_Account:login")
def PasswordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!', extra_tags="pass_change")
            return redirect('App_Account:passwordchange')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Subscriber/change_password.html', {
        'form': form
    })


@login_required(login_url="App_Account:login")
def BecomeSubscriberView(request):
    is_subscriber = False
    is_editor = False
    if Subscriber.objects.filter(user=request.user).exists():
        subs=Subscriber.objects.get(user=request.user)
        print("agei subscriber hoyse")
        if subs.status:
            is_editor = True
            print("eta to editor")
        is_subscriber=True
        print("editor hoy nai")
    if request.method=="POST":
        subs=Subscriber.objects.create(user=request.user)
        subs.save()
        messages.success(request,"You are now a subscriber user",extra_tags="subscriber")
        return redirect(request.POST['next'])
    context={
        'is_subscriber':is_subscriber,
        'is_editor':is_editor,
    }
    return render(request, 'Subscriber/becomesubscriber.html',context)


@login_required(login_url='App_Accounts:login')
def MyAuthorNews(request):
    try:
        my_namer=EditorList.objects.get(editor=request.user)
        my_author=my_namer.author
        my_author_news=News.objects.filter(author=my_author)
    except:
        return redirect('App_Account:subscriber_dashboard')
    context={
        'my_author_news':my_author_news,
    }
    return render(request,'Subscriber/myauthornews.html',context)


@login_required(login_url='App_Accounts:login')
def UpdateAuthorNews(request,id):
    my_namer = EditorList.objects.get(editor=request.user)
    my_author = my_namer.author
    single_news = News.objects.get(author=my_author, id=id)
    if request.method == "POST":
        form = NewsForm(request.POST or None, request.FILES, instance=single_news)
        if form.is_valid():
            u = form.save(commit=False)
            if u.draft is True:
                u.publish = False
                u.save()
            else:
                u.save()
            messages.success(request, "News Updated Successfully", extra_tags="news_update")
            return redirect(request.POST['next'])
    else:
        form = NewsForm(instance=single_news)
    context={
        'form':form,
        'single_news':single_news,
    }
    return render(request,'Subscriber/authornewsupdate.html',context)


def MyAuthorComments(request):
    try:
        my_namer = EditorList.objects.get(editor=request.user)
        my_author = my_namer.author
        all_news = News.objects.filter(author=my_author)
        context = {
            'all_news': all_news,
        }
    except:
        return redirect('App_Account:subscriber_dashboard')
    return render(request,'Subscriber/my_author_comments.html',context)


def MyAuthorCommentView(request,id):
    try:
        single_news = News.objects.get(id=id)
        is_spam = False
        if single_news.spam.filter(id=request.user.id).exists():
            is_spam = True
        context = {
            'single_news': single_news,
            'is_spam': is_spam,
        }
        return render(request, 'Subscriber/my_author_single_comment.html', context)
    except:
        return redirect('App_Account:my_author_comments')

def MyAuthorDeleteComment(request):
    try:
        id = request.POST['my_author_comment_delete']
        print("deleted")
        single_news = Comment.objects.get(id=id)
        single_news.delete()
        messages.success(request, "Comment Deleted Successfully", extra_tags="comment_delete")
        return redirect(request.POST['next'])
    except:
        return redirect('App_Account:my_author_delete_comment')
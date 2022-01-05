from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from App_News.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from App_News.token import account_activation_token
import datetime
from django.db.models import Count

from django.utils import timezone

def index(request):
    try:
        categories = Category.objects.all()
        sliders=Sliderimage.objects.all().order_by("-id")
        popular_news = News.objects.filter(publish=True, publish_date__lte=date.today()).annotate(
            q_count=Count('like')).order_by('-q_count')[:5]
        latest_news = News.objects.filter(publish=True, publish_date__lte=date.today()).order_by('-post_date')[:5]

    except:
        return HttpResponse("<h1>Something Went Wrong</h1>")
    context = {
        'categories': categories,
        'popular_news': popular_news,
        'latest_news': latest_news,
        'sliders':sliders,
        'today': timezone.now()
    }
    return render(request, 'App_News/b_index.html', context)


def send_verify_email(request, email, com):
    print("verify process start")
    user = UserVerify.objects.create(email=email)
    user.save()
    print(user)
    em = email
    current_site = get_current_site(request)
    message = render_to_string('App_News/message.html', {
        'user': em,
        'domain': current_site.domain,
        'u_email': em,
        'token': account_activation_token.make_token(em),
    })
    to_email = em
    email = EmailMessage(
        "Email Verification", message, to=[to_email]
    )
    email.send()


def viewnews(request, title, id):
    try:
        news_post = get_object_or_404(News, id=id)
        suggest_news = News.objects.filter(category=news_post.category, publish=True).exclude(id=news_post.id).order_by(
            "-post_date")[:4]
        featured_news = News.objects.filter(category__name="Featured", publish=True,
                                            publish_date__lte=date.today()).order_by("-post_date")
        print(featured_news)
        cats = Category.objects.all().order_by('-id')
        is_liked = False
        is_spam = False
        if news_post.like.filter(id=request.user.id).exists():
            is_liked = True
        if news_post.spam.filter(id=request.user.id).exists():
            is_spam = True
        comments = Comment.objects.filter(post=news_post, reply=None, status=True).order_by('-id')
        if request.user.is_authenticated:
            if request.method == "POST":
                comment_form = CommentForm(request.POST or None)
                if comment_form.is_valid():
                    content = comment_form.cleaned_data.get('content')
                    reply_id = request.POST.get('comment_id')
                    comment_qs = None
                    if reply_id:
                        comment_qs = Comment.objects.get(id=reply_id)
                    comment = Comment.objects.create(
                        post=news_post, user=request.user, content=content, status=True, reply=comment_qs
                    )
                    comment.save()
            else:
                comment_form = CommentForm()
        else:
            if request.method == "POST":
                comment_form = UnauthCommentForm(request.POST or None)
                if comment_form.is_valid():
                    un_name = comment_form.cleaned_data.get('name')
                    un_email = comment_form.cleaned_data.get('email')
                    un_content = comment_form.cleaned_data.get('content')
                    reply_id = request.POST.get('comment_id')
                    comment_qs = None
                    if reply_id:
                        comment_qs = Comment.objects.get(id=reply_id)
                    print("codition part")
                    if UserVerify.objects.filter(email=un_email).exists():
                        print("user to age akber comment korse")
                        user = UserVerify.objects.get(email=un_email)
                        if user.status:
                            comment = Comment.objects.create(
                                post=news_post,
                                user=None,
                                name=un_name,
                                email=un_email,
                                content=un_content,
                                status=True,
                                reply=comment_qs
                            )
                            comment.save()
                        else:
                            print("age comment korle ki hobe beta email verify kore nai")
                            comment = Comment.objects.create(
                                post=news_post,
                                user=None,
                                name=un_name,
                                email=un_email,
                                content=un_content,
                                status=False,
                                reply=comment_qs)
                            comment.save()
                    else:
                        print("na first time user comment korlo")
                        comment = Comment.objects.create(
                            post=news_post,
                            user=None,
                            name=un_name,
                            email=un_email,
                            content=un_content,
                            status=False,
                            reply=comment_qs)
                        comment.save()
                        send_verify_email(request, un_email, comment.id)

            else:
                comment_form = UnauthCommentForm()

    except:
        return redirect('App_News:index')

    context = {
        'single_post': news_post,
        'cats': cats,
        'is_liked': is_liked,
        'is_spam': is_spam,
        'comments': comments,
        'comment_form': comment_form,
        'suggest_news': suggest_news,
        'featured_news': featured_news,
        'categories': Category.objects.all(),
        'today': timezone.now(),
        'latest_news' : News.objects.filter(publish=True, publish_date__lte=date.today()).order_by('-post_date')[:5],
    }
    if request.is_ajax():
        print("ajax")
        html = render_to_string('App_News/comment_section.html', context, request=request)
        return JsonResponse({'form': html})
    return render(request, 'App_News/details.html', context)


def load_cities(request):
    category = request.GET.get('category')
    sub_cats = Subcategory.objects.filter(category=category)
    print(sub_cats)
    return render(request, 'App_News/city_dropdown_list_options.html', {'sub_cats': sub_cats})


def newslike(request):
    try:
        news_post = get_object_or_404(News, id=request.POST.get('id'))
        is_liked = False
        if news_post.like.filter(id=request.user.id).exists():
            news_post.like.remove(request.user)
            is_liked = False
        else:
            news_post.like.add(request.user)
            is_liked = True
    except:
        return HttpResponse("Something went wrong")
    context = {
        'single_post': news_post,
        'is_liked': is_liked,
        'total_like': news_post.like_count(),
    }
    if request.is_ajax():
        html = render_to_string('App_News/reaction_section.html', context, request=request)
        return JsonResponse({'form': html})


def activate(request, email, token):
    try:
        user = UserVerify.objects.get(email=email)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        user.status = True
        user.save()
        com = Comment.objects.filter(email=email)
        for c in com:
            c.status = True
            c.save()
        return redirect('App_News:index')
    else:
        return HttpResponse('Activation link is invalid!')


def ViewAuthorPost(request, user):
    try:
        author_data = get_object_or_404(User, username=user)
        all_news = News.objects.filter(author=author_data, publish=True)
        featured_news = News.objects.filter(category__name="Featured", publish=True,
                                            publish_date__lte=date.today()).order_by("-post_date")
    except:
        return redirect('App_News:index')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_news, 50)
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)
    context = {
        'author_data': author_data,
        'all_news': all_news,
        'featured_news': featured_news,
        'categories': Category.objects.all(),
        'today': timezone.now(),
        'latest_news': News.objects.filter(publish=True, publish_date__lte=date.today()).order_by('-post_date')[:5],
    }
    return render(request, 'App_News/author.html', context)


def ViewCategory(request, cat, id):
    try:
        single_category = Category.objects.get(id=id)
        all_news = News.objects.filter(category_id=single_category, publish=True,
                                       publish_date__lte=date.today()).order_by("-post_date")
        featured_news = News.objects.filter(category__name="Featured", publish=True,
                                            publish_date__lte=date.today()).order_by("-post_date")
    except:
        return redirect('App_News:index')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_news, 50)
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)
    context = {
        'single_category': single_category,
        'featured_news': featured_news,
        'all_news': all_news,
        'categories': Category.objects.all(),
        'today':timezone.now(),
        'latest_news': News.objects.filter(publish=True, publish_date__lte=date.today()).order_by('-post_date')[:5],
    }

    return render(request, 'App_News/category.html', context)

def ViewSubcategory(request,cat_id,sub_id):
    try:
        print("sub category page")
        single_category = Category.objects.get(id=cat_id)
        print(single_category)
        single_subcategor=Subcategory.objects.get(category=single_category,id=sub_id)
        print(single_subcategor)
        all_news = News.objects.filter(category=single_category,subcategory=single_subcategor, publish=True,
                                       publish_date__lte=date.today()).order_by("-post_date")
        featured_news = News.objects.filter(category__name="Featured", publish=True,
                                            publish_date__lte=date.today()).order_by("-post_date")
    except:
        return redirect('App_News:index')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_news, 50)
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)
    context = {
        'single_category': single_category,
        'single_subcategory':single_subcategor,
        'featured_news': featured_news,
        'all_news': all_news,
        'categories': Category.objects.all(),
        'today': timezone.now(),
        'latest_news': News.objects.filter(publish=True, publish_date__lte=date.today()).order_by('-post_date')[:5],
    }

    return render(request, 'App_News/subcategory.html', context)

def Newssearch(request):
    all_news = News.objects.filter(publish=True, publish_date__lte=date.today())
    if request.method == "POST":
        query = request.POST['s']
        if query:
            all_news = all_news.filter(
                Q(news_title__icontains=query) |
                Q(category__name__icontains=query) |
                Q(subcategory__name__icontains=query) |
                Q(short_description__icontains=query)
            ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(all_news, 20)
        try:
            all_news = paginator.page(page)
        except PageNotAnInteger:
            all_news = paginator.page(1)
        except EmptyPage:
            all_news = paginator.page(paginator.num_pages)
    context = {
        'all_news': all_news,
        'categories': Category.objects.all(),
        'today': timezone.now(),
        'latest_news': News.objects.filter(publish=True, publish_date__lte=date.today()).order_by('-post_date')[:5],
    }
    return render(request, 'App_News/search.html', context)

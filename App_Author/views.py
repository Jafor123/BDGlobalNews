from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, Http404, get_object_or_404
from App_Accounts.forms import ProfileUpdateForm, UserUpdateForm
from App_Accounts.models import Profile, Subscriber
from App_Author.forms import *
from App_Author.models import *


def AuthorDashboard(request):
    if request.user.is_authenticated and request.user.profile.is_author:
        return render(request, 'App_Author/index.html')
    else:
        return redirect('App_Account:login')


@login_required(login_url='App_Accounts:login')
def addnews(request):
    if request.user.profile.is_author:
        if request.method == "POST":
            form = NewsForm(request.POST or None, request.FILES)
            if form.is_valid():
                u = form.save(commit=False)
                if u.draft is True:
                    u.publish = False
                    u.author = request.user
                    u.save()
                else:
                    u.author = request.user
                    u.save()
                messages.success(request, "News Saved Successfully", extra_tags="news_add")
                return redirect(request.POST['next'])
        else:
            form = NewsForm()
        context = {
            'form': form
        }
        return render(request, 'App_Author/add_news.html', context)
    else:
        return Http404("You are not a Author")


@login_required(login_url='App_Accounts:login')
def ManageView(request):
    if request.user.profile.is_author:
        my_news = News.objects.filter(author=request.user)
        context = {
            'my_news': my_news,
        }
        return render(request, 'App_Author/manage_news.html', context)
    else:
        return redirect('App_Account:subscriber_dashboard')


@login_required(login_url='App_Accounts:login')
def UpdateView(request, id):
    if request.user.profile.is_author:
        single_news = News.objects.get(author=request.user, id=id)
        if request.method == "POST":
            form = NewsForm(request.POST or None, request.FILES, instance=single_news)
            if form.is_valid():
                u = form.save(commit=False)
                if u.draft is True:
                    u.publish = False
                    u.author = request.user
                    u.save()
                else:
                    u.author = request.user
                    u.save()
                messages.success(request, "News Updated Successfully", extra_tags="news_update")
                return redirect(request.POST['next'])
        else:
            form = NewsForm(instance=single_news)
        context = {
            'single_news': single_news,
            'form': form,
        }
        return render(request, 'App_Author/update_news.html', context)
    else:
        return redirect('App_Account:subscriber_dashboard')


@login_required(login_url='App_Accounts:login')
def DeleteView(request):
    if request.user.profile.is_author:
        try:
            id = request.POST['delc']
            print(id)
            single_news = News.objects.get(author=request.user, id=id)
            single_news.delete()
            messages.success(request, "News Deleted Successfully", extra_tags="news_delete")
            return redirect('App_Author:manage_news')
        except:
            return redirect('App_Author:author_dashboard')

    else:
        return redirect('App_Account:subscriber_dashboard')


@login_required(login_url='App_Accounts:login')
def UpdateAuthorProfile(request):
    try:
        if request.method == "POST":
            form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
            form_2 = UserUpdateForm(request.POST or None, instance=request.user)
            if form.is_valid() and form_2.is_valid():
                form.save()
                form_2.save()
                messages.success(request, "Profile Update Successfully", extra_tags="profit")
                return redirect(request.POST["next"])
        else:
            form = ProfileUpdateForm(instance=request.user.profile)
            form_2 = UserUpdateForm(instance=request.user)
    except:
        return redirect('App_Author:author_dashboard')
    context = {
        'form': form,
        'form_2': form_2,
        'profile_pic': Profile.objects.get(user=request.user),
    }
    return render(request, 'App_Author/update_author_profile.html', context)


@login_required(login_url='App_Accounts:login')
def CommentListView(request):
    if request.user.profile.is_author:
        try:
            all_news = News.objects.filter(author=request.user)
            context = {
                'all_news': all_news,
            }
            return render(request, 'App_Author/comment_list.html', context)
        except:
            return redirect('App_Author:author_dashboard')

    else:
        return redirect('App_Author:author_dashboard')


@login_required(login_url='App_Accounts:login')
def SingleCommentView(request, id):
    try:
        single_news = News.objects.get(id=id)
        is_spam = False
        if single_news.spam.filter(id=request.user.id).exists():
            is_spam = True
        context = {
            'single_news': single_news,
            'is_spam': is_spam,
        }
        return render(request, 'App_Author/single_comment_view.html', context)
    except:
        return redirect('App_Author:comment_list_view')


@login_required(login_url='App_Accounts:login')
def DeleteCommentView(request):
    if request.user.profile.is_author:
        try:
            id = request.POST['delc']
            print(id)
            single_news = Comment.objects.get(id=id)
            single_news.delete()
            messages.success(request, "Comment Deleted Successfully", extra_tags="comment_delete")
            return redirect(request.POST['next'])
        except:
            return redirect('App_Author:comment_list_view')

    else:
        return redirect('App_Account:subscriber_dashboard')


@login_required(login_url='App_Accounts:login')
def spamview(request, id):
    try:
        if request.method == "POST":
            print("1st step")
            comm = Comment.objects.get(id=request.POST['comment_id'])
            if comm.spam == True:
                comm.spam = False
                comm.status=True
                comm.save()
            else:
                comm.spam = True
                comm.status=False
                comm.save()
            if comm.email != "":
                print("unauth")
                user_get = UserVerify.objects.get(email=comm.email)
                user_get.status = False
                user_get.save()
            else:
                print("auth")
                single_news = get_object_or_404(News, id=id)
                if single_news.spam.filter(id=comm.user.id).exists():
                    single_news.spam.remove(comm.user)
                else:
                    single_news.spam.add(comm.user)

            return redirect(request.POST['next'])

    except:
        return HttpResponse("Something went wrong")


@login_required(login_url='App_Accounts:login')
def CategoryApply(request):
    if request.method == "POST":
        form = CategoryApplyForm(request.POST or None)
        if form.is_valid():
            cats = form.save(commit=False)
            cats.user = request.user
            cats.save()
            messages.success(request, "Successfully apply for New Category", extra_tags="apply_cats")
            return redirect(request.POST['next'])
    else:
        form = CategoryApplyForm()
    context = {
        'form': form,
        'apply_category': Categoryapply.objects.filter(user=request.user)
    }
    return render(request, 'App_Author/apply_for_category.html', context)


@login_required(login_url='App_Accounts:login')
def ApplyCategoryDelete(request):
    try:
        id = request.POST['cat_id']
        print(id)
        single_news = Categoryapply.objects.get(id=id)
        single_news.delete()
        messages.success(request, "Data Deleted Successfully", extra_tags="category_delete")
        return redirect(request.POST['next'])
    except:
        return redirect('App_Author:category_apply')


@login_required(login_url='App_Accounts:login')
def CategoryApplyUpdate(request, id):
    category_app = Categoryapply.objects.get(user=request.user, id=id)
    if request.method == "POST":
        form = CategoryApplyForm(request.POST or None, instance=category_app)
        if form.is_valid():
            form.save()
            messages.success(request, "Application Update Successfully", extra_tags="update_category")
            return redirect('App_Author:category_apply')
    else:
        form = CategoryApplyForm(instance=category_app)
    context = {
        'form': form,
        'category_app': category_app,
        'apply_category': Categoryapply.objects.filter(user=request.user)
    }
    return render(request, 'App_Author/update_for_category.html', context)


@login_required(login_url='App_Accounts:login')
def UserListView(request):
    subs = Subscriber.objects.filter(status=False)
    context = {
        'all_Subscriber': subs,
    }
    return render(request, 'App_Author/userlistview.html', context)


@login_required(login_url='App_Accounts:login')
def MakeEditorView(request):
    try:
        user_list_id = request.POST['user_list_id']
        subs = Subscriber.objects.get(id=user_list_id)
        subs.status = True
        subs.save()
        pro = Profile.objects.get(user=subs.user)
        pro.is_editor = True
        pro.save()
        en_editor = EditorList.objects.create(
            author=request.user, editor=subs.user
        )
        en_editor.save()
        messages.success(request, "User Successfully Become Your Editor", extra_tags="editor_make")
        return redirect(request.POST['next'])
    except:
        return redirect('App_Author:userlist_view')


@login_required(login_url='App_Accounts:login')
def RemoveEditorView(request):
    try:
        editor_list_id = request.POST['editor_list_id']
        editor_ = EditorList.objects.get(id=editor_list_id)
        pro = Profile.objects.get(user=editor_.editor)
        pro.is_editor = False
        pro.save()
        if Subscriber.objects.filter(user=editor_.editor).exists():
            subs = Subscriber.objects.get(user=editor_.editor)
            subs.status = False
            subs.save()
        editor_.delete()
        messages.success(request, "You have successfully Remove this Editor", extra_tags="editor_remove")
        return redirect(request.POST['next'])
    except:
        return redirect('App_Author:userlist_view')


@login_required(login_url='App_Accounts:login')
def MyEditorList(request):
    my_editors = EditorList.objects.filter(author=request.user)
    context = {
        'my_editors': my_editors,
    }
    return render(request, 'App_Author/my_editorlist.html', context)


@login_required(login_url='App_Accounts:login')
def SubcategoryApply(request):
    if request.method == "POST":
        form = SubcategoryApplyForm(request.POST or None)
        if form.is_valid():
            cats = form.save(commit=False)
            cats.user = request.user
            cats.save()
            messages.success(request, "Successfully apply for Sub Category", extra_tags="apply_subcats")
            return redirect(request.POST['next'])
    else:
        form = SubcategoryApplyForm()
    context = {
        'form': form,
        'apply_subcategory': Subcategoryapply.objects.filter(user=request.user)
    }
    return render(request, 'App_Author/apply_for_subcategory.html', context)


@login_required(login_url='App_Accounts:login')
def ApplySubcategoryDelete(request):
    try:
        id = request.POST['subcat_id']
        single_news = Subcategoryapply.objects.get(id=id)
        single_news.delete()
        messages.success(request, "Application Deleted Successfully", extra_tags="subcategory_delete")
        return redirect(request.POST['next'])
    except:
        return redirect('App_Author:subcategory_apply')


@login_required(login_url='App_Accounts:login')
def SubcategoryApplyUpdate(request, id):
    subcategory_app = Subcategoryapply.objects.get(user=request.user, id=id)
    if request.method == "POST":
        form = SubcategoryApplyForm(request.POST or None, instance=subcategory_app)
        if form.is_valid():
            form.save()
            messages.success(request, "Application Update Successfully", extra_tags="update_subcategory")
            return redirect('App_Author:subcategory_apply')
    else:
        form = SubcategoryApplyForm(instance=subcategory_app)
    context = {
        'form': form,
        'subcategory_app': subcategory_app,
        'apply_subcategory': Subcategoryapply.objects.filter(user=request.user)
    }
    return render(request, 'App_Author/update_for_subcategory.html', context)


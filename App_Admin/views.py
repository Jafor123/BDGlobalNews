from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from App_Accounts.forms import *
from App_Accounts.models import *
from App_Admin.forms import *


@login_required(login_url='App_Admin:superadmin_login')
def Dashboard(request):
    if request.user.is_superuser:
        return render(request, 'App_Admin/index.html')
    else:
        return redirect('App_Account:subscriber_dashboard')


def SuperadminLogin(request):
    if request.user.is_authenticated:
        return redirect('App_Admin:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('App_Admin:dashboard')
            else:
                messages.info(request, "Enter correct username and password", extra_tags="login")
                return redirect('App_Admin:superadmin_login')

        else:
            return render(request, 'App_Admin/login.html')


def SuperadminLogout(request):
    logout(request)
    return redirect('App_Admin:superadmin_login')


def Userlist(request):
    if request.user.is_superuser:
        all_users = User.objects.filter(is_superuser=False)
        context = {
            'all_users': all_users,
        }
        return render(request, 'App_Admin/userlist.html', context)
    else:
        return redirect('App_News:index')


def UserDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['user_delc']
            single_user = User.objects.get(id=id)
            single_user.delete()
            messages.success(request, "User Deleted Successfully", extra_tags="user_delete")
            return redirect('App_Admin:userlist')
        except:
            return redirect('App_Admin:dashboard')
    else:
        return redirect('App_News:index')


def UserUpdate(request, id):
    if request.user.is_superuser:
        try:
            single_user = User.objects.get(id=id)
            if request.method == "POST":
                form = ProfileUpdateForm(request.POST or None, request.FILES, instance=single_user.profile)
                form_2 = UserUpdateForm(request.POST or None, instance=single_user)
                if form.is_valid() and form_2.is_valid():
                    form.save()
                    form_2.save()
                    messages.success(request, "User Profile Update Successfully", extra_tags="user_profile")
                    return redirect(request.POST['next'])
            else:
                form = ProfileUpdateForm(instance=single_user.profile)
                form_2 = UserUpdateForm(instance=single_user)
        except:
            return redirect('App_Admin:dashboard')
        context = {
            'form': form,
            'form_2': form_2,
            'single_user': single_user,
        }
        return render(request, 'App_Admin/userupdate.html', context)
    else:
        return redirect('App_News:index')


def CategoryView(request):
    if request.user.is_superuser:
        try:
            all_categoris = Category.objects.all()
            if request.method == "POST":
                form = CategoryForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Category Added successfully", extra_tags="add_cat")
                    return redirect(request.POST['next'])
            else:
                form = CategoryForm()

        except:
            return redirect('App_Admin:dashboard')
        context = {
            'all_categoris': all_categoris,
            'form': form,
        }
        return render(request, 'App_Admin/category_view.html', context)
    else:
        return redirect('App_News:index')


def CategoryDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['cat_delc']
            single_category = Category.objects.get(id=id)
            single_category.delete()
            messages.success(request, "Category Deleted Successfully", extra_tags="cat_delete")
            return redirect('App_Admin:category_view')
        except:
            return redirect('App_Admin:category_view')
    else:
        return redirect('App_News:index')


def CategoryUpdate(request, id):
    if request.user.is_superuser:
        try:
            single_cat = Category.objects.get(id=id)
            if request.method == "POST":
                form = CategoryForm(request.POST or None, instance=single_cat)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Category Updated Successfully", extra_tags="cat_update")
                    return redirect('App_Admin:category_view')
            else:
                form = CategoryForm(instance=single_cat)
        except:
            return redirect('App_Admin:category_view')
        context = {
            'form': form,
            'single_cat': single_cat,
            'all_categoris': Category.objects.all(),
        }
        return render(request, 'App_Admin/category_update.html', context)
    else:
        return redirect('App_News:index')


def SubcategoryView(request):
    if request.user.is_superuser:
        try:
            all_subcategoris = Subcategory.objects.all()
            if request.method == "POST":
                form = SubCategoryForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Subcategory Added successfully", extra_tags="add_subcat")
                    return redirect(request.POST['next'])
            else:
                form = SubCategoryForm()

        except:
            return redirect('App_Admin:dashboard')
        context = {
            'all_subcategoris': all_subcategoris,
            'form': form,
        }
        return render(request, 'App_Admin/subcategory_view.html', context)
    else:
        return redirect('App_News:index')


def SubcategoryUpdate(request, id):
    if request.user.is_superuser:
        try:
            single_subcat = Subcategory.objects.get(id=id)
            if request.method == "POST":
                form = SubCategoryForm(request.POST or None, instance=single_subcat)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Category Updated Successfully", extra_tags="subcat_update")
                    return redirect('App_Admin:subcategory_view')
            else:
                form = SubCategoryForm(instance=single_subcat)
        except:
            return redirect('App_Admin:subcategory_view')
        context = {
            'form': form,
            'single_subcat': single_subcat,
            'all_subcategoris': Subcategory.objects.all(),
        }
        return render(request, 'App_Admin/subcategory_update.html', context)
    else:
        return redirect('App_News:index')


def SubcategoryDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['subcat_delc']
            single_subcategory = Subcategory.objects.get(id=id)
            single_subcategory.delete()
            messages.success(request, "Sub Category Deleted Successfully", extra_tags="subcat_delete")
            return redirect('App_Admin:subcategory_view')
        except:
            return redirect('App_Admin:subcategory_view')
    else:
        return redirect('App_News:index')


def CategoryRequest(request):
    if request.user.is_superuser:
        try:
            request_category = Categoryapply.objects.all()
        except:
            return redirect('App_Admin:dashboard')
        context = {
            'request_category': request_category,
        }
        return render(request, 'App_Admin/category_request.html', context)
    else:
        return redirect('App_News:index')


def CategoryRequestDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['cat_apply_delc']
            single_subcategory = Categoryapply.objects.get(id=id)
            single_subcategory.delete()
            messages.success(request, "Add Category Request Deleted Successfully", extra_tags="cat_request_delete")
            return redirect('App_Admin:category_request')
        except:
            return redirect('App_Admin:category_request')
    else:
        return redirect('App_News:index')


def CategoryRequestApprove(request, id):
    if request.user.is_superuser:
        try:
            cat_apply = Categoryapply.objects.get(id=id)
            cats = Category.objects.create(
                name=cat_apply.name
            )
            cats.save()
            cat_apply.status = True
            cat_apply.save()
            messages.success(request, "Category Request Accepted", extra_tags="cat_request_approve")
            return redirect('App_Admin:category_request')
        except:
            return redirect('App_Admin:category_request')
    else:
        return redirect('App_News:index')


def SubcategoryRequest(request):
    if request.user.is_superuser:
        try:
            request_subcategory = Subcategoryapply.objects.all()
        except:
            return redirect('App_Admin:dashboard')
        context = {
            'request_subcategory': request_subcategory,
        }
        return render(request, 'App_Admin/subcategory_request.html', context)
    else:
        return redirect('App_News:index')


def SubcategoryRequestDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['subcat_apply_delc']
            single_subcategory = Subcategoryapply.objects.get(id=id)
            single_subcategory.delete()
            messages.success(request, "Sub Category Request Delete Successfully", extra_tags="subcat_request_delete")
            return redirect('App_Admin:subcategory_request')
        except:
            return redirect('App_Admin:subcategory_request')
    else:
        return redirect('App_News:index')


def SubcategoryRequestApprove(request, id):
    if request.user.is_superuser:
        try:
            cat_apply = Subcategoryapply.objects.get(id=id)
            cat_apply.status = True
            cat_apply.save()
            cats = Subcategory.objects.create(
                category=cat_apply.category, name=cat_apply.name
            )
            cats.save()
            messages.success(request, "Sub category Request Accepted", extra_tags="subcat_request_approve")
            return redirect('App_Admin:subcategory_request')
        except:
            return redirect('App_Admin:subcategory_request')
    else:
        return redirect('App_News:index')


def NewsList(request):
    if request.user.is_superuser:
        all_news = News.objects.all().order_by('-post_date')
        context = {
            'all_news': all_news,
        }
        return render(request, 'App_Admin/newsmanagement.html', context)
    else:
        return redirect('App_News:index')


def Newsadd(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = NewsAddForm(request.POST or None, request.FILES)
            if form.is_valid():
                u = form.save()
                if u.draft is True:
                    u.publish = False
                    u.save()
                else:
                    u.save()
                messages.success(request, "News Saved Successfully", extra_tags="news_add")
                return redirect(request.POST['next'])
        else:
            form = NewsAddForm()
        context = {
            'form': form,
        }
        return render(request, 'App_Admin/newsadd.html', context)
    else:
        return redirect('App_News:index')


def Newsupdate(request, id):
    if request.user.is_superuser:
        single_news = News.objects.get(id=id)
        if request.method == "POST":
            form = NewsAddForm(request.POST or None, request.FILES, instance=single_news)
            if form.is_valid():
                u = form.save()
                if u.draft is True:
                    u.publish = False
                    u.save()
                else:
                    u.save()
                messages.success(request, "News Update Successfully", extra_tags="news_update")
                return redirect(request.POST['next'])
        else:
            form = NewsAddForm(instance=single_news)
        context = {
            'form': form,
            'single_news': single_news,
        }
        return render(request, 'App_Admin/newsupdate.html', context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def Newsdelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['news_delc']
            single_news = News.objects.get(id=id)
            single_news.delete()
            messages.success(request, "News Deleted Successfully", extra_tags="news_delete")
            return redirect('App_Admin:news_list')
        except:
            return redirect('App_Admin:dashboard')

    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def UserVerifyList(request):
    if request.user.is_superuser:
        try:
            user_list = UserVerify.objects.all().order_by('-id')
            if request.method=="POST":
                form=UserverifyListForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request,"User Info saved successfully",extra_tags="add_user_verify")
                    return redirect(request.POST['next'])
            else:
                form=UserverifyListForm()
        except:
            user_list = None
        context = {
            'user_list': user_list,
            'form':form,
        }
        return render(request, 'App_Admin/userverifylist.html', context)
    else:
        return redirect('App_News:index')

@login_required(login_url='App_Admin:superadmin_login')
def UpdateUserVerifyList(request, id):
    if request.user.is_superuser:
        try:
            single_user=UserVerify.objects.get(id=id)
            user_list = UserVerify.objects.all().order_by('-id')
            if request.method=="POST":
                form=UserverifyListForm(request.POST or None,instance=single_user)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Data Update successfully",extra_tags="update_userverify")
                    return redirect('App_Admin:user_verify_list')
            else:
                form=UserverifyListForm(instance=single_user)
        except:
            user_list = None
        context = {
            'user_list': user_list,
            'form':form,
            'single_user':single_user,
        }
        return render(request, 'App_Admin/updateuserverifylist.html', context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def DeleteUserVerifyList(request):
    if request.user.is_superuser:
        try:
            id = request.POST['user_verify_delete']
            single_user = UserVerify.objects.get(id=id)
            single_user.delete()
            messages.success(request, "User Deleted Successfully", extra_tags="user_delete")
            return redirect('App_Admin:user_verify_list')
        except:
            return redirect('App_Admin:dashboard')
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def CommentList(request):
    if request.user.is_superuser:
        try:
            comment_list=Comment.objects.all().order_by("-timestamp")
            context={
                'comment_list':comment_list,
            }
        except:
            return redirect('App_Admin:dashboard')
        return render(request,'App_Admin/commentslist.html',context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def CommentUpdate(request,id):
    if request.user.is_superuser:
        try:
            comment_id=Comment.objects.get(id=id)
            if request.method=="POST":
                form=CommentUpdateForm(request.POST or None,instance=comment_id)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Comment Update successfully',extra_tags='comment_update')
                    return redirect(request.POST['next'])
            else:
                form=CommentUpdateForm(instance=comment_id)
        except:
            return redirect('App_Admin:comment_list')

        context={
            'form':form,
            'comment_id':comment_id,
        }
        return render(request, 'App_Admin/commentupdate.html',context)
    else:
        return redirect('App_News:index')

@login_required(login_url='App_Admin:superadmin_login')
def CommentDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['comment_delte_data']
            single_comment = Comment.objects.get(id=id)
            single_comment.delete()
            messages.success(request, "Comment Deleted Successfully", extra_tags="comment_delete")
            return redirect('App_Admin:comment_list')
        except:
            return redirect('App_Admin:dashboard')
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def SubscriberList(request):
    if request.user.is_superuser:
        try:
            subscriber_list=Subscriber.objects.all().order_by('-id')
            if request.method=="POST":
                form=SubscriberForm(request.POST or None)
                if form.is_valid():
                    user=form.cleaned_data.get('user')
                    if Subscriber.objects.filter(user=user).exists():
                        messages.success(request, "Subscriber Already Added", extra_tags="subscriber_alert")
                    else:
                        form.save()
                        messages.success(request,"Subscriber Added succesfully",extra_tags="subscriber_add")
                    return redirect(request.POST['next'])
            else:
                form=SubscriberForm()
            context={
                'subscriber_list':subscriber_list,
                'form':form,
            }
        except:
            return redirect('App_Admin:dashboard')
        return render(request,'App_Admin/subscriberlist.html',context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def SubscriberDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['subscriber_id']
            single_subscriber = Subscriber.objects.get(id=id)
            single_subscriber.delete()
            messages.success(request, "Subscriber Deleted Successfully", extra_tags="subscriber_delete")
            return redirect('App_Admin:subscriber_list')
        except:
            return redirect('App_Admin:dashboard')
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def SubscriberUpdate(request,id):
    if request.user.is_superuser:
        try:
            subscriber_id = Subscriber.objects.get(id=id)
            if request.method == "POST":
                form = SubscriberForm(request.POST or None, instance=subscriber_id)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Subscriber Information Update successfully', extra_tags='subscriber_update')
                    return redirect('App_Admin:subscriber_list')
            else:
                form = SubscriberForm(instance=subscriber_id)
        except:
            return redirect('App_Admin:subscriber_list')

        context = {
            'form': form,
            'subscriber_id':subscriber_id,
            'subscriber_list':Subscriber.objects.all().order_by('-id'),
        }
        return render(request, 'App_Admin/subscriberupdate.html', context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def EditorListView(request):
    if request.user.is_superuser:
        try:
            editor_list = EditorList.objects.all().order_by('-id')
            if request.method == "POST":
                form = EditorForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Editor Added succesfully", extra_tags="add_editor")
                    return redirect(request.POST['next'])
            else:
                form = EditorForm()
            context = {
                'editor_list': editor_list,
                'form': form,
            }
        except:
            return redirect('App_Admin:dashboard')
        return render(request, 'App_Admin/editorlistview.html', context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def EditorDeleteView(request):
    if request.user.is_superuser:
        try:
            id = request.POST['editor_id']
            single_editor = EditorList.objects.get(id=id)
            single_editor.delete()
            messages.success(request, "Editor Deleted Successfully", extra_tags="editor_delete")
            return redirect('App_Admin:editor_list')
        except:
            return redirect('App_Admin:dashboard')
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def EditorUpdateView(request,id):
    if request.user.is_superuser:
        try:
            editor_id = EditorList.objects.get(id=id)
            if request.method == "POST":
                form = EditorForm(request.POST or None, instance=editor_id)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Editor Information Update successfully', extra_tags='editor_update')
                    return redirect('App_Admin:editor_list')
            else:
                form = EditorForm(instance=editor_id)
        except:
            return redirect('App_Admin:editor_list')

        context = {
            'form': form,
            'editor_id':editor_id,
            'editor_list':EditorList.objects.all().order_by('-id')
        }
        return render(request, 'App_Admin/editorupdateview.html', context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def Profileview(request):
    if request.user.is_superuser:
        try:
            profile_list = Profile.objects.all().order_by('-id')
            context = {
                'profile_list': profile_list,
            }
        except:
            return redirect('App_Admin:dashboard')
        return render(request, 'App_Admin/profilelist.html', context)
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def ProfileAdd(request):
    if request.user.is_superuser:
        try:
            if request.method == "POST":
                form = ProfileForm(request.POST or None,request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Profile added  successfully', extra_tags='profile_add')
                    return redirect(request.POST['next'])
            else:
                form = ProfileForm()
        except:
            return redirect('App_Admin:editor_list')

        context = {
            'form': form,
        }
        return render(request, 'App_Admin/addprofile.html', context)


@login_required(login_url='App_Admin:superadmin_login')
def ProfileDelete(request):
    if request.user.is_superuser:
        try:
            id = request.POST['profile_id']
            single_profile = Profile.objects.get(id=id)
            single_profile.delete()
            messages.success(request, "Profile Deleted Successfully", extra_tags="profile_delete")
            return redirect('App_Admin:profile_list')
        except:
            return redirect('App_Admin:dashboard')
    else:
        return redirect('App_News:index')


@login_required(login_url='App_Admin:superadmin_login')
def ProfileUpdate(request,id):
    if request.user.is_superuser:
        try:
            user_profile=Profile.objects.get(id=id)
            if request.method == "POST":
                form = ProfileForm(request.POST or None,request.FILES,instance=user_profile)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Profile updated successfully', extra_tags='profile_updated')
                    return redirect(request.POST['next'])
            else:
                form = ProfileForm(instance=user_profile)
        except:
            return redirect('App_Admin:profile_list')

        context = {
            'form': form,
            'user_profile':user_profile,
        }
        return render(request, 'App_Admin/updateprofile.html', context)
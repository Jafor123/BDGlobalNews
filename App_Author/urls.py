from django.urls import path
from App_Author import views
app_name='App_Author'
urlpatterns = [
    path('',views.AuthorDashboard,name='author_dashboard'),
    path('add-news', views.addnews, name='addnews'),
    path('manage-news/', views.ManageView, name='manage_news'),
    path('update-news/<int:id>', views.UpdateView, name='update_news'),
    path('delete-news', views.DeleteView, name='delete_news'),

    path('user-list',views.UserListView,name='userlist_view'),
    path('update-profile',views.UpdateAuthorProfile,name='update_author_profile'),
    path('make-editor',views.MakeEditorView,name='make_editor'),
    path('editor-list',views.MyEditorList,name='editor_list'),
    path('remove-editor',views.RemoveEditorView,name='remove_editor'),

    path('news/comment-list',views.CommentListView,name='comment_list_view'),
    path('news/comment-view/<int:id>',views.SingleCommentView,name='single_comment_view'),
    path('news/comment-delete',views.DeleteCommentView,name='author_delete_comment'),
    path('spam/<int:id>', views.spamview, name="spam_user"),

    path('category-apply',views.CategoryApply,name='category_apply'),
    path('category-delete',views.ApplyCategoryDelete,name='category_delete'),
    path('category-update/<int:id>',views.CategoryApplyUpdate,name='category_apply_update'),

    path('subcategory-apply', views.SubcategoryApply, name='subcategory_apply'),
    path('subcategory-delete', views.ApplySubcategoryDelete, name='subcategory_delete'),
    path('subcategory-update/<int:id>', views.SubcategoryApplyUpdate, name='subcategory_apply_update'),


]

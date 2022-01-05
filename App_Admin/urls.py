from django.urls import path
from App_Admin import views
app_name='App_Admin'
urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('superadmin-login', views.SuperadminLogin, name="superadmin_login"),
    path('superadmin-logout', views.SuperadminLogout, name="superadmin_logout"),
    path('user-list',views.Userlist,name='userlist'),
    path('user-delete',views.UserDelete,name='user_delete'),
    path('user-update/<int:id>',views.UserUpdate,name='user_update'),

    path('category-list',views.CategoryView,name='category_view'),
    path('category-delete',views.CategoryDelete,name='category_delete'),
    path('category-update/<int:id>',views.CategoryUpdate,name='category_update'),

    path('subcategory-list', views.SubcategoryView, name='subcategory_view'),
    path('subcategory-delete', views.SubcategoryDelete, name='subcategory_delete'),
    path('subcategory-update/<int:id>', views.SubcategoryUpdate, name='subcategory_update'),

    path('category-request/',views.CategoryRequest,name='category_request'),
    path('category-request/delete',views.CategoryRequestDelete,name='category_request_delete'),
    path('category-request/approve/<int:id>',views.CategoryRequestApprove,name='category_request_approve'),

    path('subcategory-request/', views.SubcategoryRequest, name='subcategory_request'),
    path('subcategory-request/delete', views.SubcategoryRequestDelete, name='subcategory_request_delete'),
    path('subcategory-request/approve/<int:id>', views.SubcategoryRequestApprove, name='subcategory_request_approve'),

    path('news-list',views.NewsList,name='news_list'),
    path('news-add',views.Newsadd,name='news_add'),
    path('news-delete',views.Newsdelete,name='news_delete'),
    path('news-update/<int:id>',views.Newsupdate,name='news_update'),

    path('user-verify-list', views.UserVerifyList, name='user_verify_list'),
    path('update/user-verify-list/<int:id>', views.UpdateUserVerifyList, name='update_user_verify_list'),
    path('user-verify-list/delete',views.DeleteUserVerifyList,name='delete_user_Verify_list'),

    path('comment-list',views.CommentList,name='comment_list'),
    path('comment-update/<int:id>',views.CommentUpdate,name='commentupdate'),
    path('comment-delete',views.CommentDelete,name='commentdelete'),

    path('subscriber-list',views.SubscriberList,name='subscriber_list'),
    path('subscriber-delete',views.SubscriberDelete,name='subscriber_delete'),
    path('subscriber-update/<int:id>',views.SubscriberUpdate,name='subscriber_update'),

    path('editor-list',views.EditorListView,name='editor_list'),
    path('editor-delete',views.EditorDeleteView,name='editor_delete'),
    path('editor-update/<int:id>',views.EditorUpdateView,name='editor_update'),

    path('profile-list',views.Profileview,name='profile_list'),
    path('profile-delete',views.ProfileDelete,name='profile_delete'),
    path('profile-add',views.ProfileAdd,name='profile_add'),
    path('profile-update/<int:id>',views.ProfileUpdate,name='profile_update'),

]

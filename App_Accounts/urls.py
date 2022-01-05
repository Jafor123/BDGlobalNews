from django.urls import path
from App_Accounts import views
app_name='App_Account'
urlpatterns = [
    path('signup',views.signupview,name='signup'),
    path('login',views.loginview,name='login'),
    path('logout',views.logoutview,name='logout'),
    path('subscriber',views.Dashboard,name='subscriber_dashboard'),
    path('subscriber/update',views.UpdateProfile,name='subscriber_update'),
    path('become-subscriber',views.BecomeSubscriberView,name='become_Subscriber'),
    path('password-change/',views.PasswordChange,name="passwordchange"),
    path('editor-news', views.MyAuthorNews, name='my_author_news'),
    path('editor-news/update/<int:id>',views.UpdateAuthorNews,name='update_editor_news'),

    path('editor-comments', views.MyAuthorComments, name='my_author_comments'),
    path('editor-comments<int:id>',views.MyAuthorCommentView,name='my_author_comment_view'),
    path('editor/comment-delete',views.MyAuthorDeleteComment,name='my_author_delete_comment'),
]

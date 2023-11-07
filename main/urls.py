from django.urls import path
from main import views

urlpatterns = [
    # path('', views.blog_home, name="home"),
    path('', views.BlogHome.as_view(), name="home"),
    
    # path('blog_detail/<str:slug_url>', views.blog_detail, name="blog_detail"),
    path('blog_detail/<str:slug>', views.BlogDetail.as_view(), name="blog_detail"),
    
    # path('contact_us/', views.contact_us, name="contact_us"),
    path('contact_us/', views.ContactUs.as_view(), name="contact_us"),
    
    path('create_new_blog/', views.CreateBlog.as_view(), name="create-blog")
    
]
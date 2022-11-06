from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", views.BlogPostPage.as_view(), name="blog-post"),
    path("post/new/", views.BlogCreatePage.as_view(), name="blog-new"),
    path("post/<int:pk>/update/", views.BlogUpdatePage.as_view(), name="blog-update"),
    path("post/<int:pk>/delete/", views.BlogDeletePage.as_view(), name="blog-delete")
]

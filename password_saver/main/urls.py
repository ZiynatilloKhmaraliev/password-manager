from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index , name="index"),
    path("add-password",views.addPassword,name="addpassword"),
    path("edit/<pk>",views.edit,name="edit"),
    path("delete/<pk>",views.delete,name="delete"),
    path("signup/",views.signUp, name="signup"),
    path('login/',LoginView.as_view(),name='login'),
    path("logout/",views.logoutp,name="logout"),






]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
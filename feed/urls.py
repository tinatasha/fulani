from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.shortcuts import redirect

urlpatterns = [
    url(r'login/edit_profile/feed/', views.feed, name='feed'),
    url(r'login/briefcase', views.briefcase, name='briefcase'),
    url(r'login/medkit', views.medkit, name='medkit'),
    url(r'login/police', views.police, name='police'),
    url(r'signup/', views.signup, name='signup'),
    url(r'login/profile/', views.profile, name="profile"),
    url(r'login/edit_profile/', views.edit_profile, name="edit_profile"),
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
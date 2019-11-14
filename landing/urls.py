from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('partners/', views.partners, name='partners'),
    path('about/', views.about, name='about'),
    path('about-energoservice/', views.about_energoservice, name='about-energoservice'),
    path('projects/', views.project, name='projects'),
    path('projects/<str:slug>/', views.detail, name='detail'),
    path('contacts/', views.contacts, name='contacts'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
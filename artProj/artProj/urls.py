"""
URL configuration for artProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import artApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', artApp.views.index, name='index'),
    # 좋아요 증가 url
    path('project-detail.html/like/<int:pk>/', artApp.views.like, name='like' ),
    # 전시회 1
    path('project-detail.html/', artApp.views.project_detail, name='project_detail'),
    path('project-detail.html/2page', artApp.views.project_detail2, name='project_detail2'),
    path('project-detail.html/3page', artApp.views.project_detail3, name='project_detail3'),
    path('project-detail.html/4page', artApp.views.project_detail4, name='project_detail4'),
    path('project-detail.html/5page', artApp.views.project_detail5, name='project_detail5'),
    # 전시회 2
    path('reMixing-detail.html/', artApp.views.reMixing_detail, name='reMixing_detail'),
    path('reMixing-detail.html/2page', artApp.views.reMixing_detail2, name='reMixing_detail2'),
    path('reMixing-detail.html/3page', artApp.views.reMixing_detail3, name='reMixing_detail3'),
    path('reMixing-detail.html/4page', artApp.views.reMixing_detail4, name='reMixing_detail4'),
    path('reMixing-detail.html/5page', artApp.views.reMixing_detail5, name='reMixing_detail5'),
    # 전시회 3
    path('kim-detail.html/', artApp.views.kim_detail, name='kim_detail1'),
    path('kim-detail.html/2page', artApp.views.kim_detail2, name='kim_detail2'),
    path('kim-detail.html/3page', artApp.views.kim_detail3, name='kim_detail3'),
    path('kim-detail.html/4page', artApp.views.kim_detail4, name='kim_detail4'),
    path('kim-detail.html/5page', artApp.views.kim_detail5, name='kim_detail5'),

    # 홍세연 작가 페이지
    path('artist-page-hong.html', artApp.views.hong_detail, name='hong_detail'),

    # 홍원표 작가 페이지
    path('artist-page-pyo.html', artApp.views.pyo_detail, name='pyo_detail'),

    # 유근택 작가 페이지
    path('artist-page-yoo.html', artApp.views.yoo_detail,name='yoo_detail'),

]


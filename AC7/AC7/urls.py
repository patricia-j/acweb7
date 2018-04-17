"""AC7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cadastro/', cadastro_aluno),
    path('cadastro-de-disciplina/', cadastro_disciplina),
    path('cadastro-de-novo-curso/', cadastro_novo_curso),
    path('cursos/', courses),
    path('ads/', cursos_analise_e_desenvolvimento),
    path('bd/', cursos_banco_de_dados),
    path('redes/', cursos_redes),
    path('descricao-redes/', DescricaoCurso),
    path('descricao-disciplina/', DescricaoDisciplina),
    path('login/', login),
    path('matricula/', login),


]

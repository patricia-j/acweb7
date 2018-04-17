from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "index.html", contexto)


def cadastro_aluno(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cadastro_aluno.html", contexto)


def cadastro_disciplina(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cadastro_disciplina.html", contexto)


def cadastro_novo_curso(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cadastro_novo_curso.html", contexto)


def courses(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
        "cursos":[
            {"nome":"Redes de Computadores", "link":"/curso/descricao-redes/"},
            {"nome":"Análise e Desenvolvimento de Sistemas", "link":"/curso/ads"},
            {"nome":"Banco de Dados", "link":"/curso/bd"}
        ]
    }
    return render(request, "courses.html", contexto)


def cursos_analise_e_desenvolvimento(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cursos_analise_e_desenvolvimento.html", contexto)


def cursos_banco_de_dados(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cursos_banco_de_dados.html", contexto)


def cursos_redes(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "cursos_redes.html", contexto)


def DescricaoCurso(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "DescricaoCurso.html", contexto)


def DescricaoDisciplina(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "DescricaoDisciplina.html", contexto)


def login(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "login.html", contexto)


def matricula(request):
    contexto={
        "titulo":"Faculdade Impacta de Tecnologia",
    }
    return render(request, "matricula.html", contexto)
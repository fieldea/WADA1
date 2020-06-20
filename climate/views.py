from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from . import forms
from .forms import RegisterForm
from .models import  DataSource, Format, Folder, Diagram, Tag, TagDiagram, Comment, Summary, SearchResult
from django.utils import timezone
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import FormatSerializer


class FormatViewSet(viewsets.ModelViewSet):
    queryset = Format.objects.all().order_by('-id')
    serializer_class = FormatSerializer


def test(request, diagram_id):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    diagram1 = Diagram.objects.get(id=diagram_id)
    data_source1 = diagram1.DataSourceID
    format_list = Format.objects.order_by('-id')
    temp = []
    year = []
    for f in format_list:
        if (f.id >= data_source1.StartID) and (f.id <= data_source1.EndID):
            year.append(f.Year)
            temp.append(f.Temp)
    template = loader.get_template('climate/test.html')
    context = {
        'temp': temp,
        'year': year,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    memberList = User.objects.order_by('-id')
    membNum = len(memberList)
    diagramList = Diagram.objects.order_by('-id')
    diaNum = len(diagramList)
    tag_list = Tag.objects.order_by('-id')
    tagNum = len(tag_list)
    totalVisit = 0
    for d in diagramList:
        totalVisit += d.Visit
    hdiagram_list = Diagram.objects.order_by('-Visit')
    ndiagram_list = Diagram.objects.order_by('-id')
    hdiagram_list.reverse()
    ndiagram_list.reverse()
    hdata_source = hdiagram_list[0].DataSourceID
    ndata_source = ndiagram_list[0].DataSourceID
    format_list = Format.objects.order_by('-id')
    htemp = []
    hyear = []
    ntemp = []
    nyear = []
    for f in format_list:
        if (f.id >= hdata_source.StartID) and (f.id <= hdata_source.EndID):
            hyear.append(f.Year)
            htemp.append(f.Temp)
        if (f.id >= ndata_source.StartID) and (f.id <= ndata_source.EndID):
            nyear.append(f.Year)
            ntemp.append(f.Temp)
    member_list = User.objects.order_by('-id')[:5]
    template = loader.get_template('climate/index.html')
    hyear.reverse()
    htemp.reverse()
    nyear.reverse()
    ntemp.reverse()
    context = {
        'member_list': member_list,
        'hid': hdiagram_list[0].id,
        'nid': ndiagram_list[0].id,
        'htemp': htemp,
        'hyear': hyear,
        'ntemp': ntemp,
        'nyear': nyear,
        'membNum': membNum,
        'diaNum': diaNum,
        'tagNum': tagNum,
        'totalVisit': totalVisit,
        'username': request.user.username,
    }
    return HttpResponse(template.render(context, request))


def member(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    memberList = User.objects.order_by('-id')[:5]
    template = loader.get_template('climate/member.html')
    context = {
        'member_list': memberList,
    }
    return HttpResponse(template.render(context, request))


def member_detail(request, member_id):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    try:
        member1 = User.objects.get(id=member_id)
    except User.DoesNotExist:
        raise Http404("Member does not exist")
    return render(request, 'climate/member_detail.html', {'member': member1})


def tags(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    tag_list = Tag.objects.order_by('-id')[:5]
    template = loader.get_template('climate/tags.html')
    context = {
        'tag_list': tag_list,
    }
    return HttpResponse(template.render(context, request))


def data_source(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    dataSource = DataSource.objects.order_by('-id')[:5]
    template = loader.get_template('climate/data_source.html')
    context = {
        'data_source': dataSource,
    }
    return HttpResponse(template.render(context, request))


def folder(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    folder_list = Folder.objects.order_by('-id')[:5]
    template = loader.get_template('climate/folder.html')
    context = {
        'folder_list': folder_list,
    }
    return HttpResponse(template.render(context, request))


def diagram(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    diagram_list = Diagram.objects.order_by('-id')[:5]
    template = loader.get_template('climate/diagram.html')
    context = {
        'diagram_list': diagram_list,
    }
    return HttpResponse(template.render(context, request))


def diagram_detail(request, diagram_id):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    comment_list = Comment.objects.order_by('-id')
    tag_list = Tag.objects.order_by('-id')[:5]
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    format_list = Format.objects.order_by('-id')
    temp = []
    year = []
    comment1 = []
    for c in comment_list:
        comment1.append(c)
    try:
        diagram1 = Diagram.objects.get(id=diagram_id)
        data_source1 = diagram1.DataSourceID
        for f in format_list:
            if (f.id >= data_source1.StartID) and (f.id <= data_source1.EndID):
                year.append(f.Year)
                temp.append(f.Temp)
        year.reverse()
        temp.reverse()
    except Diagram.DoesNotExist:
        raise Http404("Diagram does not exist")
    return render(request, 'climate/diagram_detail.html',
                  {
                      'diagram': diagram1,
                      'tag_diagram_list': tag_diagram_list,
                      'tag_list': tag_list,
                      'temp': temp,
                      'year': year,
                      'comment1': comment1,
                  })


def tag_diagram(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    template = loader.get_template('climate/tag_diagram.html')
    context = {
        'tag_diagram_list': tag_diagram_list,
    }
    return HttpResponse(template.render(context, request))


def comment(request, diagram_id):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    commentString = request.POST.get('comment', None)
    diagram1 = Diagram.objects.get(id=diagram_id)
    td = Comment(Content=commentString, DiagramID=diagram1, PostDate=timezone.now())
    td.save();
    return redirect(reverse('diagram_detail', args=[diagram_id]))


def summary(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    summary_list = Summary.objects.order_by('-id')[:5]
    template = loader.get_template('climate/summary.html')
    context = {
        'summary_list': summary_list,
    }
    return HttpResponse(template.render(context, request))


def bind(request, diagram_id):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    tagID = request.POST.get('tagID', None)
    tag = Tag.objects.get(id=tagID)
    diagram1 = Diagram.objects.get(id=diagram_id)
    try:
        t1 = TagDiagram.objects.get(TagID=tag)
        if t1.DiagramID.id != diagram_id:
            td = TagDiagram(TagID=tag, DiagramID=diagram1)
            td.save();
    except:
        td = TagDiagram(TagID=tag, DiagramID=diagram1)
        td.save();
    return redirect(reverse('diagram_detail', args=[diagram_id]))


def login_view(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "error！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # message = username + password
                login(request, user)
                return redirect(reverse('index', args=[]))
            else:
                return render(request, 'climate/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'climate/login.html', locals())


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def register(request):
    if request.session.get('is_login', None):
        return redirect(reverse('index', args=[]))
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "error！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['confirm']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = "confirm password please！"
                return render(request, 'climate/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:
                    message = 'username exist!'
                    return render(request, 'climate/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    message = 'email in use！'
                    return render(request, 'climate/register.html', locals())

                new_user = User.objects.create_user(username, email, password1)
                new_user.save()
                return redirect(reverse('login'))
    register_form = RegisterForm()
    return render(request, 'climate/register.html', locals())
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django import forms
from .models import Member, DataSource, Format, Folder, Diagram, Tag, TagDiagram, Comment, Summary, SearchResult, User
from django.utils import timezone
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


def test(request, diagram_id):
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
    memberList = Member.objects.order_by('-Name')
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
    member_list = Member.objects.order_by('-Name')[:5]
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
    }
    return HttpResponse(template.render(context, request))


def member(request):
    memberList = Member.objects.order_by('-Name')[:5]
    template = loader.get_template('climate/member.html')
    context = {
        'member_list': memberList,
    }
    return HttpResponse(template.render(context, request))


def member_detail(request, member_id):
    try:
        member1 = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    return render(request, 'climate/member_detail.html', {'member': member1})


def tags(request):
    tag_list = Tag.objects.order_by('-id')[:5]
    template = loader.get_template('climate/tags.html')
    context = {
        'tag_list': tag_list,
    }
    return HttpResponse(template.render(context, request))


def data_source(request):
    dataSource = DataSource.objects.order_by('-id')[:5]
    template = loader.get_template('climate/data_source.html')
    context = {
        'data_source': dataSource,
    }
    return HttpResponse(template.render(context, request))


def folder(request):
    folder_list = Folder.objects.order_by('-id')[:5]
    template = loader.get_template('climate/folder.html')
    context = {
        'folder_list': folder_list,
    }
    return HttpResponse(template.render(context, request))


def diagram(request):
    diagram_list = Diagram.objects.order_by('-id')[:5]
    template = loader.get_template('climate/diagram.html')
    context = {
        'diagram_list': diagram_list,
    }
    return HttpResponse(template.render(context, request))


def diagram_detail(request, diagram_id):
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
    except Member.DoesNotExist:
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
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    template = loader.get_template('climate/tag_diagram.html')
    context = {
        'tag_diagram_list': tag_diagram_list,
    }
    return HttpResponse(template.render(context, request))


def comment(request, diagram_id):
    comment_list = Comment.objects.order_by('-id')
    tag_list = Tag.objects.order_by('-id')[:5]
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    commentString = request.POST.get('comment', None)
    diagram1 = Diagram.objects.get(id=diagram_id)
    format_list = Format.objects.order_by('-id')
    temp = []
    year = []
    comment1 = []
    td = Comment(Content=commentString, DiagramID=diagram1, PostDate=timezone.now())
    td.save();
    data_source1 = diagram1.DataSourceID
    for c in comment_list:
        comment1.append(c)
    for f in format_list:
        if (f.id >= data_source1.StartID) and (f.id <= data_source1.EndID):
            year.append(f.Year)
            temp.append(f.Temp)
    year.reverse()
    temp.reverse()
    return render(request, 'climate/diagram_detail.html',
                  {
                      'diagram': diagram1,
                      'tag_diagram_list': tag_diagram_list,
                      'tag_list': tag_list,
                      'temp': temp,
                      'year': year,
                      'comment1': comment1,
                  })


def summary(request):
    summary_list = Summary.objects.order_by('-id')[:5]
    template = loader.get_template('climate/summary.html')
    context = {
        'summary_list': summary_list,
    }
    return HttpResponse(template.render(context, request))


def bind(request, diagram_id):
    comment_list = Comment.objects.order_by('-id')
    tagID = request.POST.get('tagID', None)
    tag = Tag.objects.get(id=tagID)
    diagram1 = Diagram.objects.get(id=diagram_id)
    tag_list = Tag.objects.order_by('-id')[:5]
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    format_list = Format.objects.order_by('-id')
    temp = []
    year = []
    comment1 = []
    for c in comment_list:
        comment1.append(c)
    try:
        t1 = TagDiagram.objects.get(TagID=tag)
        if t1.DiagramID.id != diagram_id:
            td = TagDiagram(TagID=tag, DiagramID=diagram1)
            td.save();
    except:
        td = TagDiagram(TagID=tag, DiagramID=diagram1)
        td.save();
    data_source1 = diagram1.DataSourceID
    for f in format_list:
        if (f.id >= data_source1.StartID) and (f.id <= data_source1.EndID):
            year.append(f.Year)
            temp.append(f.Temp)
    year.reverse()
    temp.reverse()
    return render(request, 'climate/diagram_detail.html',
                  {
                      'diagram': diagram1,
                      'tag_diagram_list': tag_diagram_list,
                      'tag_list': tag_list,
                      'temp': temp,
                      'year': year,
                      'comment1': comment1,
                  })


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    email = forms.EmailField(label='email')


def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            User.objects.create(username=username, password=password, email=email)
            User.save()

            return HttpResponse('regist success!!!')
    else:
        userform = UserForm()
    return render(request, 'climate/login.html', {'userform': userform})


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

        user = User.objects.filter(username__exact=username, password__exact=password)

        if user:
            return render(request, 'climate/index.html', {'userform': userform})
        else:
            return HttpResponse('error')

    else:
        userform = UserForm()
    return render(request, 'climate/login.html', {'userform': userform})
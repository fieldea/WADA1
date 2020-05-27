from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Member, DataSource,Format,Folder,Diagram,Tag,TagDiagram,Comment,Summary,SearchResult

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


def test(request, diagram_id):
    diagram1 = Diagram.objects.get(id=diagram_id)
    data_source1 = diagram1.DataSourceID
    format_list = Format.objects.order_by('-id')
    temp = []
    year = []
    for f in format_list :
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
    member_list = Member.objects.order_by('-Name')[:5]
    template = loader.get_template('climate/index.html')
    context = {
        'member_list': member_list,
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
    tag_list = Tag.objects.order_by('-id')[:5]
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    format_list = Format.objects.order_by('-id')
    temp = []
    year = []
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
                  })


def tag_diagram(request):
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]
    template = loader.get_template('climate/tag_diagram.html')
    context = {
        'tag_diagram_list': tag_diagram_list,
    }
    return HttpResponse(template.render(context, request))


def comment(request):
    comment_list = Comment.objects.order_by('-id')[:5]
    template = loader.get_template('climate/comment.html')
    context = {
        'comment_list': comment_list,
    }
    return HttpResponse(template.render(context, request))


def summary(request):
    summary_list = Summary.objects.order_by('-id')[:5]
    template = loader.get_template('climate/summary.html')
    context = {
        'summary_list': summary_list,
    }
    return HttpResponse(template.render(context, request))


def bind(request, diagram_id):
    tagID = request.POST.get('tagID', None)
    tag= Tag.objects.get(id=tagID)
    diagram1 = Diagram.objects.get(id=diagram_id)
    tag_list = Tag.objects.order_by('-id')[:5]
    tag_diagram_list = TagDiagram.objects.order_by('-id')[:5]

    td = TagDiagram(TagID = tag, DiagramID = diagram1)
    td.save();
    return render(request, 'climate/diagram_detail.html',
                  {'diagram': diagram1, 'tag_diagram_list': tag_diagram_list, 'tag_list': tag_list})


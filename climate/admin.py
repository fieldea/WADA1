from django.contrib import admin

from .models import  DataSource, Format, Folder, Diagram, Tag, TagDiagram, Summary, SearchResult

# admin.site.register(Member)
admin.site.register(DataSource)
admin.site.register(Diagram)
admin.site.register(Tag)
admin.site.register(TagDiagram)
admin.site.register(Format)
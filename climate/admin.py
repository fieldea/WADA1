from django.contrib import admin

from .models import Member, DataSource, Format, Folder, Diagram, Tag, TagDiagram, Summary, SearchResult, User, UserAdmin

admin.site.register(Member)
admin.site.register(DataSource)
admin.site.register(Diagram)
admin.site.register(Tag)
admin.site.register(TagDiagram)
admin.site.register(Format)
admin.site.register(User)
admin.site.register(UserAdmin)
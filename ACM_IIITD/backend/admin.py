from django.contrib import admin
from .models import Blog, Paragraph, TeamMember, Image

class ParagraphInlineAdmin(admin.StackedInline):
    model = Paragraph
    extra = 0

class ImageInlineAdmin(admin.StackedInline):
    model = Image
    max_num = 1

class BlogAdmin(admin.ModelAdmin):
    # def content(self, obj):
    #     return obj.paragraph_set.all()[0].content[:200]

    inlines = [ParagraphInlineAdmin, ImageInlineAdmin]
    list_display = ['heading','id']

admin.site.register(TeamMember)
admin.site.register(Blog, BlogAdmin)
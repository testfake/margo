# encoding=utf8
from django.contrib import admin

from django.contrib.admin import AdminSite

from .models import Post, Tag, Tags, Comment

class TagInline(admin.TabularInline):
	model = Tags
	extra = 3

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 1

class PostAdmin(admin.ModelAdmin):
	list_display = ('post_name', 'post_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['post_name']
	fieldsets = [
		(None,   {'fields': ['post_name', 'post_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	inlines = [TagInline, CommentInline]

class TagAdmin(admin.ModelAdmin):
	#list_display = ('tag_name')
	search_fields = ['tag_name']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
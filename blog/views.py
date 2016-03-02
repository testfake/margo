from pprint import pprint
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Tag, Comment
from .forms import PostForm

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'post_list'
	paginate_by = 5
	def get_queryset(self):
		return Post.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')

class PostView(generic.DetailView):
	model = Post
	template_name = 'blog/view.html'

	def get_queryset(self):
		return Post.objects.filter(pub_date__lte=timezone.now())
	def get_context_data(self, **kwargs):
		form = PostForm()
		context = super(PostView, self).get_context_data(**kwargs)
		context['form'] = form
		return context

class TagView(generic.ListView):
	template_name = 'blog/tag.html'
	context_object_name = 'post_list'
	paginate_by = 5
	def get_queryset(self):
		self.tag = self.kwargs['tag']
		return Post.objects.filter(
			tags__tag_id = self.tag
		).order_by('-pub_date')
	def get_context_data(self, **kwargs):
		tag = Tag.objects.get(id=self.kwargs['tag'])
		context = super(TagView, self).get_context_data(**kwargs)
		context['tag'] = tag
		return context

def comment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post_id = post_id
			comment.pub_date = timezone.now()
			comment.save()

	return HttpResponseRedirect(reverse('blog:post', args=(post.id,)))
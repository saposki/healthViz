from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post
# Create your views here.


def post_create(request):
	form = PostForm(request.POST or None, request.FILES or  None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Created')
		return HttpResponseRedirect(instance.get_absolute_url())
	# else:
	# 	messages.error(request, 'Not Successfully Saved')
	# if request.method == 'POST':
	# 	print request.POST.get('content')
	context = {
		"form": form,
	}
	return render(request, 'post_form.html', context)
	# return HttpResponse("<h1>Create</h1>")

def post_detail(request, id=None): #retrieve
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, 'post_detail.html', context)

def post_list(request): #list items
	queryset_list = Post.objects.all().order_by('-timestamp')
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = 'page'

	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "Recent Post",
		'page_request_var': page_request_var
	}
	return render(request, 'post_list.html', context)




def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or  None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Successfully Updated')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, 'post_form.html', context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, 'Successfully deleted')
	return redirect('posts:list')

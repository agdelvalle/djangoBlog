from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import blogEntry, comment
from django.db.models import Count
from .forms import newEntry, newComment
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You've reached the index page!")
    template = 'index.html'
    blogs = blogEntry.objects.all().order_by('-id')
    comments_count = comment.objects.all().count()
    context = {
        'blogs': blogs,
		'comments_count': comments_count,
    }
    return render(request, template, context)

def new_entry(request):
	template = "new_entry.html"

	if request.method == "POST":
		form = newEntry(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/')
	else:
		context = {
			'new_entry': newEntry(),
		}
		return render(request, template, context)

def view_entry(request, blog_id):
    template = 'view_entry.html'
    entry = blogEntry.objects.get(id=int(blog_id))
    comments = comment.objects.filter(blog_id=int(blog_id))
    form = newComment(request.POST, initial={'blog':entry.id,})

    if request.method == "POST":
	    if form.is_valid():
		    form.save() # Now save it
	    return HttpResponseRedirect('/view_entry/' + blog_id)
    else:
	    context = {
			'newComment': newComment(initial={'blog':entry.id,}),
			'entry': entry,
			'comments': comments,
		}
	    return render(request, template, context)

def update_entry(request, blog_id):
    template = 'update_entry.html'
    entry = blogEntry.objects.get(id=int(blog_id))
    form = newEntry(request.POST, instance=entry)

    if request.method == "POST":
	    if form.is_valid():
		    form.save() # Now save it
	    return HttpResponseRedirect('/view_entry/' + blog_id)
    else:
        context = {
        'entry': entry,
		'newEntry': newEntry(instance=entry),
        }
    return render(request, template, context)

def delete_entry(request, blog_id):
	entry = blogEntry.objects.get(id=int(blog_id))
	entry.delete()
	return HttpResponseRedirect('/')

def delete_comment(request, blog_id, comment_id):
	comm = comment.objects.get(blog=int(blog_id), id=int(comment_id))
	comm.delete()
	return HttpResponseRedirect('/view_entry/' + blog_id)

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))
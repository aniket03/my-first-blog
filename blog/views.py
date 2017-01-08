from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

## This function takes a request and will return render (put together) a template
## blog/post_list.html
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts} )
	##Here a list is passed to template file

##pk is the variable we send from urls and should not be ommitted and should be kept same
def post_detail(request,pk):
	##post = Post.objects.get(pk=pk)	
	##This could have been used but if pk does not exist then it should give 404 error so we use
	##so we use django shortcut
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post} )
	##Here only a post file is passed to template

def post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		##To construct PostForm from data typed by user 
		if form.is_valid():
		##To check all fields are filled in properiety
			post=form.save(commit=False)
			##commit=0 so that data not saved to db directly
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect("post_detail",pk=post.pk)
			##"post_detail" is name of the view want to got to
	else:
		form=PostForm()
	return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form=PostForm(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			return redirect("post_detail",pk=post.pk)
	else:
		form=PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})







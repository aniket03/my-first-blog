from django.shortcuts import render

def post_list(request):
	return render(request,'blog/post_list.html',{} )
## This function tales a request and will return render (put tpgether) a template
## blog/post_list.html
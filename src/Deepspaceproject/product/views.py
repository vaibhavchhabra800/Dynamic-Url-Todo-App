from django.shortcuts import *
from django.http import *
from .models import Comment
from .forms import CommentForm
import hashlib
import requests

# Create your views here.

def fetch_view(request,slug,*args,**kwargs):

    try:
        commentobject=Comment.objects.get(title=slug)
    except Comment.DoesNotExist:
        raise Http404

    #return HttpResponse('<h1>Hello</h1>')

    context= {
        "commentobject":commentobject,

    }


    return render(request, "thenote.html",context)


def created_view2(request,slug,*args,**kwargs):

    try:
        commentobject=Comment.objects.get(id=1)
    except Comment.DoesNotExist:
        raise Http404


    url="http://localhost:8000/"+slug
    context= {
        "url": url,
        "commentobject": commentobject,

    }

    return render(request, "created2.html",context)



def new_view(request,*args,**kwargs):


    form= CommentForm(request.POST or None)
    countwa1=Comment.objects.all().count()
    countwa1+=1

    hash_object = hashlib.sha1(str(countwa1).encode())
    hex_dig = hash_object.hexdigest()
    if form.is_valid():


        newComment=Comment.objects.create(
        title = hex_dig,

        description=form.cleaned_data.get("description")

        )

        if newComment:
            return HttpResponseRedirect("/created2/"+hex_dig)


        else:
            newComment = CommentForm()

    context= {
    "sampletext": "text",
    "form": form,

}


    return render(request, "new.html",context)


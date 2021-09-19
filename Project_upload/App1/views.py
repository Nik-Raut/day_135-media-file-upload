from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhotosForm
from .models import Photos
from django.shortcuts import render,redirect

def homeview(request):
    return render(request, 'App1/base.html')

def uploadview(request):
    if request.method == 'POST':
        form = PhotosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotosForm()
    return render(request, 'App1/upload.html', {
        'form': form
    })

def photolist(request):
    photos=Photos.objects.all()
    for x in photos:
        print(x.id,x.name,x.uploaded_photo,x.uploaded_at)

    return render(request,'App1/photolist.html',{'photos':photos})





import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import nbformat
from nbconvert import HTMLExporter

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        f = request.FILES['file']
        path = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(path,'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
        return render(request,'uploaded.html',{'filename':f.name})
    return render(request,'upload.html')

def view_file(request, filename):
    path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(path, "rb") as f:
     nb = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    body, _ = html_exporter.from_notebook_node(nb)
    return HttpResponse(body)



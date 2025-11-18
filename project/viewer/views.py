
import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import TagRemovePreprocessor, Preprocessor


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

    with open(path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    from nbconvert import HTMLExporter
    from traitlets.config import Config
    
    c = Config()
    c.HTMLExporter.exclude_input = True
    c.HTMLExporter.exclude_input_prompt = True
    
    html_exporter = HTMLExporter(config=c, template_name="classic")

    body, _ = html_exporter.from_notebook_node(nb)
    

    return HttpResponse(body)

from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddTextForm
from .models import Text


# Create your views here.


def add_text(request):
    if request.method == "POST":
        form = AddTextForm(request.POST)
        form.save()
        id = Text.objects.last()
        
        return redirect("texts", id=id.id)
    form = AddTextForm
    return render(request, "text/add_text.html", {"form": form})


def show_and_edit_text(request, id):
    text = get_object_or_404(Text, pk=id)
    url = f"http://127.0.0.1:8000/texts/{id}"
    
    if request.method == "POST":
        
        if request.POST['center'] == "Edit":
        
            form = AddTextForm(request.POST)
            if form.is_valid():
                new_text = form.cleaned_data["text"]
                text.text = new_text
                text.save()
                
                #print('render after saving')
                return redirect("texts",id)
        elif request.POST['center'] == "add":
            form = AddTextForm(instance=text)
            return render(request, "text/edit_text.html", {"form": form})
   
    return render(request, "text/show_text.html", {"text": text,"text_url": url})


def edit_text(request, id):
    text = Text.objects.get(pk=id)
    
    if request.method == "POST":
        form = AddTextForm(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data["text"]
            text.text = new_text
            text.save()
            return render("texts/",id=id)
        
        
    form = AddTextForm(instance=text)
    return render(request, "text/edit_text.html", {"form": form})


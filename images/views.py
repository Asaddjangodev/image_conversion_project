from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ImageConversion
from .forms import ImageUploadForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            conversion = form.save()
            conversion.convert_image()
            return redirect('result', pk=conversion.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'converter/home.html', {'form': form})

def result(request, pk):
    conversion = ImageConversion.objects.get(pk=pk)
    return render(request, 'converter/result.html', {'converision': conversion})
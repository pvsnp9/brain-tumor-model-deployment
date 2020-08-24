from django.shortcuts import render
from django.http import HttpResponse


from django.http import JsonResponse
from .forms import ImageFileUploadForm

#here i will create views
def home(request):
    return render(request, 'mri_core/main.html')

def operation(request):
    return render(request, 'mri_core/operation.html')

def about(request):
    return render(request, 'mri_core/about.html')

def predict_show(request, image_key):
    return HttpResponse(image_key)

def upload_file(request):
    if request.method == 'POST':
       form = ImageFileUploadForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = ImageFileUploadForm()
        return render(request, 'django_image_upload_ajax.html', {'form': form})
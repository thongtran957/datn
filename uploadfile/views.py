from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    if request.method == 'POST':
        upload_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
    return render(request, 'pages/uploadfile.html')




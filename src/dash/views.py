import csv
from django.shortcuts import render
# Create your views here.

def dash_csv(request):
    file = request.FILES['fileUpload']
    if file.is_valid():
        data = [row for row in csv.reader(file.read().splitlines())]
        data_instance = file.save(commit=False)
        data_instance.save(using='dashdb')
        message.success(request, 'Successfully Uploaded')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'file': file
    }
    return render(request, 'dash_form.html', context)

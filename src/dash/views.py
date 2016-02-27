import csv
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from .forms import DashForm
from .models import Dash
from .forms import DashForm
# Create your views here.

def dash_create(request):
    form = DashForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save(using='dashdb')
        reader = csv.reader(request.FILES['file_upload'])
        data = csv.DictReader(request.FILES['file_upload'])
        print data
    context = {
        'form': form,
     }
    return render(request, 'dash_form.html', context)

    # return HttpResponse('<h1>DASH</h1>')

def dash_detail(request, id=None): #retrieve
# 	data_instance = get_object_or_404(Dash, id=id)
# 	context = {
# 		"title": data_instance.title,
# 		"data_instance": data_instance,
# 	}
# 	return render(request, 'dash_detail.html', context)
#
    return HttpResponse('<h1>Dash Detail</h1>')
def dash_list(request): #list items
# 	queryset_list = Dash.objects.all().order_by('-timestamp')
# 	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
# 	page_request_var = 'page'
#
# 	page = request.GET.get(page_request_var)
# 	try:
# 		queryset = paginator.page(page)
# 	except PageNotAnInteger:
# 	    # If page is not an integer, deliver first page.
# 		queryset = paginator.page(1)
# 	except EmptyPage:
# 	    # If page is out of range (e.g. 9999), deliver last page of results.
# 		queryset = paginator.page(paginator.num_pages)
#
# 	context = {
# 		"object_list": queryset,
# 		"title": "Recent Data",
# 		'page_request_var': page_request_var
# 	}
# 	return render(request, 'dash_list.html', context)
    return HttpResponse('<h1>Dash List</h1>')

def dash_chart(request):
    # xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    # ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    # chartdata = {'x': xdata, 'y': ydata}
    # charttype = "pieChart"
    # chartcontainer = 'piechart_container'
    data = {
        # 'charttype': charttype,
        # 'chartdata': chartdata,
        # 'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render(request, 'dash_chart.html', data)

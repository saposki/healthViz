from __future__ import unicode_literals
import csv
import httplib
import xml.etree.ElementTree as ElementTree
import json

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
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
    context = {
        'form': form,
     }
    return render(request, 'dash_form.html', context)

def dash_list(request): #list items
    context = {

    }
    return render(request, 'dash_list.html', context)

def dash_chart(request):
    queryset_array  = []
    for i in Dash.objects.all():
        queryset_array.append(ContentFile(i.file))

    raw_content_array = []
    for i in queryset_array:
        raw_content_array.append(i.read())

    # print queryset_array


    data_string_array = []
    for i in raw_content_array:
        data_string_array.append(default_storage.open(i).read())

# at this point entire xml upload is a list
# it will need to be converted to a string to use the json.loads()
# json.loads convert strings to dictonary
# with correct formatting of the string we should get desired dict.

# below we have created a string variable 'str'
# 'str' will hold the string equivalent of the xml file being read

    str_array = []
    str = ''
    for i in data_string_array:
        str += i

# here we call the json.loads method after importing json lib
# 'json.loads() converts 'str' to a valid JSON dict'

    str_dict = json.loads(str)
    print str_dict



    # xml_container = []
    # for i in data_string_array:
        # print i

    # print xml_container

    # print len(data_string_array)
    # print data_string_array
    # print len(data_string_array[0])
    # print data_string_array[0][0]
    # print data_string_array[0][1]

    # row = []
    # row = data_string_array[0][4:len(data_string_array[0])]
    # print len(row)


    # new_row = []
    # print len(new_row)

    # count = 0
    # for i in row:
    #     new_row.append(row.split("\n"))
    #     count += 1
    # print len(new_row)


    # print data_string_array[0][4]
    # row_array = []

    # for i in data_string_array:
        # row_array.append(i.split(','))

    # row_array = row_array[2:len(row_array)]
    # print len(row_array)

    queryset = Dash.objects.all()
    # queryset = queryset

    context = {
        'object_list': queryset,
        # 'file': 'List',
        'raw_file': queryset_array,
        'file_location': raw_content_array,
        'data_string': data_string_array,
        'json_dict': str_dict,
        # 'row': row_array,
    }
    # print queryset
    # {% for i in data_string %}
    #    {{i}}
    # {% endfor %}

    return render(request, 'dash_chart.html', context)

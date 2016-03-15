from __future__ import unicode_literals
from django.http import JsonResponse
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

# end point url D3
def dash_json_end_point(request):

    queryset_array  = []
    for i in Dash.objects.all():
        queryset_array.append(ContentFile(i.file))

    raw_content_array = []
    for i in queryset_array:
        raw_content_array.append(i.read())

    data_string_array = []
    for i in raw_content_array:
        data_string_array.append(default_storage.open(i).read())

    str = ''
    for i in data_string_array:
        str += i

    str_dict = json.loads(str)

    response = JsonResponse(str_dict, safe=False)
    # print type(response)

    return response


def dash_chart(request):
    queryset_array  = []
    for i in Dash.objects.all():
        queryset_array.append(ContentFile(i.file))

    raw_content_array = []
    for i in queryset_array:
        raw_content_array.append(i.read())

    data_string_array = []
    for i in raw_content_array:
        data_string_array.append(default_storage.open(i).read())

# at this point entire xml upload is a list
# it will need to be converted to a string to use the json.loads()
# json.loads convert strings to dictonary
# with correct formatting of the string we should get desired dict.
# https://docs.python.org/3/library/json.html#json.loads
# https://docs.python.org/3/library/json.html#json.load

# below we have created a string variable 'str'
# 'str' will hold the string equivalent of the xml file being read

    str_array = []
    str = ''
    for i in data_string_array:
        str += i

# here we call the json.loads method after importing json lib
# 'json.loads() converts 'str' to a valid JSON dict'

    str_dict = json.loads(str)

    response = JsonResponse(str_dict, safe=False)
    # print type(response)

    ##############################################################
    #  for addressing .csv
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
    ###########################################################

    context = {
        'raw_file': queryset_array,
        'file_location': raw_content_array,
        'data_string': data_string_array,
        'json_dict': str_dict,
        # 'row': row_array,
        'json_end_point': response,
    }

    return render(request, 'dash_chart.html', context)

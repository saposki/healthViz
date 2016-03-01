AttributeError: 'Manager' object has no attribute 'i'
>>> for i in Dash.objects.all():
...    print i
...
hello
Death Rate
>>> for i in Dash.objects.all():
...    print i.title
...
hello
Death Rate
>>> for i in Dash.objects.all():
...    print i.file
...
upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> for i in Dash.objects.all():
...    records.append(Dash.objects.i.file)
...
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: 'Manager' object has no attribute 'i'
>>> for i in Dash.objects.all():
...    records.append(i.file)
...
>>> records
[<FieldFile: upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>, <FieldFile: upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>]
>>> records[0]
<FieldFile: upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>
>>> from django.core.files.storage import default_storage
>>> from __future__ impoort unicode_literals
  File "<console>", line 1
    from __future__ impoort unicode_literals
                          ^
SyntaxError: invalid syntax
>>> from __future__ import unicode_literals
>>> import csv
>>> records
[<FieldFile: upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>, <FieldFile: upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>]
>>> for i in records:
...
...
... new_records = []
  File "<console>", line 4
    new_records = []
              ^
IndentationError: expected an indented block
>>> new_records = []
>>> for i in records:
...    new_records.push(ContentFile(records[i]))
...
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: 'list' object has no attribute 'push'
>>> for i in records:
...    new_records.append(ContentFile(records[i]))
...
Traceback (most recent call last):
  File "<console>", line 2, in <module>
NameError: name 'ContentFile' is not defined
>>> i.key
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'FieldFile' object has no attribute 'key'
>>> records
[<FieldFile: upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>, <FieldFile: upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>]
>>> records[0]
<FieldFile: upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>
>>> new_records.append(ContentFile(records[0]))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'ContentFile' is not defined
>>> fromo django.core.files.base import ContentFile
  File "<console>", line 1
    fromo django.core.files.base import ContentFile
               ^
SyntaxError: invalid syntax
>>> from django.core.files.base import ContentFile
>>> new_records.append(ContentFile(records[0]))
>>> new_records.append(ContentFile(records[1]))
>>> new_records
[<ContentFile: Raw content>, <ContentFile: Raw content>]
>>> stuff = []
>>> for i in new_records:
...    stuff.append(new_records[i].read())
...
Traceback (most recent call last):
  File "<console>", line 2, in <module>
TypeError: list indices must be integers, not ContentFile
>>> for i in new_records:
...    print i
...
Raw content
Raw content
>>> for i in new_records:
...    stuff.append(i.read())
...
>>> stuff
['upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png', 'upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv']
>>> stringer = []
>>> for i in stuff:
...    print i
...
upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> for i in stuff:
...    stringer.append(default_storage.open(i))
...
>>> string
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'string' is not defined
>>> stringer
[<File: /Users/orobosa/myBlog/media_cdn/upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>, <File: /Users/orobosa/myBlog/media_cdn/upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>]
>>> decoded = []
>>> for i in stringer:
...    print i
...
/Users/orobosa/myBlog/media_cdn/upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png
/Users/orobosa/myBlog/media_cdn/upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> for i in stringer
  File "<console>", line 1
    for i in stringer
                    ^
SyntaxError: invalid syntax
>>> for i in stringer:
...    decoded.append(csv.reader(stringer[1]))
...
>>> decoded
[<_csv.reader object at 0x110002c90>, <_csv.reader object at 0x110002c20>]
>>> for i in stringer:
...    decoded.append(default_storage.open(i).read())
...
>>> stringer
[<File: /Users/orobosa/myBlog/media_cdn/upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>, <File: /Users/orobosa/myBlog/media_cdn/upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>]
>>> stringer[0]
<File: /Users/orobosa/myBlog/media_cdn/upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png>
>>> stringer[0] = csv.reader(stringer[1])
>>> stringer
[<_csv.reader object at 0x110002d00>, <File: /Users/orobosa/myBlog/media_cdn/upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>]
>>>





>>> Dash.objects.all()
[<Dash: hello>, <Dash: Death Rate>]
>>> file_object = []
>>> for i in Dash.objects.all():
...    file_object.append(ContentFile(i.file))
...
>>> file_object
[<ContentFile: Raw content>, <ContentFile: Raw content>]
>>> file_read = []
>>> file_read.append(file_object[1].read())
>>> file_read
['upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv']
>>> default_storage.size(file_read[0])
681688
>>> file_read[0]
'upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv'
>>> data_string = default_storage.open(file_read[0]).read()
>>>

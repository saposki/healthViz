Last login: Tue Feb 23 20:37:25 on ttys000
carter:myBlog orobosa$ source bin/activat
-bash: bin/activat: No such file or directory
carter:myBlog orobosa$ source bin/activatls
-bash: bin/activatls: No such file or directory
carter:myBlog orobosa$ pwd
/Users/orobosa/myBlog
carter:myBlog orobosa$ source ../bin/activat
-bash: ../bin/activat: No such file or directory
carter:myBlog orobosa$ pwd
/Users/orobosa/myBlog
carter:myBlog orobosa$ ls
#####		components	lib		src		static_cdn
bin		include		media_cdn	static
carter:myBlog orobosa$ source bin/activate
(myBlog)carter:myBlog orobosa$ python src/manage.py shell
Python 2.7.10 (default, Aug 22 2015, 20:33:39)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Post.object.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Post' is not defined
>>> from myBlog.models import Dash
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: No module named models
>>> from .modesl import Post
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: No module named modesl
>>> from .models import Post
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: No module named models
>>>
(myBlog)carter:myBlog orobosa$ python src/manage.py shell
Python 2.7.10 (default, Aug 22 2015, 20:33:39)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from posts.models import Post
>>> from dash.models import Dash
>>> Post.objects.all()
[<Post: MUSKETEER>, <Post: Lead Musketeer>, <Post: Three Musketeer>]
>>>
>>> Dash.objects.all()
[<Dash: hello>, <Dash: Death Rate>]
>>> Dash.objects.all()
[<Dash: hello>, <Dash: Death Rate>]
>>> Post.objects.all()
[<Post: MUSKETEER>, <Post: Lead Musketeer>, <Post: Three Musketeer>]
>>> Dash.objects.all()
[<Dash: hello>, <Dash: Death Rate>]

>>> Dash.objects.all()
[<Dash: hello>, <Dash: Death Rate>]
>>> Dash.objects.filter(title='Death Rate')
[<Dash: Death Rate>]
>>> for key in Dash.objects.all():
...    print key.file
...
upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> for key in Dash.objects.filter(title='Death Rate'):
...    print key
...
Death Rate

>>> for key in Dash.objects.filter(title='Death Rate'):
...    print key
...
Death Rate
>>> for key in Dash.objects.filter(title='Death Rate'):
...    print key
...
Death Rate
>>> for key in Dash.objects.all():
...    print key
...
hello
Death Rate
>>> for key in Dash.objects.all():
...    print key.file
...
upload_location/Screen_Shot_2016-01-18_at_3.37.54_PM.png
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> for key in Dash.objects.all():
...    print key
...
hello
Death Rate
>>> for key in Dash.objects.filter(title='Death Rate'):
...    print key.file
...
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> txt = key.file
>>> print txt
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> txt = open(txt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, FieldFile found
>>> txt = open(key.file)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, FieldFile found

>>> print txt
upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv
>>> txt = open('key.file')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'key.file'
>>> import csv
>>> with open(txt, rb) as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|'
...    for row in spamreader:
  File "<console>", line 3
    for row in spamreader:
      ^
SyntaxError: invalid syntax
>>> with open(txt, rb) as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       print ', '.join(row)
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'rb' is not defined
>>> with open(txt, r) as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       print ', '.join(row)
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'r' is not defined
>>> import csv
>>> with open(txt, r) as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       print ', '.join(row)
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'r' is not defined
>>> with open(txt, 'rb') as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       print ', '.join(row)
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, FieldFile found
>>> from __future=__ import unicode_literals
  File "<console>", line 1
    from __future=__ import unicode_literals
                 ^
SyntaxError: invalid syntax
>>> from __future__ import unicode_literals
>>> txt =  Content(txt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Content' is not defined
>>> txt =  ContentFiule(txt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'ContentFiule' is not defined
>>> txt =  ContentFile(txt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'ContentFile' is not defined
>>> from django.core.files.base import ContentFile
>>> txt =  ContentFile(txt)
>>> print txt
Raw content
>>> Post.objects.all()
[<Post: MUSKETEER>, <Post: Lead Musketeer>, <Post: Three Musketeer>]
>>> Dash.objects.all()
[<Dash: hello>, <Dash: Death Rate>]
>>> txt.raw
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'raw'
>>> txt.Raw
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'Raw'
>>> txt.raw.read()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'raw'
>>> txt.read()
'upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv'
>>> txt.read(2)
''
>>> txt.read(3)
''
>>> txt.read(10)
''
>>> txt.read()
''
>>> txt.read()
''
>>> txt.read()
''
>>> txt.raw()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'raw'
>>> txt.raw()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'raw'
>>> txt
<ContentFile: Raw content>
>>> txt.ContentFile
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'ContentFile'
>>> txt.raw()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ContentFile' object has no attribute 'raw'
>>> txt
<ContentFile: Raw content>
>>> txt.read()
''
>>> print txt.read()

>>> with open(txt, 'rb') as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       print ', '.join(row)
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, ContentFile found
>>> txt
<ContentFile: Raw content>
>>> with open(txt, 'rb') as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       bxt =  ContentFile(txt)
...       print bxt
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, ContentFile found
>>>       print bxt
  File "<console>", line 1
    print bxt
    ^
IndentationError: unexpected indent
>>> with open(txt, 'rb') as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    for row in spamreader:
...       bxt =  ContentFile(txt)
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, ContentFile found
>>> with open(txt, 'rb') as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
... print spamreader
  File "<console>", line 3
    print spamreader
        ^
SyntaxError: invalid syntax
>>> print spamreader
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'spamreader' is not defined
>>> with open(txt, 'rb') as csvfile:
...    spamreader = csv.reader(csvfile, delimeter= ' ', quotechar='|')
...    print spamreader
...
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: coercing to Unicode: need string or buffer, ContentFile found
>>> txt
<ContentFile: Raw content>
>>> key
<Dash: Death Rate>
>>> key.file
<FieldFile: upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>
>>> txt = key.file
>>> txt
<FieldFile: upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>
>>> txt = ContentFile(key.file)
>>> txt
<ContentFile: Raw content>
>>> ContentFile.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'ContentFile' has no attribute 'objects'
>>> default_storage.size(txt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'default_storage' is not defined
>>> txt.size()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'int' object is not callable
>>> txt.size(xt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'xt' is not defined
>>> txt.size(txt)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'int' object is not callable
>>> key
<Dash: Death Rate>
>>> key.file
<FieldFile: upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv>
>>> txt
<ContentFile: Raw content>
>>> txt.read()
'upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv'
>>> stuff = txt.read()
>>> stuff
''
>>> txt.read()
''
>>> txt = ContentFile(key.file)
>>> txt
<ContentFile: Raw content>
>>> stuff = txt.read()
>>> stuff
'upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv'
>>> txt.read()
''
>>> stuff
'upload_location/af34ad54-8cc0-4207-be44-a4958c5a1e36_v2.csv'
>>> from django.core.files.storage import default_storage
>>> default_storage.size(stuff)
681688
>>>



>>> default_storage.open(stuff).read()  
>>> data_string = default_storage.open(stuff).read()
>>> data_set_unicode_decode = csv.reader(data_string)


>>> data_set_list = []
>>> data_set_unicode_decode = csv.reader(data_string)
>>> for row in data_set_unicode_decode:
...    data_set_list.append(row)

from django.shortcuts import render

from django import forms
from django.http import HttpResponse
from django.core.urlresolvers import reverse


from django.views.generic.base import View

from .forms import codeUploadForm

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

import csv
import os

from .models import Lsflat
from django.db import connection


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = codeUploadForm()
        context = {'form':form}
        return render(request, 'import.html',
                  context)


    def post(self, request, *args, **kwargs):
        form = codeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['Uploadedfile']
        
            fout = open("uploads/%s" % uploaded_file.name, 'wb')
            for chunk in uploaded_file.chunks():
                fout.write(chunk)
            fout.close()

            fcsv = open("uploads/%s" % uploaded_file.name, 'rt')
            #csv_data = csv.reader(fcsv)  
                      
            csv_data = csv.DictReader(fcsv,delimiter=";")  
            cursor = connection.cursor()
            cursor.execute("TRUNCATE `articles`.`csvtest_lsflat`;")
 

            lst = [row['CONTRNUM'] for row in csv_data]
            #for row in csv_data:
            #    s = row['CONTRNUM']
            lss = [lst[i:i+10000:] for i in range(0, len(lst), 10000)]
            for i in lss:
                aList = [Lsflat(ls=val) for val in i]
                Lsflat.objects.bulk_create(aList)

#csvcount = sum( int('1') for row in csv_data)


           # s=""
           # for row in csv_data:
           #     s += ', '.join(row) + "</br>"


            fcsv.close()
            os.remove("uploads/%s" % uploaded_file.name);
# + str(csvcount)
            return HttpResponse("Upload OK!" +"</br>"+str(Lsflat.objects.count()))
        else:
            # Do something in case if form is not valid
            raise Http404 
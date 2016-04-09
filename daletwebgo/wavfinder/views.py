from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from stat import S_ISREG, ST_MTIME, ST_MODE
import os, sys, time, re
from django_rq import job
import django_rq
from rq import get_current_job
from .models import LongTask


class Search(object):
    query=""
    results=0

def wavsearch(request, search="", addqueue="", enqueue="" ):
#    return HttpResponse("Hello, world. You're at the wavfinder index.")
    dirpath="/home/henning/env/inputfiles"  # insert the path to your directory, FIXME: Please make static variable of some sort for this
    entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
    # get all entries in the directory w/ stats
    entries = ((os.stat(path), path) for path in entries)
    # leave only regular files, insert creation date
    entries = ((stat[ST_MTIME], path) for stat, path in entries if S_ISREG(stat[ST_MODE]))
    searchobject=Search()
    searchobject.query=search
    #if request.POST.get('search', ""):
    #   searchobject.query = request.POST.get('search', "")
    filelist=[]
    count=0
    for time, path in sorted(entries, reverse=True):
        if searchobject.query:
            if re.search(searchobject.query, os.path.basename(path), re.IGNORECASE):
                filelist.append(os.path.basename(path))
                searchobject.results += 1
        else:
            filelist.append(os.path.basename(path))
        count+=1
        if not searchobject.query and count == 10:
            break
    if (addqueue != ""):
        task = LongTask.objects.create(
            name=addqueue,
            result='QUEUED'
        )   
        django_rq.enqueue(longrun, task)
    return render(request, 'wavfinder/wavsearch.html', {'filelist': filelist, 'search': searchobject, 'addqueue': addqueue, 'enqueue': enqueue })

def wavsearchredir(request, search=""):
    if request.POST.get('search', ""):
       search = request.POST.get('search', "")
    #in case someone searches with no value just send them back to front page
    if search == "":
        return HttpResponseRedirect( "/wavfinder/")
    return HttpResponseRedirect( "/wavfinder/search/"+search+"/")


def jobstatus(request, status="progress"):
    return render(request, 'wavfinder/jobstatus.html', {'status': status})

@job('default')
def longrun(task):
  job = get_current_job()
  task.result = 'FASE 1 av 6 - Sjekker'

  #duration_in_second_persentages = task.duration*1.0 / 100
  duration_in_second_persentages = 10*1.0 / 100
  for i in range(100):
      task.progress = i
      task.save()
      print(task.progress)
      time.sleep(duration_in_second_persentages)

  task.result = 'FERDIG'
  task.save()
  return task.result

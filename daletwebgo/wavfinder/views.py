from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from stat import S_ISREG, ST_MTIME, ST_MODE
import os, sys, time

def wavsearch(request):
#    return HttpResponse("Hello, world. You're at the wavfinder index.")
    dirpath="/home/henning/env/inputfiles"  # insert the path to your directory, FIXME: Please make static variable of some sort for this
    entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
    # get all entries in the directory w/ stats
    entries = ((os.stat(path), path) for path in entries)
    # leave only regular files, insert creation date
    entries = ((stat[ST_MTIME], path) for stat, path in entries if S_ISREG(stat[ST_MODE]))
    filelist=[]
    count=0
    for time, path in sorted(entries, reverse=True):
        filelist.append(os.path.basename(path))
        count+=1
        if count == 10:
            break
    return render(request, 'wavfinder/wavsearch.html', {'filelist': filelist})


def jobstatus(request, status="progress"):
    return render(request, 'wavfinder/jobstatus.html', {'status': status})




#NOTE: on Windows `ST_CTIME` is a creation date 
#  but on Unix it could be something else
#NOTE: use `ST_MTIME` to sort by a modification date


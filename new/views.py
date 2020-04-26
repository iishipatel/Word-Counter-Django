from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    d={}
    for word in wordlist:
        if word in d:
            d[word]+=1
        else:
            d[word]=1

        sortedWords=sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext': fulltext, 'count':len(wordlist), 'dict':sortedWords})

def about(request):
    return render(request, 'about.html')



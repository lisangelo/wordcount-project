from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request) :
    return render(request, 'home.html', {'number': 'first'})

def about(request) :
    return render(request, 'about.html')

def count(request) :
    fulltext = request.GET['fulltext']

    word_list = fulltext.split()

    words = {}
    for word in word_list :
        if word in words :
            words[word] += 1
        else :
            words[word] = 1
    words_sorted = sorted(words.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fulltext': fulltext, 'word_count': len(word_list), 'words': words_sorted})

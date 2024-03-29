from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:  
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'result.html',{'full': text, 'exclude_blank' : len(words), 'include_blank' : len(words)*2-1, 'dictionary' : word_dictionary.items()})
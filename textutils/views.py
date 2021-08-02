# I have created this file - Herik.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("""<h1>Hello</h1> <a href ="https://www.codewithharry.com/">Django code with harry</a>""")

    # params = {'name':"xyz",'place':'Mars'}
    # return render(request, 'index.html',params) 
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About me")


def analyze(request):
    # print(request.GET.get('text', 'default'))

    djtext = request.POST.get('text', 'default')
    removepun = request.POST.get('removepunc', 'off')
    capital = request.POST.get('uppercase', 'off')
    newlinerem = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.GET.get('spaceremove', 'off')

    # check which checkbox is on
    if removepun == "on":
        punctu = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if (char not in punctu):
                analyzed = analyzed + char

        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (capital == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'capitalized', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlinerem == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'new line removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extra space removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")


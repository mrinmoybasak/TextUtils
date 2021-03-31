# I have creatyed my file - Mrinmoy
from  django.http import HttpResponse
from django.shortcuts import render
#
# def index(request):
#     return HttpResponse('''<h1>Mrinmoy's MB Welath Youtube Channel</h1>
#     <a href="https://www.youtube.com/channel/UCWBq1E7ssnon-4T6P5cXCPQ"> M B Welath<a/> ''')
#
# def about(request):
#     return HttpResponse("About Mrinmoy")

def index(request):

    return render(request,'index.html')
    # return HttpResponse("Home")

def removepunc(request):
    djtext=request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params )
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

def capfirst(request):
    return HttpResponse('capitalize first')

def newlineremove(request):
    return HttpResponse('new line remove')

def spaceremove(request):
    return HttpResponse(" space remove <a href='/'>Back</a>")

def charcount(request):
    return HttpResponse('charcountt')



from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'Default')
    removepunc = request.POST.get('removepunc', 'off')
    capital = request.POST.get('captalize', 'off')
    newline = request.POST.get('nlr', 'off')
    spacer = request.POST.get('rs', 'off')
    character = request.POST.get('cc', 'off')
    duplicate = djtext

    punctu = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == 'on':
        tempstr = ""
        purp = "Removed Punctuations"
        for char in djtext:
            if char not in punctu:
                tempstr += char
        params = {'purpose': purp, 'analyzed_text': tempstr}
        duplicate = tempstr
    if capital == "on":
        duplicate = duplicate.upper()
        purp = "Changed to UpperCase"
        params = {'purpose': purp, 'analyzed_text': duplicate}

    if newline == "on":
        tempstr = ""
        purp = "New Line Removed"
        for char in duplicate:
            if char != "\n" and char != "\r":
                tempstr = tempstr + char
        params = {'purpose': purp, 'analyzed_text': tempstr}
        duplicate = tempstr
    if character == "on":
        purp = "Character Counted"
        analyzed = len(duplicate)
        params = {'purpose': purp, 'analyzed_text': analyzed}

    if spacer == "on":
        tempstr = ""
        purp = "extra Space Removed"
        for index, char in enumerate(duplicate):
            if not (duplicate[index] == " " and duplicate[index + 1] == " "):
                tempstr = tempstr + char
        params = {'purpose': purp, 'analyzed_text': tempstr}

    if removepunc == "on" or spacer == "on" or character == "on" or newline == "on" or capital == "on":
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error bruh!!")

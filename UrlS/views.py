from django.shortcuts import render
import pyshorteners
from django.contrib import messages

def home(request):
    try:
        short_url = ''
        url = ''
        if request.method == 'POST':
            shortener = pyshorteners.Shortener()
            url = request.POST.get('url')
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Generated")
        return render(request, 'index.html', {"short_url": short_url, "url" : url})
    except:
        return render(request, 'index.html')

# Create your views here.

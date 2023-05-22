from django.shortcuts import render
import requests
import os

Api_key=os.environ.get('news_api_key')

def home(request):
    country=request.GET.get('country')
    if country:
        url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={Api_key}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    catagory=request.GET.get('catagory')
    if catagory:
        url=f'https://newsapi.org/v2/top-headlines?category={catagory}&apiKey={Api_key}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
    context={'articles':articles}
    return render(request, 'news.html', context)


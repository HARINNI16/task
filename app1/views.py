from django.shortcuts import render
import requests
def base(request):
    response=requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render(request, 'base.html',{'response':response})

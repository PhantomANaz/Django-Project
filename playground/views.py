from django.shortcuts import render
#from django.http import HttpResponse
from .models import SQLStockMarketTaskData

# Create your views here.
# Takes a request and return response
# request -> response
# request handler
# In some framework it's called an Action. In django, it's called View. But it's not like something that user sees.

# def say_hello(request):
#     # Pull data from db
#     # Transform data
#     # Send Email
#     # For now, let's return a simple response
#     return render(request, 'hello.html', {'name': 'Ayesha'})
def home(request):
    data = SQLStockMarketTaskData.objects.all()
    return render(request, 'home.html', {'data': data})
from django.shortcuts import render, HttpResponse
from .models import Area_data
def home(request):
    return render(request, 'price_prediction.html')

def price_predictions(request):
    if(request.method == 'POST'):
        area = request.POST['area']
    Area_data(area = area).save()
    return render(request, 'price_prediction.html')
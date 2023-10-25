from django.shortcuts import render, HttpResponse

def price_predictions(request):
    return render(request, 'price_predictions.html')
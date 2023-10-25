from django.shortcuts import render, HttpResponse
from joblib import load
import locale


model = load('./savedModels/models.joblib')
locale.setlocale(locale.LC_MONETARY, 'en_IN')
'en_IN'
from .models import Area_data
def home(request):
    return render(request, 'price_prediction.html')

def price_predictions(request):
    if(request.method == 'POST'):
        area = request.POST['area']
    Area_data(area = area).save()
    print("Area == ",area)
    predicted_price = model.predict([[int(area)]])
    print("Predicted Price =",predicted_price)
    price = locale.currency(int(predicted_price), grouping=True) 
    print("Price =",price)
    return render(request, 'price_prediction.html',{'price': price})
import requests
from django.shortcuts import render

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        url = f"https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/pair/{from_currency}/{to_currency}/{amount}"

        response = requests.get(url)
        result = int(response.json()['conversion_result'])
        currency_time = response.json()['time_last_update_utc']
    else:
        result = None
        amount = request.GET.get('amount')
        from_currency = request.GET.get('from_currency')
        to_currency = request.GET.get('to_currency')
        currency_time = None

    return render(request, 'index.html', {'result': result, 'amount': amount, 'from_currency': from_currency, 'to_currency': to_currency, 'currency': currency_time})
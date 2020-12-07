from django.shortcuts import render

def home(request):
    import requests
    import json

    # pk_80c91974cc9f4db58f64b11769d7ef03
    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_80c91974cc9f4db58f64b11769d7ef03')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error ..."




    return  render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
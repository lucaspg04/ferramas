from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    return render(request, 'base.html')


def productos(request):
    
    if request:
        api_url = 'https://96694140-a72c-4bdb-929f-a1afeb67cc29-00-vz52l71pjvcq.picard.replit.dev/api/productos/'
        
        response = requests.get(api_url)

        if response.status_code == 200:
            datos = response.json()
            return render(request, 'tienda/productos.html', {'datos': datos})
        else:
            print(response.content)
    
    return render(request, 'tienda/productos.html')
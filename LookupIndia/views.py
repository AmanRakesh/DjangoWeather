from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    import cv2
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+ zipcode +",in&units=metric&appid=5d4bb43eacd5f2f05918921bf43a0535")
        try:
            api = json.loads(api_request.content)
                
        except Exception as e:
            api = 'Error...'
        
        try:
            name = api['name']
            main_status = api['weather'][0]['main']
            description = api['weather'][0]['description']
            temp = api['main']['temp']
            pressure = api['main']['pressure']
            temp_min = api['main']['temp_min']
            temp_max = api['main']['temp_max']
            wind = api['wind']['speed']
            
            return render(request, 'home.html', {'api':api,
                                             'name':name,
                                             'main_status':main_status,
                                             'description':description,
                                             'temp':temp,
                                             'pressure':pressure,
                                             'temp_max':temp_max,
                                             'temp_min':temp_min,
                                             'wind':wind,
                                             'zipcode':zipcode,
                                             
                                                })
        except Exception as e:
            api = 'Error...'
            return render(request, 'home.html', {'api':api,
                                                })
        
        
    else:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=603203,in&units=metric&appid=5d4bb43eacd5f2f05918921bf43a0535")
        try:
            api = json.loads(api_request.content)
                
        except Exception as e:
            api = 'Error...'
        
        zipcode = '603203'    
        name = api['name']
        main_status = api['weather'][0]['main']
        description = api['weather'][0]['description']
        temp = api['main']['temp']
        pressure = api['main']['pressure']
        temp_min = api['main']['temp_min']
        temp_max = api['main']['temp_max']
        #ground_level = api['main']['grnd_level']
        wind = api['wind']['speed']
        
        return render(request, 'home.html', {'api':api,
                                             'name':name,
                                             'main_status':main_status,
                                             'description':description,
                                             'temp':temp,
                                             'pressure':pressure,
                                             'temp_max':temp_max,
                                             'temp_min':temp_min,
                                             'wind':wind,
                                             'zipcode':zipcode,
                                                })
    

def about(request):
    return render(request, 'about.html', {})

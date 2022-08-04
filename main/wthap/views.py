from django.shortcuts import render
import urllib.request as ur
import json

def HomeView(request):
    context = {}
    if request.method == "POST":    
        city = request.POST['city']
        if city == "":
            context = {
            "city" : " - " ,
            "code" : " - " ,
            "temp" : " - ",
            "pressure" : " - ",
        }
        else:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=xxxxxxxxxxxxxxxxxxxxxxx"
            req = ur.urlopen(url).read()
            data = json.loads(req)
            context['city'] = city
            context['code'] = str(data['cod']) 
            context["temp"] = str(round(data['list'][0]['main']["temp"] - 273.15, 1)) + " Celsius"
            context["pressure"] = str(data['list'][0]['main']['pressure'])
            context['tempmin'] =  str(round(data['list'][0]['main']["temp_min"] - 273.15, 1)) + " Celsius"
            context['tempmax'] = str(round(data['list'][0]['main']["temp_max"] - 273.15, 1)) + " Celsius"
            context['wind'] = str(data['list'][0]['wind']['speed'])
            context['weather'] = str(data['list'][0]['weather'][0]['main'])
            context['description'] = str(data['list'][0]['weather'][0]['description'])
            context['stats'] = str(data['list'][1])
    else:
        city = ""
        context = {}
    return render(request, 'index.html', context)

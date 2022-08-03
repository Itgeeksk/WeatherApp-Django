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
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=21c2fba050f4b6c020c53a04db856bb9"
            req = ur.urlopen(url).read()
            data = json.loads(req)
            context['city'] = city
            context['code'] = str(data['cod']) 
            context["temp"] = str(round(data['list'][2]['main']["temp"] - 273.15, 2)) + " Celsius"
            context["pressure"] = str(data['list'][2]['main']['pressure'])
    else:
        city = ""
        context = {
            "city" : " - " ,
            "code" : " - " ,
            "temp" : " - ",
            "pressure" : " - ",
        }
    return render(request, 'index.html', context)

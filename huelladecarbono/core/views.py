from django.views.generic.base import TemplateView
from django.shortcuts import render
from geolocalizacion.models import Address, Destination


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination = Destination.objects.all()
        #print("Los destinos son: ", destination.name)
        qs=[]
        suma=0
        i=0
        for item in destination:
            #print(item.name)
            #print(item.addr)
            matches = Address.objects.filter(destination_id=item.id)
            for c in matches:
                if c.footprint:
                    suma = suma+c.footprint
                    i+=1
                    if i==len(matches):
                        print("La suma final ", suma)
                        qs.append(suma)
                        suma=0
                        i=0

                #print(c.footprint)
            #print("Los matches son ", matches)
            #print("Las huellas son ", matches.footprint)
            #for match in matches:
                #print("match: ", match)
                # suma=suma+match.footprint
                # i=+1
                # if i==len(matches):
                #     print("La suma es: ",suma)
                #     qs.append(suma)
                #print("Hola mundo")
        print(qs)
        context["qs"] = qs
        context["destination"] = Destination.objects.all()
        return context
    


class SamplePageView(TemplateView):
    template_name = "core/sample.html"


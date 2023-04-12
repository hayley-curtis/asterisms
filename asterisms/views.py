from django.shortcuts import render, get_object_or_404
from .models import Culture, Asterism, Stars

#you have to import every django function from somewhere 

#def index(request): 
  # constellation_list = Constellation.objects.order_by('-pub_date')[:5] 
   #context = {'constellation_list': constellation_list}
  # return render(request, 'asterisms/index.html', context)



#def info(request, constellation_id):
  # c = Constellation.objects.get(pk=constellation_id)
  # star_list = c.star_set.all
   #context = {'star_list': star_list, 'c': c.constellation_name}
  # return render(request, 'asterisms/info.html', context)

def about(request): 
   return render(request, 'asterisms/about.html')

def index(request):
   culture_list = Culture.objects.order_by('culture_name')
   context = { 'culture_list' : culture_list}
   return render(request, 'asterisms/index.html', context)


def culture_detail(request, culture):
   c = Culture.objects.get(culture_name = culture)
   asterism = Asterism.objects.filter(culture_id = c.id)
   asterism_list = asterism.order_by('-asterism_name')
   context = { 'asterism_list': asterism_list, 
              'c': c,
              }
   return render(request, 'asterisms/culture.html', context)
   

def asterism_detail(request, culture, asterism):
   a = Asterism.objects.get(asterism_name = asterism)
   stars = Stars.objects.filter(asterisms = a.id)    #how do I deal with this as many-to-many relationship?
   stars_list = stars.order_by('-star_hip')
   context = {'stars_list': stars_list, 
              'a': a,
             }
   return render(request, 'asterisms/asterism.html', context)
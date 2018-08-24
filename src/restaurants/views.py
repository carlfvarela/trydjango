from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)



class RestaurantListView(ListView):
	queryset = RestaurantLocation.objects.all()
	template_name = 'restaurants/restaurants_list.html'
class SearchRestaurantListView(ListView):
	
	template_name = 'restaurants/restaurants_list.html'
	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(Q(category_iexact=slug) | Q(category_icontains=slug))
		else:
			queryset = RestaurantLocation.objects.none()
		return queryset 


from django.shortcuts import render
from seasonal.models import Produce, Location
from .forms import AllForm
from django.http import HttpResponseRedirect, HttpResponse
from .functions import local_zipcodes, grow_zone_stripper, grow_zone_matcher


def home_view(request):
    if request.method == 'GET':
        form = AllForm(request.GET)
        if form.is_valid():
            zipcode = form.cleaned_data['zipcode']
            distance = form.cleaned_data['distance']
            produce = form.cleaned_data['produce']
            location_model = Location.objects.get(zipcode=zipcode)
            grow_zone = grow_zone_stripper(location_model.grow_zone)
            zips_in_radius = local_zipcodes(zipcode, int(distance))
            city, state = str(location_model).split(',')
            city = city.capitalize()
            starting_location = city.capitalize() + ' ' + state
            proddy = grow_zone_matcher(grow_zone)
            if produce == "":
                """ if produce list is blank will redirect to
                    show grow zone and produce in same zone """
                context = {'zipcode': zipcode,
                           'distance': distance,
                           'zips_in_radius': zips_in_radius,
                           'starting_location': starting_location,
                           'grow_zone': grow_zone,
                           'location_model': location_model,
                           'proddy': proddy,
                           'city': city,
                           'state': state}
                return render(request, 'local_grow.html', context)
            else:
                context = {'zipcode': zipcode,
                           'distance': distance,
                           'produce': produce,
                           'zips_in_radius': zips_in_radius,
                           'starting_location': starting_location}
            return render(request, 'local_harvest.html', context)
    form = AllForm()
    return render(request, 'home.html', {'form': form})


def browse_view(request):
    produce = Produce.objects.order_by('-name')
    context = {'produce': produce}
    return render(request, 'browse.html', context)


def search_view(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        else:
            produce = Produce.objects.filter(name__icontains=q)
            if produce:
                context = {'produce': produce, 'query': q}
                return render(request, 'search_results.html', context)
            else:
                errors.append('No search results found for: {}'.format(q))
    return render(request, 'search.html', {'errors': errors})

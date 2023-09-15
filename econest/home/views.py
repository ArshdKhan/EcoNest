from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")

def search(request):
    return render(request, "search.html")

def maps(request):
    return render(request, "maps.html")

def maps(request, map_id):
    try:
        neighbourhood_info = Neighbourhood_Info.objects.get(neighbourhood=map_id)
        # Neighborhood exists in the database, so return the rent information
        return render(request, "rent_info.html", {'neighbourhood_info': neighbourhood_info})
    except Neighbourhood_Info.DoesNotExist:
        # Neighborhood doesn't exist in the database, so run the scraper function
        scraped_data = get_avg_rent(city="Bangalore", bhk="2", locality=map_id)

        if scraped_data is not None:
            # Create a new NeighbourhoodInfo object and save it to the database
            neighbourhood_info = Neighbourhood_Info.objects.create(neighbourhood=map_id, average_rent=scraped_data)
            neighbourhood_info.save()
            return render(request, "rent_info.html", {'neighbourhood_info': neighbourhood_info})
        else:
            # Handle the case where scraping failed
            return HttpResponse("Scraping failed for this neighborhood")



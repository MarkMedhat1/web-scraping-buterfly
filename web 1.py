headers = {'User-Agent': 'Chrome/55.0 ',}
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.booking.com/searchresults.html?ss=Cairo&ssne=Cairo&ssne_untouched=Cairo&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaEOIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AreSo68GwAIB0gIkZWYxMzdhNTEtZDA5YS00YTJkLWI1ODctOGRkYjJmNmM2MTk22AIF4AIB&sid=2712e21d7b8eaa4091d8d752e443d91d&aid=304142&lang=en-us&sb=1&src_elem=sb&src=city&dest_id=-290692&dest_type=city&checkin=2024-03-13&checkout=2024-04-28&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure '

response  = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
hotels = soup.findAll('div', {'data-testid': 'property-card'})
hotels_data = []
for hotel in hotels:
    name_element = hotel.find('div', {'data-testid': 'title'})
    name = name_element.text.strip()
    location_element = hotel.find('span', {'data-testid': 'address'})
    location = location_element.text.strip()

    hotels_data.append({
        'name': name,
        'location': location,
    })

hotels = pd.DataFrame(hotels_data)
print(hotels)
try :
    hotels.to_csv('hotels.csv', header=True, index=False)
except  :
    print("errro")


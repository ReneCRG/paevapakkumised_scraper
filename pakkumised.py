import requests
from bs4 import BeautifulSoup
import json
import sys

url = "https://päevapakkumised.ee/tartu"

response = requests.get(url)

no_asian = "--no-asian" in sys.argv

with open("places.json", "r", encoding="utf-8") as f:
    places = json.load(f)

with open("asian.json", "r", encoding="utf-8") as f:
    asian_options = json.load(f)


if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    result = {}
    offers = soup.select("#offers")
    for meal in offers[0].select(".meal"):
        h3 = meal.find("h3")
        if not h3:
            continue
        result[h3.text.strip()] = [
            offer.text.split("\n")[0] for offer in meal.select(".offer")
        ]

    print()
    for place in places:
        if no_asian and place in asian_options:
            continue
        offers_list = result.get(place, [])
        if len(offers_list) == 0:
            continue
        print(place)
        for offer in offers_list:
            print(offer)
        print()
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

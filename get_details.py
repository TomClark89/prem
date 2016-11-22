import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import urllib.request

import csv

def download_details(url):
    result = requests.get(url)

    if result.status_code != 200:
        return None

    content = result.content

    soup = BeautifulSoup(content, "html.parser")

    page_results = soup.find_all(class_="search-page__result")
    #j = 0
    for page_result in page_results:
        #j = j + 1
        search_result_content = page_result.find(class_="search-result standard ").find(class_="search-result__r1").find(class_="search-result__content ")

        car_id = page_result.get("id")

        for li in search_result_content.find(class_="search-result__attributes").findAll("li"):
            if "miles" in li.text:
                mileage = li.text.replace(',', '').replace('miles', '').strip()


        for li in search_result_content.find(class_="search-result__attributes").findAll("li"):
            if "reg" in li.text:
                age = li.text.strip()[:4]

        price = search_result_content.find(class_="search-result__titles").find(class_="search-result__price").text.strip().ljust(6)[1:].replace(',', '')
        car_info = [car_id, age, price, mileage]# img_page = image_cell.a['href']
        print(car_info)
        with open('cars.csv', 'a', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(car_info)

        # img_location = image_cell.img['src']
        # med_location = img_location.upper().find("/MED/")
        # img_location = img_location[:med_location] + "/LRG/" + img_location[med_location+5:]
        # o = urlparse(img_location)
        # file_name = os.path.basename(o.path)
        # print (str(j).rjust(2) + ": " + file_name)
        # urllib.request.urlretrieve(img_location,"downloaded_images/" + file_name)
#original URL had a limit on age
#url_front = "http://www.autotrader.co.uk/car-search?sort=distance&radius=1500&postcode=bs84ye&onesearchad=Used&make=MINI&model=HATCH&year-from=2003&maximum-mileage=125000&body-type=Hatchback&fuel-type=Petrol&maximum-badge-engine-size=1.6&transmission=Manual&quantity-of-doors=3&seller-type=private&keywords=cooper&page="
url_front = "http://www.autotrader.co.uk/car-search?sort=distance&radius=1500&postcode=bs84ye&onesearchad=Used&make=MINI&model=HATCH&maximum-mileage=125000&body-type=Hatchback&fuel-type=Petrol&maximum-badge-engine-size=1.6&transmission=Manual&quantity-of-doors=3&seller-type=private&keywords=cooper&page="
row_headers = ['ID','Age','Price','Miles']

with open('cars.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(row_headers)
print (row_headers)

for i in range(1, 41):
    url = url_front + str(i)
    #print(url)
    #print ("Page " + str(i))
    download_details(url)

import time
import re
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import urllib.request

import csv

def download_details(url,i):
    result = requests.get(url + str(i))

    if result.status_code != 200:
        return None

    content = result.content

    soup = BeautifulSoup(content, "html.parser")
    home_name = soup.find(class_="teamsContainer").find(class_="home").find(class_="teamName").find(class_="long").text
    away_name = soup.find(class_="teamsContainer").find(class_="away").find(class_="teamName").find(class_="long").text
    home_div = soup.find(class_="matchEventsContainer").find(class_="home")
    away_div = soup.find(class_="matchEventsContainer").find(class_="away")
    home_events = home_div.find_all(class_="event")
    away_events = away_div.find_all(class_="event")
    for event in home_events:
        trimmed_event = event.text.strip()
        event_len = len(trimmed_event)
        #print(trimmed_event)

        player = re.search(r"[\w|\s]+\d", trimmed_event, flags=re.IGNORECASE).group().rstrip('1234567890 ')
        goal_times = re.findall(r"\s+\d+", trimmed_event, flags=re.IGNORECASE)
        for goal_time in goal_times:
            #print (player, goal_time)
            line_info = [i, home_name, away_name, player, home_name, goal_time]
            print(line_info)
            with open('results.csv', 'a', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(line_info)

    for event in away_events:
        trimmed_event = event.text.strip()
        event_len = len(trimmed_event)
        #print(trimmed_event)

        player = re.search(r"[\w|\s]+\d", trimmed_event, flags=re.IGNORECASE).group().rstrip('1234567890 ')
        goal_times = re.findall(r"\s+\d+", trimmed_event, flags=re.IGNORECASE)
        for goal_time in goal_times:
            #print (player, goal_time)
            line_info = [i, home_name, away_name, player, away_name, int(goal_time.strip())]
            print(line_info)
            with open('results.csv', 'a', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(line_info)
        # img_location = image_cell.img['src']
        # med_location = img_location.upper().find("/MED/")
        # img_location = img_location[:med_location] + "/LRG/" + img_location[med_location+5:]
        # o = urlparse(img_location)
        # file_name = os.path.basename(o.path)
        # print (str(j).rjust(2) + ": " + file_name)
        # urllib.request.urlretrieve(img_location,"downloaded_images/" + file_name)
#original URL had a limit on age
start_time = time.time()

row_headers = ['MatchID','HomeTeam','AwayTeam','Scorer', 'ScoredFor','Time']

with open('results.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(row_headers)
print (row_headers)

for i in range(1, 101):
    url = 'https://www.premierleague.com/match/'
    #print ("Page " + str(i))
    download_details(url,i)

end_time = time.time()

elapsed_seconds = int(end_time-start_time)
elapsed_mins = int(elapsed_seconds/60)

print ("total mins: " + str(elapsed_mins))
print ("total seconds: " + str(elapsed_seconds))

import csv

file = 'constellations_per_star.csv'

culturelist = []
no_dupe_list = []

with open('constellations_per_star.csv', 'r') as data:
    for line in csv.DictReader(data):
        cult = str(line['const_id'])
        if cult.startswith("kamilaroi"): 
            culturelist.append(cult[:-4])
        elif cult.startswith("japanese_moon_station"): 
            culturelist.append(cult[:-3])
        else: 
            culturelist.append(cult[:-4])
for culture in culturelist: 
    count = no_dupe_list.count(culture)
    if count < 1: 
        no_dupe_list.append(culture)
print(no_dupe_list)
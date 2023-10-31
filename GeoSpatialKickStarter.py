###import pandas as pd
##from geopy.geocoders import Nominatim
##import csv
##import folium
from folium.plugins import HeatMap

geolocator = Nominatim(user_agent = "geo")

m = folium.Map([41.0701,10.6298], zoom_start = 0)

df = pd.read_csv("KickStarterDataSmall.csv")

groupby_Loc = df["PROJECT_PAGE_LOCATION_NAME"].value_counts

df_groupbyLoc = groupby_Loc.reset_index()
df_groupbyLoc.column = ["Location", "Counts"]

listKS = df.values.tolist()

##singleLoc = listKS[0]

##print(singleLoc)

##location = geolocator.geocode(singleLoc[7])

with open('newKickStarterCountData.csv', 'w', newLine = '') as dataFile:
    wr = csv.writer(dataFile,quoting = csv.QUOTE_ALL)
    wr.writerow(["Location", "Count", "Latitude", "Longitude"])

    for row in listKS:
        location = geolocator.geocode(row[7])
        try:
            location = geolocator.geocode(row[0])
            row.append(location.latitude)
            row.append(location.longitude)
            wr.writerow(row)
        except:
            print("Location not found")

df_counts = pd.read_csv("newKickStartCountData.csv")

lats_longs_weight = list(map(list,zip(df_counts["Latitude"], df_counts["Longitude"], df["count"])))

HeatMap(lats_longs_weight).add_to(m)

m.save("kickstarter_project.html")

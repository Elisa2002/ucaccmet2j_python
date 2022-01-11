import json

with open ('precipitation.json') as precipitation_file:
    precipitation = json.load(precipitation_file)

#to be, final dictionary with resuls
all_locations_precipitations = {}

with open ('stations.csv') as stations_file:
    headers = stations_file.readline()

# calculating total yearly rain for all locations
    yearly_rain_total = 0
    for rain in precipitation:
        yearly_rain_total = yearly_rain_total + int(rain["value"])

# looping for each location 
    for line in stations_file:
        location, state, station = line.strip().split(',')
    
#making list with dictionaries for one location
        station_rain = []
        for weather in precipitation:
            if weather["station"] == station:
                station_rain.append(weather)

#making a list with rain per month per location
        station_monthly = []
        for i in range(1, 13):
            monthly_rain = 0

            for entry in station_rain:
                date = entry["date"].split('-')

                if int(date[1])== i:
                    monthly_rain = monthly_rain + int(entry["value"])
            station_monthly.append(monthly_rain)

#I forgot to commit after each step, to obtain result one was the above code without lines 9 to 19 
    #with open ('result1.json', 'w') as seatle_precipiation:
        #json.dump(seatle_monthly, seatle_precipiation)

#Calculating both yearly rain per location and relative yearly rain
        yearly_rain = 0
        for entry in station_rain:
            yearly_rain = yearly_rain + int(entry["value"])
        relative_yearly_rain = (yearly_rain/yearly_rain_total) * 100

#realtive monthly rain per location
        relative_monthly_rain = []
        for rain_value in station_monthly:
            percentage_rain_year = (rain_value/yearly_rain) * 100
            relative_monthly_rain.append(percentage_rain_year)

#Final dictionary  
        precipitation_summary = {
            'station': station,
            'state': state,
            'totalMonthlyPrecipitation': station_monthly,
            'relativeMonthly Precipitation': relative_monthly_rain,
            'totalYearlyPrecipiation': yearly_rain,
            'realtiveYearlyPrecipitation': relative_yearly_rain
        }
        all_locations_precipitations[location] = precipitation_summary

#I did not commit for step 2 but the code was the above without the relative yearly rate 
    #with open ('result2.json', 'w') as seatle_summary:
        #json.dump(precipitation_summary, seatle_summary, indent =4 )

with open ('result3.json', 'w') as all_locations_summary:
    json.dump(all_locations_precipitations, all_locations_summary, indent = 4)
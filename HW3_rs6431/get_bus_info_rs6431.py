from __future__ import print_function 
import json
import sys
import csv
#import pandas as pd

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

MTA_KEY = sys.argv[1]
level = "calls"
BUS_LINE = sys.argv[2] 

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=%s&LineRef=%s"%(MTA_KEY, level, BUS_LINE)

response = urllib.urlopen(url)
data = response.read().decode("utf-8") 
data = json.loads(data) 
data_filter = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
bus_csv = open(sys.argv[3], 'w')
bus_csv.write('Bus Line: ' + str(BUS_LINE) + '\n' + 'Number of Active Buses :' + str(len(data_filter)) + '\n' + 'Latitude,Longitude,Stop Name,Stop Status\n')

for i in data_filter:
    try:
        bus_location = i['MonitoredVehicleJourney']['VehicleLocation']
        bus_next = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
        Latitude = str(bus_location['Latitude'])
        Longitude = str(bus_location['Longitude'])
        bus_csv.write(Latitude + ',' + Longitude + ',' + bus_next['StopPointName'] + ',' + bus_next['Extensions']['Distances']['PresentableDistance'] + '\n')
    except KeyError:
        bus_location = i['MonitoredVehicleJourney']['VehicleLocation']
        Latitude = str(bus_location['Latitude'])
        Longitude = str(bus_location['Longitude'])
        bus_csv.write(Latitude + ',' + Longitude + ',' + 'N/A' + 'N/A')


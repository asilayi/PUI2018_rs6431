from __future__ import print_function

import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

MTA_KEY = sys.argv[1]
level = 'calls'
BUS_LINE = sys.argv[2] 

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=%s&LineRef=%s'%(MTA_KEY, level, BUS_LINE)

response = urllib.urlopen(url)
data = response.read().decode('utf-8') 
data = json.loads(data) 
data_filter = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

if not len(sys.argv) == 3:
    print ('Invalid number of arguments. Run as: python show_bus_locations_rs6431.py <MTA_KEY> <BUS_LINE>')
    sys.exit()

print('Bus Line :', sys.argv[2])
print('Number of Active Buses :', len(data_filter))
bus_index = 0
for i in data_filter:
    bus_location=i['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus',bus_index,'is at Latitude:', bus_location['Latitude'],'and Longitude',bus_location['Longitude'])
    bus_index+=1
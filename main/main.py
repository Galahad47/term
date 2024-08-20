import ephem
import numpy as np
from astropy.coordinates 
from astropy.time import Time
import datetime
import matplotlib.pyplot as  plt
import json


#time
format = "%Y-%m-%d %H:%M:%S"

time_input = input("Введите время в формате Год-Месяц-День Часы:Минуты:Секунды")
time = datetime.datetime.strptime(time_input,format)
formatted_time = time.strftime(format)
# time_str = "2024-02-17 18:00:00"





def terminatorcoords(date_time):
    eye = ephem.Observer()
    eye.date = date_time
    terminator_coords = []
    for lon in np.arange(-180,180,1):
        eye.lon = np.radians(lon)

        for lat in np.arange(-90,90):
            eye.lat = np.radians(lat)
            sun = ephem.Sun()
            sun.compute(eye)


            if abs(np.degrees(sun.alt))<0.5:

                terminator_coords.append((np.degrees(eye.lat),np.degrees(eye.lon)))
    
    
    return terminator_coords



date_time = datetime.datetime.strptime(formatted_time, format)
terminator_coords = terminatorcoords(date_time)
print("cords")
for coord in terminator_coords:
    print(f"lat {coord[0]}, lon {coord[1]}")


lat = terminator_coords[0]
lon = terminator_coords[1]


plt.plot(lat,lon)

plt.show()




coords = {terminator_coords[0],terminator_coords[1]}
with open("coords.json") as file:
    json.dump(coords,file)
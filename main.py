import numpy as np
import datetime
import matplotlib.pyplot as plt
import json

time_input = input("Введите время (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
time = datetime.datetime.strptime(time_input, "%Y-%m-%d %H:%M:%S")

# Функция для вычисления позиции Солнца
def calculate_sun_position(time):
    days = (time - datetime.datetime(2000, 1, 1, 12, 0, 0)).total_seconds() / (24 * 3600)
    obliquity = np.radians(23.44)

    mean_longitude = np.radians((280.460 + 0.9856474 * days) % 360)
    mean_anomaly = np.radians((357.528 + 0.9856003 * days) % 360)

    ecliptic_longitude = mean_longitude + np.radians(1.915) * np.sin(mean_anomaly) + np.radians(0.020) * np.sin(2 * mean_anomaly)

    declination = np.arcsin(np.sin(obliquity) * np.sin(ecliptic_longitude))

    return declination


def terminatorcoords(time):
    declination = calculate_sun_position(time)
    coords = []

    for lon in range(-180, 180):
        # Терминатор проходит по линии, где угол между горизонтом и солнцем равен 0 (полдень)
        lat = np.degrees(np.arcsin(-np.cos(np.radians(lon)) * np.cos(declination)))
        coords.append({"lat": lat, "lon": lon})
    
    return coords

# Сохранение координат терминатора и построения примера в виде графика

terminator_coords = terminatorcoords(time)
if terminator_coords:
    with open('terminator.json', 'w') as file:
        json.dump(terminator_coords, file)

    latitudes = [coord["lat"] for coord in terminator_coords]
    longitudes = [coord["lon"] for coord in terminator_coords]
    print (latitudes, longitudes)
    # plt.figure(figsize=(10, 5))
    # plt.plot(longitudes, latitudes, label='Терминатор', color='orange')
    # plt.fill_between(longitudes, min(latitudes), latitudes, where=np.array(latitudes) >= min(latitudes),
    #                  color='skyblue', alpha=0.5, label='Ночная сторона')
    # plt.xlabel('Долгота')
    # plt.ylabel('Широта')
    # plt.title('Терминатор на карте Земли')
    # plt.xlim(-180, 180)
    # plt.ylim(-90, 90)
    # plt.grid()
    # plt.axhline(0, color='black', lw=1)
    # plt.axvline(0, color='black', lw=1)
    # plt.legend()
    # plt.show()
else:
    print("Не обнаружены координаты терминатора на заданное время.")

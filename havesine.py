# -*- coding: utf8 -*-

from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半径，单位为公里
    return c * r

def read(filePath):
    lats = []
    lons = []
    stations = []
    with open(filePath) as f:
        line = f.readline()
        while line:
            station = line.split(',')[0]
            lat = line.split(',')[1]
            lon = line.split(',')[2]
            stations.append(station)
            lats.append(lat)
            lons.append(lon)
            print(line)
            line = f.readline()
    return stations, lats, lons

if __name__ == "__main__":
    filePath = 'E:\\WeatherData\\ghcnd-stations.csv'
    stations, lats, lons = read(filePath)
    print(len(lats),len(lats), lats[0], lons[0])
    collectionStations = []
    for i in range(len(lats)):
        distance = haversine(lon1=float(lons[1000]), lat1=float(lats[1000]),
                             lon2=float(lons[i]), lat2=float(lats[i]))
        if distance <= 500.0:
            collectionStations.append(stations[i])
            if distance == 0.0:
                print(stations[i])
    # print(collectionStations)
    print(len(collectionStations))


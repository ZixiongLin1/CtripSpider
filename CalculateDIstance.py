# Calculate the distance between hotel and landmark position by latitude and longitude.

from math import sin, cos, sqrt, atan2, radians
import csv
import numpy as np

def calculate_distance(lat1, lon1, lat2, lon2):
    '''Calculate the distance between 2 location have given latitude and longitude in km.'''
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


if __name__ == "__main__":
    print(calculate_distance(18.3603382110596, 109.750579833984, 18.3665, 109.750889))
    lat1 = 18.3603382110596
    lon1 = 109.750579833984
    with open('atlantis.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        row = reader.__next__()
        row[0] += ',distance'
        with_distance_array = np.array((row[0].split(',')))
        print(with_distance_array)
        row = reader.__next__()
        while(row != None):
            lat2 = float((row[0].split(','))[2])
            lon2 = float((row[0].split(','))[3])
            distance = calculate_distance(lat1, lon1, lat2, lon2)
            new_row = [(row[0] + (',' + str(distance))).split(',')]
            print(new_row)
            with_distance_array = np.vstack((with_distance_array, new_row))
            try:
                row = reader.__next__()
            except:
                print("end of the file")
                break
        with open("atlantis_with_distance.csv", 'w', encoding="utf-8-sig", newline="") as f:
            csvwriter = csv.writer(f, dialect='excel', delimiter=',')
            csvwriter.writerows(with_distance_array)
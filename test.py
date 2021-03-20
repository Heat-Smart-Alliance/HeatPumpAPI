from scipy.spatial import distance
from database import heatpump_coaches
import numpy as np

def run(data_input):
    closest_three = match_coach(data_input)

    output = [
        {
            'id': heatpump_coaches[closest_three[0]][0],
            'name': heatpump_coaches[closest_three[0]][1],
            'email': heatpump_coaches[closest_three[0]][2],
            'house': {
                'size': heatpump_coaches[closest_three[0]][3],
                'year': heatpump_coaches[closest_three[0]][4],
                'cost': heatpump_coaches[closest_three[0]][5]*1000,
                'stories': heatpump_coaches[closest_three[0]][6]/1000,
                'houseType': convert(heatpump_coaches[closest_three[0]][7]),
            }
        },
        {
            'id': heatpump_coaches[closest_three[1]][0],
            'name': heatpump_coaches[closest_three[1]][1],
            'email': heatpump_coaches[closest_three[1]][2],
            'house': {
                'size': heatpump_coaches[closest_three[1]][3],
                'year': heatpump_coaches[closest_three[1]][4],
                'cost': heatpump_coaches[closest_three[1]][5]*1000,
                'stories': heatpump_coaches[closest_three[1]][6]/1000,
                'houseType': convert(heatpump_coaches[closest_three[1]][7]),
            }
        },
        {
            'id': heatpump_coaches[closest_three[2]][0],
            'name': heatpump_coaches[closest_three[2]][1],
            'email': heatpump_coaches[closest_three[2]][2],
            'house': {
                'size': heatpump_coaches[closest_three[2]][3],
                'year': heatpump_coaches[closest_three[2]][4],
                'cost': heatpump_coaches[closest_three[2]][5]*1000,
                'stories': heatpump_coaches[closest_three[2]][6]/1000,
                'houseType': convert(heatpump_coaches[closest_three[2]][7]),
            }
        }
    ]
    return output


def convert(num):
    if num == 500:
        return 'Town House'
    elif num == 1000:
        return 'Ranch House'
    elif num == 1500:
        return 'Victorian'
    elif num == 2000:
        return 'House Type 4'
    elif num == 2500:
        return 'House Type 5'
    elif num == 3000:
        return 'House Type 6'


def match_coach(data_input):
    size = data_input['size']  # high: order of 3, typical = 1800
    year = data_input['year']  # high: order of 3, typical = 1960
    cost = data_input['cost']/1000  # low: order of 2, typical = $450,000
    stories = data_input['stories']*1000  # high: order of 3 = 2
    #location = data_input.location

    if data_input['houseType'] == 'Town House':
        houseType = 500
    elif data_input['houseType'] == 'Ranch House':
        houseType = 1000
    elif data_input['houseType'] == 'Victorian':
        houseType = 1500
    elif data_input['houseType'] == 'House Type 4':
        houseType = 2000
    elif data_input['houseType'] == 'House Type 5':
        houseType = 2500
    elif data_input['houseType'] == 'House Type 6':
        houseType = 3000

    data = [size, year, cost, stories, houseType]

    all_data = [i[3:] for i in heatpump_coaches]
    all_data.insert(0, data)

    D = distance.squareform(distance.pdist(all_data))
    sorted_closest = np.argsort(D, axis=1)
    k = 3  # For each point, find the 3 closest points
    closest = sorted_closest[:, 1:k+1]

    return closest[0]


data_input = {
    'size': 1766,
    'year': 1960,
    'cost': 480000,
    'stories': 2,
    'houseType': 'Town House'
}
print(run(data_input))
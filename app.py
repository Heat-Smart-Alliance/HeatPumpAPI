from flask import Flask, render_template, url_for, request, redirect, jsonify
from scipy.spatial import distance
from database import heatpump_coaches
import numpy as np
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    data_input = request.json
    return jsonify(data_input)

@app.route('/test', methods=['GET'])
def test():
    return {'message': "Hello World"}

@app.route('/run', methods=['POST', 'GET'])
def run():
    data_input = request.json
    closest_three = match_coach(data_input)

    output = {
        'output':
            [{
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
            }]
    }
    return jsonify(output)

def convert(num):
    if num == 500:
        return 'Town House'
    elif num == 1000:
        return 'Ranch'
    elif num == 1500:
        return 'Victorian'
    elif num == 2000:
        return 'Cape Cod'
    elif num == 2500:
        return 'Farm'
    elif num == 3000:
        return 'Condominium'
    elif num == 3500:
        return 'Bungalow'
    elif num == 4000:
        return 'Colonial'
    elif num == 4500:
        return 'Conventional'
    

def match_coach(data_input):
    size = data_input['size']  # high: order of 3, typical = 1800
    year = data_input['year']  # high: order of 3, typical = 1960
    cost = data_input['cost']/1000  # low: order of 2, typical = $450,000
    stories = data_input['stories']*1000  # high: order of 3 = 2
    #location = data_input.location

    if data_input['houseType'] == 'Town House':
        houseType = 500
    elif data_input['houseType'] == 'Ranch':
        houseType = 1000
    elif data_input['houseType'] == 'Victorian':
        houseType = 1500
    elif data_input['houseType'] == 'Cape Cod':
        houseType = 2000
    elif data_input['houseType'] == 'Farm':
        houseType = 2500
    elif data_input['houseType'] == 'Condominium':
        houseType = 3000
    elif data_input['houseType'] == 'Bungalow':
        houseType = 3500
    elif data_input['houseType'] == 'Colonial':
        houseType = 4000
    elif data_input['houseType'] == 'Conventional':
        houseType = 4500

    data = [size, year, cost, stories, houseType]

    all_data = [i[3:] for i in heatpump_coaches]
    all_data.insert(0, data)

    D = distance.squareform(distance.pdist(all_data))
    sorted_closest = np.argsort(D, axis=1)
    k = 3  # For each point, find the 3 closest points
    closest = sorted_closest[:, 0:k]

    return closest[0]


if __name__ == "__main__":
    app.run(debug=True)
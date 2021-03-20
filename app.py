from flask import Flask, render_template, url_for, request, redirect, jsonify
from scipy.spatial import distance
from database import heatpump_coaches

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
    return closest_three


def match_coach(data_input):
    size = data_input.size #high: order of 3, typical = 1800
    year = data_input.year #high: order of 3, typical = 1960
    cost = data_input.cost/1000 #low: order of 2, typical = $450,000
    stories = data_input.stories*1000 #high: order of 3 = 2
    #location = data_input.location
    
    if data_input.houseType == 'Town House':
        houseType = 500
    elif data_input.houseType == 'Ranch House':
        houseType = 1000
    elif data_input.houseType == 'Victorian':
        houseType = 1500
    elif data_input.houseType == 'House Type 4':
        houseType = 2000
    elif data_input.houseType == 'House Type 5':
        houseType = 2500
    elif data_input.houseType == 'House Type 6':
        houseType = 3000
    
    data = [size, year, cost, stories, houseType]
    heatpump_coaches.insert(0, data)

    D = distance.squareform(distance.pdist(points))
    sorted_closest = np.argsort(D, axis=1)
    k = 3  # For each point, find the 3 closest points
    closest = sorted_closest[:, 1:k+1]

    return closest[0]


if __name__ == "__main__":
    app.run(debug=True)
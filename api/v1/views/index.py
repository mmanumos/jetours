#!/usr/bin/python3
'''
routes:
/status - returns status: Ok
'''
from api.v1.views import app_views
from flask import jsonify
from flask import request


@app_views.route('/status/', methods=['GET'])
def status():
    """Route for return API status """
    return jsonify({'status': 'OK'})


@app_views.route('/sorted_numbers/', methods=['GET'])
def sorted_numbers():
    """Return a sorted list of numbers """
    if 'numbers' in request.args:
        try:
            numbers = request.args.get('numbers').replace("[", "")
            numbers = numbers.replace("]", "")
            numbers = [int(i) for i in numbers.split(",")]
            numbers = sorted(numbers)
            return jsonify({'response': numbers})
        except Exception:
            return jsonify({'error': "datatype"})
    else:
        return jsonify({'error': 'key numbers nof found'})


@app_views.route('/name_file/', methods=['GET'])
def name_file():
    """ return the number of capital letters in a file """
    file = request.files['file']
    f = file.read()
    count = 0
    for x in f:
        if x >= 65 and x <= 90:
            count = count + 1

    return jsonify({'number_of_capital_letters': count})

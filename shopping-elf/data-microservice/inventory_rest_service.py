import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,Response

from flask import json
from flask import jsonify
from werkzeug import secure_filename
import processed_data_service as pdservice;

app = Flask(__name__)



@app.route("/inventory/list/<username>", methods=['GET'])
def getShoppingList(username):
    #return  pdservice.getShoppingList(username))


    j = jsonify(pdservice.getShoppingList(username));


    return j


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=3008)
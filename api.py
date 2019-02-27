# -*- coding: utf-8 -*-
import json
import time
import requests
import sys

from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin

app = FlaskAPI(__name__)
CORS(app, resources={ r"/api/*": {"origins": "*"}}, supports_credentials=True)

@app.route("/api/Token", methods=["GET"])
def token():
    return "ce2314c9-97ec-4d9b-a230-12365110e22b"

@app.route("/api/ReverseWords", methods=["GET"])
def ReverseWords():
    s = request.args.get("sentence", "")
    return s[::-1]

@app.route("/api/Fibonacci", methods=["GET"])
def Fibonacci():
    n = request.args.get("n", "0")
    if not n.isdigit():
        return "The request is invalid.", status.HTTP_400_BAD_REQUEST
    
    n = int(n)
    ls = [0, 1]
    if n == 0 or n == 1:
        return str(ls[n])
    else:
        for i in range(2, n + 1):
            ls.append(ls[i-1] + ls[i-2])

        return str(ls[n])

@app.route("/api/TriangleType", methods=["GET"])
def TriangleType():
    a = request.args.get("a", "")
    b = request.args.get("b", "")
    c = request.args.get("c", "")
    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        return "The request is invalid.", status.HTTP_400_BAD_REQUEST

    a, b, c = int(a), int(b), int(c)
    if a == 0 or b == 0 or c == 0:
        return "Error", status.HTTP_400_BAD_REQUEST

    ls = [a, b, c]
    ls.sort(key=int)
    if ls[0] + ls[1] <= ls[2]:
        return "Error", status.HTTP_400_BAD_REQUEST

    if a == b:
        if b == c:
            return "Equilateral"
        else:
            return "Isosceles"
    elif b == c:
        return "Isosceles"
    else:
        return "Scalene"


if __name__ == '__main__':
    app.run(port=5000, debug=True)

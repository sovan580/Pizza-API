import json
from flask import request, Response
from pizzaapi import app
from pizzaapi.database.db import new_order, all_orders, single_order
from mongoengine import errors
from rq import Queue
from rq.job import Job
from pizzaapi.worker import conn

q = Queue(connection=conn)

# Task-1 Welcome API
@app.route("/api/welcome", methods=["GET"])
def welcome():
    return "Welcome to Pizza House", 200

# Task-2 and 4 Accept order API
@app.route("/api/order", methods=["POST"])
def addOrder():
    try:
        data = request.get_json()
        # Old API To Insert Into DB
        # id = new_order(data)
        # return str(id), 200

        # New API Logic to Insert through Message Queue
        job = q.enqueue(new_order, data)
        res = {"Status": "Accepted", "Job Id": str(job.id)}
        return Response(json.dumps(res), mimetype="application/json", status=200)

    except Exception as e:
        res = {"Error": str(e)}
        return Response(json.dumps(res), mimetype="application/json", status=400)

# Task-3.1 Get all order details API
@app.route("/api/getorders", methods=["GET"])
def getAllOrders():
    try:
        data = all_orders()
        return Response(data, mimetype="application/json", status=200)
        
    except Exception as e:
        res = {"Error": str(e)}
        return Response(json.dumps(res), mimetype="application/json", status=400)

# Task-3.2 Get single order details API
@app.route("/api/getorders/<id>", methods=["GET"])
def getSingleOrder(id):
    try:
        data = single_order(id=id)
        return Response(data, mimetype="application/json", status=200)

    except Exception as e:
        res = {"Error": str(e)}
        return Response(json.dumps(res), mimetype="application/json", status=400)

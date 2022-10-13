from flask_mongoengine import MongoEngine

from pizzaapi.database.models import Order
# MongoDB URI
MONGO_URI = "mongodb+srv://test-user:test123@cluster0.zdb7i.mongodb.net/pizza_house"   
from pizzaapi import app

#Databse Congiguration
app.config['MONGODB_SETTINGS'] = {
    'host': MONGO_URI,
}
db = MongoEngine()
db.init_app(app)

# All Operations for the DB
def new_order(body):                                # New Order Request
    pizza=Order(**body).save()
    id=pizza.id
    return id

def all_orders():                                   # All Order Show Request
    pizzas=Order.objects().to_json()
    return pizzas

def single_order(id):                               # Particular Order Show Request
    pizza=Order.objects().get(id=id).to_json()
    return pizza

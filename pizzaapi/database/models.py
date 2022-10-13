from mongoengine import Document
from mongoengine import StringField,  ListField

class Order(Document):
    cust_name = StringField(required=True)                 # Data field for Customer's Name
    cust_mobile = StringField(required=True)               # Data field for Customer's Mobile Number
    order = ListField(StringField(), required=True)        # Data field for Order List
    address = StringField(required=True)                   # Data field for Customer's Address
    email = StringField(required=True)                     # Dat field for Customer's email id

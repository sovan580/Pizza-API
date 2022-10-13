# Pizza-API
Basic pizza ordering API using Flask and MongoDB.

## Running the Application
1. Clone the Repo
2. In the root folder run `pip install e .`
3. Now run the Redis Server. 
  On Linux it is `redis-server`
4. In the pizzaapp folder, run `python worker.py` in a separate terminal. This starts worker for redis
5. Finally run `flask --app pizzaapi run`. This starts the flask application
6. To test the application, run `pytest`

## API Documentation
The details of the API and its request with their response are listed below :-

**1. Welcome**
----
  Returns a string : "Welcome to Pizza House".

* **URL**

  /api/welcome

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `Welcome`


**2. Place Order**
----
  Returns json data about the order id.

* **URL**

  /api/order

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
   
    None
   

* **Data Params**

  `cust_name = string`
  
   `cust_mobile = int`
   
   `order = List of string`
   
   `address = string`
   
   `email = string`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    
    `{
         
         id : "String id"
    
    }`

* **Error Response:**

  * **Code:** 400  <br />
    **Content:** `{ Error : Exception error }`
    

**3. Show all Orders**
----
  Returns json data about all the orders.

* **URL**

  /api/getorder

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    
    `{
    
        { 
        
            "cust_name : "String",
            
            "cust_mobile" : "int",
            
            "order" : ["String item1","String item2",...],
            
            "address" : "String",
            
            "email" : "String"
            
        },
        
        {
        
            "cust_name : "String",
            
            "cust_mobile" : "int",
            
            "order" : ["String item1","String item2",...],
            
            "address" : "String",
            
            "email" : "String"
            
        }.....
        
    }`

* **Error Response:**

  * **Code:** 400  <br />
    **Content:** `{ Error : Exception error }`


**4.Show a particular Order**
----
  Returns json data about a prticular order.

* **URL**

  /api/getorder/<id>

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
  
  `{
  
        {
  
            "cust_name : "String",
  
            "cust_mobile" : "int",
  
            "order" : ["String item1","String item2",...],
  
            "address" : "String",
  
            "email" : "String"
  
        }
  
    }`
* **Error Response:**

  * **Code:** 400  <br />
    **Content:** `{ Error : Exception error }`


## Dependencies
```async-timeout==4.0.2
click==8.1.3
Deprecated==1.2.13
dnspython==2.2.1
email-validator==1.3.0
Flask==2.2.2
flask-mongoengine==1.0.0
Flask-WTF==1.0.1
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
mongoengine==0.24.2
packaging==21.3
pymongo==4.2.0
pyparsing==3.0.9
redis==4.3.4
rq==1.11.1
Werkzeug==2.2.2
wrapt==1.14.1
WTForms==3.0.1```
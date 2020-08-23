# Multi Tenancy Example
This repo aims to show how to implement a multi-tenancy architecture using postgres/sqlAlchemy/python/flask

A detailled medium [article]() throught a hypothetical use case, and explains the step in order to comprehend the architecture

## Usage and test

You can still test the multi-tenancy without going throught the article


### populate the database:

    psql -h [host] -d [database] -U [user] -f "db/init&populate.sql" -W


### requierements:

    # if you wana use a virtual env
    python3 -m venv .my_env 
    source .my_env/bin/activate
    # install requierements
    pip install -r requierements.txt
    # start the server
    python app.py

#### Request : 
You can send a post method with the following body : 

    {
    "user_id": "2", 
    "organization_id": "client2"
    }

you have requested the schema **client2** and will have a response :

    {
      "message": "orders successfully returned",
      "results": [
        {
          "item name": "Tesla",
          "item price": 1000.0,
          "item quantity": 10,
          "total fee": 10000.0,
          "user name": "poor_dude"
        },
        {
          "item name": "Huawei",
          "item price": 100.0,
          "item quantity": 5,
          "total fee": 500.0,
          "user name": "poor_dude"
        }
      ]
    }


if you wana request the schema **client1** use the body :

    {
    "user_id": "1", 
    "organization_id": "client1"
    }

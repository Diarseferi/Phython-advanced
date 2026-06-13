# Json data set
#
# {
#   "name": "Diar",
#   "age": "16",
#   "address": {
#     "Country": "Kosovo",
#     "City": "Prishtine",
#     "ZIP Code": "10000",
#     "Street": "Rruga B"
#   },
#   "contacts":[
#     {
#       "type":"email",
#       "value":"diarseferi23@gmail.com"
#     },
#     {
#       "type":"phone",
#       "value":"+3838387368"
#     },
#     {
#       "type":"Linkedin",
#       "value":"Diar"
#     }
#   ]
# }

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {
    "name": "Diar",
    "age": "16",
    "address": {
    "Country": "Kosovo",
    "City": "Prishtine",
    "ZIP Code": "10000",
    "Street": "Rruga B"
  },
    "contacts":[
    {

        "type":"email",
         "value":"diarseferi23@gmail.com"
    },
    {
         "type":"phone",
        "value":"+3838387368"
    },
    {
        "type":"Linkedin",
         "value":"Diar"
    }
  ]
}
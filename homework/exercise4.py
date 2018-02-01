from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db['customers']
customer_list = customers.find()

events = 0
wom = 0
ads = 0
for customer in customer_list:
    if customer['ref'] == 'events':
        events += 1
    elif customer['ref'] == 'wom':
        wom += 1
    elif customer['ref'] == 'ads':
        ads += 1

print("Number of customers purchased from events is", events)
print("Number of customers purchased from word of mouth", wom)
print("Number of customers purchased from advertisements", ads)

import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot
text = ['events', 'wom', 'ads']
values = [events, wom, ads]
color = ['red', 'orange', 'blue']

pyplot.pie(values, labels = text, colors = color)
pyplot.axis('equal')

pyplot.show()

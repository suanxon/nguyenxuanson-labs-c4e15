from pymongo import MongoClient


mongo_uri ="mongodb://suanxon:10D180110@ds157873.mlab.com:57873/xuanson"
#@ds157873: sever
#57873: cua vao
#xuanson: database

#1. Open a connection to mlab
client = MongoClient(mongo_uri)

#2. Get datebase
db =client.get_default_database()
#3. Get collection
game = db['games']   # retrieve collection

game_list = game.find()
for game in game_list:
    print(game['tile'])


# #4. Create a new document
# new_blog = {
#     'play': 'soccer',
#     'music': 'Dan Truong',
#     'food' : 'banh trung'
# }
# #5. Put the created document into collection
# blog.insert_one(new_blog)

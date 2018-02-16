import pymongo
m=pymongo.MongoClient()
for user in m.tests.insertTest.find().sort("Date/Time").limit(100):
    print(user)
import pymongo
import pandas as pd

m=pymongo.MongoClient()
df=pd.DataFrame(list(m.tests.insertTest.find()))
result=df.sort_values(["Date/Time"])
print(result)
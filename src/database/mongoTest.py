from mongoDB import Mongo

test = Mongo('jdauphar@kent.edu','Test tweet')

x = test.read_collection()
print(x)

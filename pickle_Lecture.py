#Data- 27-09-24
import pickle

data= {"name":"Alice","age":30 ,"occupation":"Engineer"}
with open("data.pickle","wb") as file:
    pickle.dump(data,file)
print("Data has been serialized and saved to data.pickle")


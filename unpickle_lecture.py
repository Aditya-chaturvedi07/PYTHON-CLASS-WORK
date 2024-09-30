#Data- 27-09-24
import pickle
with open("data.pickle","rb") as file:
    loaded_data=pickle.load(file)
print("deserialized data",loaded_data)
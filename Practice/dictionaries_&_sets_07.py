# Dictionaries are as like as JS objects. it crets with key, value pairs

bandDictionary = {
    "vocals": "Arnab",
    "guiter": "Friends"
}

band2 = dict(vocals="James", guiter="Ayub")

print(bandDictionary)
print(band2)
print(type(bandDictionary))
print(len(band2))

# Access the dictionary items/values
print(band2["vocals"])
print(band2.get("guiter"))

# list all keys
print(band2.keys())

# list all items/value
print(band2.values())

# list of key.value pairs as tuples
print(band2.items())

# verify a key exists, boolean value
print("guiter" in band2)
print("flute" in band2)

# change values
band2["vocals"] = "Naim"
band2.update({"bass": "BDCTG"})

print(band2)

# Remove items
print(band2.pop("bass"))
print(band2)

band2["drums"] = "Sin"
print(band2)

# print(band2.popitem())
print(band2)

# Delete and clear items

band2["drums"] = "Sin"
del band2["drums"]
print(band2)

band2.clear()
print(band2)

del band2

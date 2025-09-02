import json

# JSON.dumps

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"}

# json_data = json.dumps(data)

# print(json_data)




#json.loads

# json_data = '{"name": "John", "age": 30, "city": "New York"}'

# data = json.loads(json_data)

# print(data)
# print(data["name"])



# json.dump
# data={
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }


# with open("data.json", "w") as file:
#     json.dump(data, file)




# json.load
with open("data.json", "r") as file:
    data = json.load(file)
print(data)

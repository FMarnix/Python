person = {"name": "Filipe", "gender": "male", "age": 34, "address": "Aveiro", "phone": 912043021}

key = input("What information do you want to know about the person? ").lower()

result = person.get(key, "That information is not available")

print(result)

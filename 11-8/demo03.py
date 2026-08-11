def person_info(data):
    match data:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}")
        case _:
            print("Unknown format")

person_info({"name": "Harsha", "age": 24})
person_info({"name": "Harsha"})
person_info({"city": "Bangalore"})
dog = {}
dog = {
    "name" : "Triana",
    "color" : "Blanca",
    "breed" : "Bichonmaltes",
    "legs" : "Cuatro patas",
    "age" : "5 años"}
    
print(dog)

student = {
    "first_name": "Lucia",
    "last_name" : "Rubiales",
    "gender" : "Mujer",
    "age" : "16",
    "marital status" : "Con novio",
    "skills" : ["Dibujar", "Estudiar"],
    "country" : "España",
    "city" : "Jerez",
    "addres" : "Barriada San Jose Obrero", }
print(student)
print(len(student))
print(student["skills"])

print(type(student))

student["skills"].append("Bailar") 
student["skills"].append("Cantar")
print(student)

keys = student.keys()
print(keys)

values = student.values()
print(student)

print(student.items())

print(student.clear())

del student



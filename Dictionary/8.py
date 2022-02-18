car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

col={ "color":"red"}

print("car: {}".format(car))
print("col: {}".format(col))

car.update(col)
print("new car: {}".format(car))
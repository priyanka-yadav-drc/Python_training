colors = [{"id" : "#FF0000", "color" : "Red"}, 
          {"id" : "#800000", "color" : "Maroon"}, 
          {"id" : "#FFFF00", "color" : "Yellow"}, 
          {"id" : "#808000", "color" : "Olive"}] 

for d in colors:
	if d["id"]=="#800000":
		colors.remove(d)

print(colors)
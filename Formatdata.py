import csv as f

data = []

with open("name.csv", newline='') as raw:
  file = f.reader(raw)
  for row in file:
    templist = []
    templist.append(row[0])
    templist.append(row[1])
    data.append(templist)
    
formatted = []

for item in data:
  formatted.append("'\'hline \n" + str(item[0]) + "&" + str(item[1]) = "'\\'\n")
  
print(formatted)

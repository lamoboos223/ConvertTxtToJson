import json 
  
  
filename = 'label.labels.txt'
dict1 = {} 
  
with open(filename) as fh: 
    i = 0
    for line in fh: 
        line = str(i) + " " + line
        key, value = line.strip().split(None, 1) 
  
        dict1[key] = value.strip() 
        i = i + 1

out_file = open("labels.json", "w") 
json.dump(dict1, out_file, indent = 4, sort_keys = False) 
out_file.close()
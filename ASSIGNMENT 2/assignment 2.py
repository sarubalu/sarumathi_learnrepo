import json

with open('2nd assignment\Ex5.json','r') as file:
    Ex5 = json.load(file)
    #print("Printing the JSON File:\n",Ex5)
    
for i in ex5:
    
    if i['name'] == 'Old Fashioned':
        x=i['batters']['batter']
        
        max_id=0
        for id in x:
            cur_id = int(id["id"])
            if cur_id > max_id:
                max_id = cur_id
        last_id=str(max_id + 1)
        z={ "id": last_id, "type": "Coffee" }
        x.append(z)
        
print("\nAfter adding 'Coffee' to JSON File:\n",Ex5)

with open('2nd assignment\Ex5.json','w') as out:
    json.dump(ex5,out,indent=4)
#%% 
# Convert JSON to CSV
import util

jsonDumps = [
    "./json/khe16/users.json",
    "./json/khe16/apps.json",
    "./json/khe17/users.json",
    "./json/khe17/apps.json",
    "./json/khe18/users.json",
    "./json/khe18/apps.json",
]

for table in jsonDumps:
    csv = table.replace("json","csv")
    print(table," to ", csv)
    util.jsonToCsv(table, csv)

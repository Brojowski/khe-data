#%%
import csv
import json
#%%
with open("./json/khe16/users.json") as jsonFile:
    jsonDf = json.load(jsonFile)

#%%
print(jsonDf)

#%%

#%% 
# Convert JSON to CSV
import util

csvDumps = [
    "./csv/khe16/users.csv",
    "./csv/khe16/apps.csv",
    "./csv/khe17/users.csv",
    "./csv/khe17/apps.csv",
    "./csv/khe18/users.csv",
    "./csv/khe18/apps.csv",
]

for table in csvDumps:
    json = table.replace("csv","json")
    print(json," to ", table)
    util.jsonToCsv(json, table)

#%%
import pandas as pd

#%%
# Remove sensitive data from applications

# 16: _id,name,school,phone,shirt,demographic,first,year,age,gender,major,conduct,status,going,checked,door,dietary,probable,created,__v,travel
# 17: _id,name,school,phone,shirt,demographic,first,year,age,gender,major,conduct,link,status,going,checked,door,dietary,probable,created,__v
# 18: _id,name,school,phone,shirt,demographic,first,year,age,gender,major,conduct,travel,resume,link,status,going,checked,door,dietary,extra,probable,created,__v

sensitiveCols = [
    "name",
    "phone",
    "__v",
    "resume",
    "link",
    "extra"
]

for csv in filter(lambda x: "apps.csv" in x, csvDumps):
    appDf = pd.read_csv(csv)

    for col in sensitiveCols:
        if col in appDf.columns:
            appDf = appDf.drop(col, axis=1)
    
    appDf.to_csv(csv.replace("csv", "cleaned", 1), index=False)
    

#%%

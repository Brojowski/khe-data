#%%
from showed import showedUp

khe18 = showedUp("./cleaned/khe18/apps.csv")
khe18.head()

#%%
import json
import numpy as np

#%%
diets = khe18["dietary"]
diets.head()

#%%
def pullOutOfArray(dietaryRestrictions):
    if dietaryRestrictions == '':
        return None
    dietaryRestrictions = dietaryRestrictions.replace("'", '"')
    restrictions = json.loads(dietaryRestrictions)
    if len(restrictions) > 0:
        return restrictions[0].lower().strip()
    else:
        return None

#%%
diets = diets.apply(pullOutOfArray)
diets.head()

#%%
diets.value_counts()

#%%

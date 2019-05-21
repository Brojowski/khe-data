import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime

def removeMongoDateWrapper(created):
        created = created.replace("'", '"')
        return datetime.fromisoformat(json.loads(created)["$date"][:10])


def plotAttendeesByAppTime(appsCsv):
    khe = pd.read_csv(appsCsv)
    khe.head()

    attended = khe[ khe["checked"] == True]
    attended.head()

    # print("Total applied: ", len(khe))
    # print("Total attended: ", len(attended))

    khe["dateApplied"] = khe["created"].apply(removeMongoDateWrapper)
    khe.head()

    showDf = pd.DataFrame()
    showDf["checkedIn"] = khe["checked"]
    showDf["dateApplied"] = khe["dateApplied"]
    showDf.head()

    showed = showDf[ showDf["checkedIn"] == True]
    skipped = showDf[ showDf["checkedIn"] == False]
    # print("Came: ", len(showed))
    # print("Skipped:", len(skipped))

    # First person applied
    startReg = showDf["dateApplied"].min()
    # Realistic last day to register (last day of the hackathon)
    endReg = showDf["dateApplied"].max()
    registrationPeriod = pd.date_range(start=startReg, end=endReg)

    showCounts = showed.groupby("dateApplied").count()
    showCounts.head()

    showX = showCounts.index
    showX

    showY = showCounts["checkedIn"].values
    showY

    skipCounts = skipped.groupby("dateApplied").count()
    skipX = skipCounts.index
    skipY = skipCounts["checkedIn"].values

    plt.figure(figsize=(10, 10))
    plt.bar(skipX, skipY, color="red")
    plt.bar(showX, showY, color="green")
    plt.xticks(registrationPeriod)
    return plt.plot()



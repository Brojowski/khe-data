import pandas as pd

def showedUp(appCsvPath):
    appDf = pd.read_csv(appCsvPath)
    showedDf = appDf[ appDf["checked"] == True]
    return showedDf
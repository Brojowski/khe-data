import csv
import json

def jsonToCsv(jsonPath, csvPath):
    with open(jsonPath) as jsonFile:
        jsonDf = json.load(jsonFile)     

    with open(csvPath, "w+", newline="") as csvFile:
        writer = csv.writer(csvFile)
        keys = jsonDf[0].keys()
        _ = writer.writerow(jsonDf[0].keys())
        for row in jsonDf:
            values = []
            for key in keys:
                try:
                    values.append(row[key])
                except KeyError:
                    values.append("")
            writer.writerow(values)

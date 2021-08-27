import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Marks_in_percentage = []
    Days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Marks_in_percentage.append(float(row[ "Marks In Percentage" ]))
            Days_present.append(float(row["Days Present"]))

    return {"x" :Marks_in_percentage, "y": Days_present }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days Present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()

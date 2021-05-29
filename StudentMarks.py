import csv
import plotly.express as px
import numpy as np

def findCorrelation():
    studentMarks = []
    daysPresent = []
    with open("StudentMarks.csv") as f:
        df = csv.DictReader(f)
        for row in df:
            studentMarks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    correlation = np.corrcoef(studentMarks, daysPresent)
    print(correlation[0,1])
findCorrelation()
import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path,encoding='utf_8') as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    Marks_In_Percentage = []
    Days_Present = []
    with open(data_path,encoding='utf_8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks_In_Percentage"]))
            Days_Present.append(float(row["Days_Present"]))

    return {"x" :Marks_In_Percentage, "y": Days_Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks_In_Percentage vs Days_Present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)
setup()
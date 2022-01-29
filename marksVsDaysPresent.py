import numpy as np
import csv 
import plotly.express as px
import pandas as pd



def getDataSource(data_path , series1 , series2 ) :

    series1_list = []
    series2_list = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            series1_list.append(float(row[series1]))
            series2_list.append(float(row[series2]))

    return {"x" : series1_list , "y" : series2_list}

def findCorrelation(datasource) :
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation :",correlation[0,1])

def plotFigure(data_path) :
    with open(data_path) as f:
        data_frame = csv.DictReader(f)
        fig = px.scatter(data_frame=data_frame , x ="Days Present" , y= "Marks In Percentage",title= "Effect of Days Student is present in school on his/her Marks")
        fig.show()

def setup() :
    data_source = getDataSource("Student Marks vs Days Present.csv","Days Present","Marks In Percentage")
    findCorrelation(data_source)

setup()
plotFigure("Student Marks vs Days Present.csv")
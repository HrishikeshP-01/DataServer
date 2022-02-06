import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def getDF(filename):
    df = pd.read_csv(filename)
    return df

def makeLinePlot(df, xAxis, yAxis, opFileName):
    df.plot(kind='line',x=xAxis,y=yAxis)
    plt.savefig(opFileName)

def makeScatterPlot(df, xAxis, yAxis, opFileName):
    df.plot(x=xAxis, y=yAxis, style='o')
    plt.savefig(opFileName)

def makeHistogram(df, xAxis, yAxis, opFileName):
    df.hist()
    plt.show()
    plt.savefig(opFileName)

df = getDF("x.csv")
makeHistogram(df, "Time", "Flex", "z.png")
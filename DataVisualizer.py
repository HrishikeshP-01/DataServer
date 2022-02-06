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

def makeHistogram(df, Axis, opFileName):
    df[Axis].hist()
    plt.savefig(opFileName)

df = getDF("data.csv")
makeHistogram(df,"Flex", "FlexHist.png")
makeLinePlot(df,"Time","Flex","FlexPlot.png")
makeHistogram(df, "Temp", "TempHist.png")
makeLinePlot(df,"Time","Temp","TempPlot.png")
makeHistogram(df, "Pulse", "PulseHist.png")
makeLinePlot(df,"Time","Pulse","PulsePlot.png")
df.hist()
plt.savefig("Overview.png")
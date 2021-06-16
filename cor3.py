import plotly.express as px
import csv 
import numpy as np
def getsource(path):
    isales=[]
    csales = []
    with open(path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            isales.append(float(row["Temperature"]))
            csales.append(float(row["Ice-cream Sales( ₹ )"]))
    return{'x':isales,'y':csales}
def findcor(source):
    cor = np.corrcoef(source['x'],source['y'])
    print(cor[0,1])
def setup():
    path = './file1.csv'
    datasource = getsource(path)
    findcor(datasource)
setup()
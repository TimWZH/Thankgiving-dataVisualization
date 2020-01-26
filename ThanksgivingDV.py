import pyecharts

import pandas as pd
import numpy as np
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Pie

from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode

from pyecharts.charts import Map;
from pyecharts.datasets import register_url

datafile = './thanksgiving.csv'
data = pd.read_csv(datafile,encoding = 'utf-8')
mainDish = data['What is typically the main dish at your Thanksgiving dinner?']

mainDishList = mainDish.tolist()
maindDishCount = mainDish.value_counts()
names = mainDish.value_counts().index.tolist()
count = mainDish.value_counts().tolist()

##############HeatMap################
import random

from pyecharts.faker import  Faker
from pyecharts import options as opts
from pyecharts.charts import HeatMap

USRegion = data['US Region']
USRegionCount = USRegion.value_counts()
USRegionList = USRegion.tolist()
USRegionSet = list(set(USRegionList))
dfUSRegion = pd.DataFrame(USRegionSet)
dfUSRegion2 = dfUSRegion.dropna(axis=0,how='any')

Brussel = data['Sides dishes - Brussel sprouts'].tolist()
BrusselMerge = [list(z) for z in zip(USRegion.tolist(), Brussel)]
BrusselCount = pd.value_counts(list([tuple(t) for t in BrusselMerge]))

Sides2 = data['Sides dishes - Carrots'].tolist()
MergeSides2 = [list(z) for z in zip(USRegion.tolist(), Sides2)]
CountSides2 = pd.value_counts(list([tuple(t) for t in MergeSides2]))

Sides3 = data['Sides dishes - Cauliflower'].tolist()
MergeSides3 = [list(z) for z in zip(USRegion.tolist(), Sides3)]
CountSides3 = pd.value_counts(list([tuple(t) for t in MergeSides3]))

Sides4 = data['Sides dishes - Corn'].tolist()
MergeSides4 = [list(z) for z in zip(USRegion.tolist(), Sides4)]
CountSides4 = pd.value_counts(list([tuple(t) for t in MergeSides4]))

Sides5 = data['Sides dishes - Cornbread'].tolist()
MergeSides5 = [list(z) for z in zip(USRegion.tolist(), Sides5)]
CountSides5 = pd.value_counts(list([tuple(t) for t in MergeSides5]))

Sides6 = data['Sides dishes - Fruit salad'].tolist()
MergeSides6 = [list(z) for z in zip(USRegion.tolist(), Sides6)]
CountSides6 = pd.value_counts(list([tuple(t) for t in MergeSides6]))

Sides7 = data['Sides dishes - Green beans/green bean casserole'].tolist()
MergeSides7 = [list(z) for z in zip(USRegion.tolist(), Sides7)]
CountSides7 = pd.value_counts(list([tuple(t) for t in MergeSides7]))

Sides8 = data['Sides dishes - Macaroni and cheese'].tolist()
MergeSides8 = [list(z) for z in zip(USRegion.tolist(), Sides8)]
CountSides8 = pd.value_counts(list([tuple(t) for t in MergeSides8]))

Sides9 = data['Sides dishes - Mashed potatoes'].tolist()
MergeSides9 = [list(z) for z in zip(USRegion.tolist(), Sides9)]
CountSides9 = pd.value_counts(list([tuple(t) for t in MergeSides9]))

Sides10 = data['Sides dishes - Rolls/biscuits'].tolist()
MergeSides10 = [list(z) for z in zip(USRegion.tolist(), Sides10)]
CountSides10 = pd.value_counts(list([tuple(t) for t in MergeSides10]))

Sides11 = data['Sides dishes - Squash'].tolist()
MergeSides11 = [list(z) for z in zip(USRegion.tolist(), Sides11)]
CountSides11 = pd.value_counts(list([tuple(t) for t in MergeSides11]))

Sides12 = data['Sides dishes - Vegetable salad'].tolist()
MergeSides12 = [list(z) for z in zip(USRegion.tolist(), Sides12)]
CountSides12 = pd.value_counts(list([tuple(t) for t in MergeSides12]))

Sides13 = data['Sides dishes - Yams/sweet potato casserole'].tolist()
MergeSides13 = [list(z) for z in zip(USRegion.tolist(), Sides13)]
CountSides13 = pd.value_counts(list([tuple(t) for t in MergeSides13]))

Sides14 = data['Sides dishes - Other'].tolist()
MergeSides14 = [list(z) for z in zip(USRegion.tolist(), Sides14)]
CountSides14 = pd.value_counts(list([tuple(t) for t in MergeSides14]))

# for i in range(len(USRegion)):
#     for j in range(len(le))
#    data[i] = dUSRegion2.ix[i+1]

dataScores = [
[27/203,41/145,29/130,7/56,22/145,4/85,3/71,12/55,6/41],
[48/203,45/145,30/130,15/56,28/145,21/85,12/71,25/55,11/41],
[11/203,25/145,18/130,5/56,13/145,3/85,3/71,4/55,4/41],
[96/203,77/145,55/130,31/56,76/145,46/85,35/71,22/55,17/41],
[53/203,33/145,37/130,16/56,23/145,34/85,12/71,10/55,10/41],
[39/203,26/145,35/130,20/56,20/145,30/85,18/71,5/55,11/41],
[150/203,92/145,84/130,49/56,103/145,66/85,60/71,33/55,31/41],
[79/203,20/145,18/130,21/56,21/145,20/85,12/71,6/55,3/41],
[157/203,130/145,112/130,45/56,127/145,70/85,65/71,52/55,38/41],
[158/203,106/145,99/130,49/56,123/145,73/85,62/71,41/55,33/41],
[31/203,44/145,17/130,12/56,15/145,8/85,2/71,31/55,5/41],
[39/203,33/145,39/130,8/56,26/145,15/85,15/71,11/55,12/41],
[144/203,99/145,85/130,44/56,90/145,63/85,33/71,34/55,26/41],
[27/203,16/145,13/130,10/56,17/145,10/85,5/71,7/55,5/41]
]

inputData = [[i,j, round(dataScores[i][j]*100)] for i in range(14) for j in range(9)]

#SouthAtlantic,MiddleAtlantic,Pacific,EastSouthCentral,EastNorthCentral,WestSouthCentral,WestNorthCentral,NewEngland,Mountain
#203,145,130,56,145,85,71,55,41

USRegionOrder = ['SA','MA','Pac','ESC','ENC','WSC','WNC','NE','Mou']

SidesList = ['Brussel sprouts' , 'Carrots' , 'Cauliflower' , 'Corn' , 'Cornbread' , 'Fruit salad' , 'Green beans/green bean casserole' , 'Macaroni and cheese' , 'Mashed potatoes' , 'Rolls/biscuits' , 'Squash' , 'Vegetable salad' , 'Yams/sweet potato casserole' , 'Other']

def heatmap_base() -> HeatMap:
    value = inputData
#    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
        .add_xaxis(SidesList)
        .add_yaxis("HeatMap", USRegionOrder, value,
                   label_opts=opts.LabelOpts(is_show=True, position="inside",interval= 0)                                             )
        .set_global_opts(
            #title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
            visualmap_opts=opts.VisualMapOpts(pos_left = "right"),
           # axis =opts.AxisOpts(offset=100,is_show= False,name_gap = 0, interval = 200)
        )
    )
    return c



heatmap = heatmap_base()

heatmap.render("heatmap9.html")

################Map##################

travel = data['How far will you travel for Thanksgiving?']
travelList = travel.tolist()
#travelListReplace = travelList.replace("Thanksgiving is local--it will take place in the town I live in","Local")

#for z in  travelList:
 #   str(z).replace("Thanksgiving is local--it will take place in the town I live in", "Local")


travelListReplace = [str(z).replace("Thanksgiving is local--it will take place in the town I live in","Local") for z in travelList]
travelListReplace = [str(z).replace("Thanksgiving is out of town but not too far--it's a drive of a few hours or less","Not far") for z in travelListReplace]
travelListReplace = [str(z).replace("Thanksgiving is happening at my home--I won't travel at all","Home") for z in travelListReplace]
travelListReplace = [str(z).replace("Thanksgiving is out of town and far away--I have to drive several hours or fly","Far") for z in travelListReplace]

travelMerge = [list(z) for z in zip(travelListReplace, USRegion.tolist())]

# def all_np(arr):
#     arr = np.array(arr)
#     key = np.unique(arr)
#     result = {}
#     for k in key:
#         mask = (arr == k)
#         arr_new = arr[mask]
#         v = arr_new.size
#         result[k] = v
#     return result
#
# targetCount = all_np(tuple(travelMerge))

targetCount2 = pd.value_counts(list([tuple(t) for t in travelMerge]))
#targetCount2 = pd.value_counts(set([tuple(t) for t in travelMerge]))


targetCountList = targetCount2.tolist()
targetCountIndex = targetCount2.index.tolist()


TargetCountDict = targetCount2.to_dict()




SouthAtlantic = (86*0 + 61*25 + 38*75 + 18 *100) / (86+61+38+18)
EastNorthCentral = (64*0 + 42*25 + 31*75+ 8*100)/(64+42+31+8)
Pacific = ( 61*0 + 39*25 + 18*75 +12*100)/(61+39+18+12)
MiddleAtlantic = (58 * 0 + 38*25 + 35*75 + 14*100)/ (58+38+35+14)
EastSouthCentral = ( 20*0 + 23*25 + 10*75 +6*100)/(20+23+10+6)
WestSouthCentral = ( 36*0 + 23*25 + 18*75 +8*100)/(36+23+18+8)
WestNorthCentral = ( 30*0 + 25*25 + 13*75 +8*100)/(30+25+13+8)
NewEngland =  ( 17*0 + 11*25 + 22*75 +5*100)/(17+11+22+5)
Mountain =  ( 17*0 + 8*25 + 9*75 +7*100)/(17+8+9+7)

df = pd.DataFrame([SouthAtlantic,EastNorthCentral,Pacific,MiddleAtlantic,EastSouthCentral,WestSouthCentral,WestNorthCentral,NewEngland,Mountain])
#data2 = (df-df.mean())/(df.std())
data3 = (df-df.min())/(df.max()-df.min()) *100 #max-min normalization
MapSA = ['Florida','Georgia','South Carolina','North Carolina','West Virginia','Delaware', 'Maryland', 'Virginia']
MapMA = ['New Jersey','New York','Pennsylvania']
MapNE = ['Maine', 'Vermont', 'New Hampshire', 'Massachusetts', 'Rhode Island', 'Connecticut']
MapENC =['Illinois', 'Indiana', 'Michigan', 'Ohio','Wisconsin']
MapPaci = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']
MapESC = [ 'Alabama', 'Kentucky', 'Mississippi', 'Tennessee']
MapWSC = [ 'Arkansas', 'Louisiana', 'Oklahoma','Texas']
MapMou = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming']
MapWNC = [ 'Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']

#inputData = [['Florida'，data3.ix(0)]]

dataSA = data3.ix[0].tolist() * len(MapSA)
dataENC = data3.ix[1].tolist() * len(MapENC)
dataPaci = data3.ix[2].tolist() * len(MapPaci)
dataMA = data3.ix[3].tolist() * len(MapMA)
dataESC = data3.ix[4].tolist() * len(MapESC)
dataWSC = data3.ix[5].tolist() * len(MapWSC)
dataWNC = data3.ix[6].tolist() * len(MapWNC)
dataNE = data3.ix[7].tolist() * len(MapNE)
dataMou = data3.ix[8].tolist() * len(MapMou)

def geo_base() -> Map:
    register_url("https://echarts-maps.github.io/echarts-countries-js/")
    c = (
        Map()
        .add("South Atlantic",(list(z) for z in zip(MapSA,dataSA)),maptype = "美国", is_map_symbol_show = False)
        .add("Pacific", (list(z) for z in zip(MapPaci, dataPaci)), maptype="美国", is_map_symbol_show=False)
        .add("East North Central", (list(z) for z in zip(MapENC, dataENC)), maptype="美国", is_map_symbol_show=False)
        .add("East South Central", (list(z) for z in zip(MapESC, dataESC)), maptype="美国", is_map_symbol_show=False)
        .add("West South Central", (list(z) for z in zip(MapWSC, dataWSC)), maptype="美国", is_map_symbol_show=False)
        .add("West North Central", (list(z) for z in zip(MapWNC, dataWNC)), maptype="美国", is_map_symbol_show=False)
        .add("New England", (list(z) for z in zip(MapNE, dataNE)), maptype="美国", is_map_symbol_show=False)
        .add("Mountain", (list(z) for z in zip(MapMou, dataMou)), maptype="美国", is_map_symbol_show=False)
        .add("Middle Atlantic", (list(z) for z in zip(MapMA, dataMA)), maptype="美国", is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
           # title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    return c

geo = geo_base()

geo.render("geo6.html")

######################Pie####################
def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(names, count)])
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

c = pie_base()



c.render("pie1.html")


####################bar###########################
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

b = bar_base()
b.render("bar1.html")
#################################################
# print(pyecharts.__version__)
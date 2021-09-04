import csv
from collections import Counter
with open("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    n_num=fileData[i][2]
    newData.append(float(n_num))

data=Counter(newData)
mode_data_for_range={
    "75-110":0,"110-145":0,"145-175":0
}
for height,occurence in data.items():
    if 75<float(height)<110:
        mode_data_for_range["75-110"]+=occurence
    elif 110<float(height)<145:
        mode_data_for_range["110-145"]+=occurence
    elif 145<float(height)<175:
        mode_data_for_range["145-175"]+=occurence

node_range, mode_occurence=0,0
for range,occurence in mode_data_for_range.items():
        if occurence>mode_occurence:
            mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((mode_range[0]+mode_range[1])/2)
print("mode is",mode)
            
    

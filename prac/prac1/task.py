import csv

def transform(list):
    for i in list:
        i = float(int(i))
    return list

with open("CSCO.csv") as csco:
    date , open, high, low, close, adj_close, volume = [], [], [], [], [], [], []
    csco_file = csv.reader(csco)
    
    for row in csco_file:
        date.append(row[0])
        open.append(row[1])
        high.append(row[2])
        low.append(row[3])
        close.append(row[4])
        adj_close.append(row[5])
        volume.append(row[6])

# task 5
print(date[1:11])
print(open[1:11])
print(high[1:11])
print(low[1:11])
print(close[1:11])
print(adj_close[1:11])
print(volume[1:11])


# task 6 # finish
transform(open) 
print(open[1:11])
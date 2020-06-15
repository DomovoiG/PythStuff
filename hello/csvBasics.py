#CSV basics. 
import csv
from datetime import datetime
#CSV is a text file that contains data. 
#in each row data is seperated by commas. data is all stored as strings (including numeric values).
#if there are two commas in a row than there is a piece of data missing. 

path = str("C:\\Data\\google_stock_data.csv")

#file = open(path)
#for line in file:
#    print(line)

#storing data. 

#without using CSV modual.
 #you can user strip() to remove leading or trailing whiespace
 #you can use split() with ',' as an argument to break each line up by the , delimeter

 #dataset = [line.strip.(split(',')) for line in open(path)]
#unfortuanatly this doesn'y handle lots of issues with possible incoming data.  so lets use the csv module instead.


#using csv module

#print(dir(csv)) #this will show you whay functions are available in the csv module. 


file = open(path, newline='')
reader = csv.reader(file)
 
header = next(reader) #The first line is the header
data = [] 
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    openPrice = float(row[1]) 
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adjClose = float(row[6])

    data.append([date, openPrice, high, low, close, volume, adjClose])

#print(data[0])

#compute and store daily stock returns.

returns_path = "C:\\Data\\google_returns.csv" #This is the output file.
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):#This os accessing all of the data and assigning it to given variables (per line)
    todaysRow = data[i]
    todaysDate = todaysRow[0]
    todaysPrice = todaysRow[-1]
    yesterdaysRow = data[i+1]
    yesterdaysPrice = yesterdaysRow[-1]
    #Then we do some math to the given date (per line) and send it to a new file. 
    dailyReturn = (todaysPrice - yesterdaysPrice) / yesterdaysPrice
    writer.writerow([todaysDate, dailyReturn])
    formattedDate = todaysDate.strftime('%m/%d/%Y')
    writer.writerow([formattedDate, dailyReturn])
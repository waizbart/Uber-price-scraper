import matplotlib.pyplot as plt
import csv
  
date = []
uberx = []
comfort = []
  
with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        date.append(row[0])
        uberx.append(float(row[1]))
        comfort.append(float(row[2]))

time = mapped_numbers = list(map(lambda time: time[11:19], date))

dados = {}

for i in time:
    dados[i] = uberx[time.index(i)]
  
plt.plot(time, uberx, color = 'black', label = "Preço UberX")
plt.xlabel('Horários')
plt.ylabel('Valores')
plt.title('Valores Uber')
plt.legend()
plt.show()
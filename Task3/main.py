'''
Некоторый поезд в пути следования останавливается на N станциях.
Дан список пассажиров поезда, для каждого из которых известно,
на какой станции он садится, а на какой - выходит.
Определите, на каких перегонах в поезде было наибольшее число пассажиров.
'''
file = open('open1.txt',"r", encoding="utf-8")
N = file.readline() # кол-во станций
countStations = {}
while True :
    readingStr = file.readline()
    data = readingStr.split()
    if not readingStr:
        break
    for i in range(int(data[2]), int(data[3])) :
        interval = str(i) + " " + str(i+1)
        if not(interval in countStations) :
            countStations[interval] = 1
        else :
            countStations[interval] += 1
file.close()
maxValue = max(countStations.values())
for key, value in countStations.items():
    if(value == maxValue):
        s = key.split()
        print(f"{s[0]}-{s[1]}")
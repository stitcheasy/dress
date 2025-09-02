import csv

def getmeasurement(filename="measurement.csv"):
    with open (filename, "r") as source:
        reader = csv.reader(source)
        data = []
        for row in reader:
            data.append(row)
            #print(row)
        # shoulder=data[1][0]
        # chest=data[1][1]
        # waist=data[1][2]
        # hip=data[1][3]
        # length=data[1][4]
        # sleeve=data[1][5]
        

        # print(shoulder)
        # print(chest)
        # print(waist)
        # print(hip)
        # print(length)
        # print(sleeve)
    return data


#print(getmeasurement())    
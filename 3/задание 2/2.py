import csv
def f():
    with open('f.csv') as a:
        reader=csv.reader(a)
        for row in reader:
            print (row)
f()

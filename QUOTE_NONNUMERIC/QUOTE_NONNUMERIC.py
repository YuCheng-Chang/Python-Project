import csv

with open('numbers.csv', newline='') as csvfile:
    favourites = csv.reader(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
    print(type(favourites))
    for row in favourites:
        print(type(row[0]), type(row[1]))
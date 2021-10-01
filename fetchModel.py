import csv

from werkzeug.wrappers import response


def fetchMovie(name):
    ### Algorithm to search date and return a list of data ###
    ###########################################################
    count = 0
    res = {}
    data = []
    # data2 = {"dob": "", "id": "", "name": "", "dept": ""}
    with open("data/db.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    # print(data)

    # name = input("Enter a first name: ")

    # gives us a list of everything in col 0
    col = [x[0] for x in data]

    # print(col)

    dt = name[5:]

    if dt in col:
        for x in range(0, len(data)):
            if dt == data[x][0]:
                res[count] = data[x]
                count = count + 1
        return(res)

    else:
        return 0
    ###########################################################

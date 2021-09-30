import csv


def fetchMovie(name):
    ### Algorithm to search date and return a list of data ###
    ###########################################################
    data = []
    data2 = {"dob": "", "id": "", "name": "", "dept": "", }
    with open("data/db.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    # print(data)

    # name = input("Enter a first name: ")

    # gives us a list of everything in col 0
    col = [x[0] for x in data]

    # print(col)

    if name in col:
        for x in range(0, len(data)):
            if name == data[x][0]:
                data2["dob"] = data[x][0]
                data2["id"] = data[x][1]
                data2["name"] = data[x][2]
                data2["dept"] = data[x][3]
                return(data2)

    else:
        return("Number does not exist")
    ###########################################################

# importing pandas as pd
import pandas as pd
import os.path

# list of uid, name, date of birth and depertment
uid = []
name = []
dob = []
dept = []


def accept():
    # accepting all the data and appending into the lists
    tuid = int(input())
    tname = input()
    tdob = input()
    tdept = input()
    uid.append(tuid)
    name.append(tname)
    dob.append(tdob)
    dept.append(tdept)


def append():
    # dictionary of lists
    dict = {'id': uid, 'name': name, 'dob': dob, 'dept': dept}
    df2 = pd.DataFrame(dict)

    if os.path.exists('data.csv'):
        df = pd.read_csv('data.csv')
        print(df.to_string())
        df.append(df2)
    else:
        df2.to_csv('data.csv')
#       print(df.to_string())


def main():
    accept()
    append()


if __name__ == "__main__":
    main()

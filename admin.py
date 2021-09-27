# importing pandas as pd
import pandas as pd
import os.path


def accept():
    # list of uid, name, date of birth and depertment
    uid = []
    name = []
    dob = []
    dept = []
    # accepting all the data and appending into the lists
    tuid = int(input())
    tname = input()
    tdob = input()
    tdept = input()
    uid.append(tuid)
    name.append(tname)
    dob.append(tdob)
    dept.append(tdept)
    append(uid, name, dob, dept)


def append(uid, name, dob, dept):
    # dictionary of lists
    dict = {'id': uid, 'name': name, 'dob': dob, 'dept': dept}
    # dictionary into dataframe
    df = pd.DataFrame(dict)

    if os.path.exists('data.csv'):
        df.to_csv('data.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('data.csv', index=False)
#       print(df.to_string())

def main():
    accept()

if __name__ == "__main__":
    main()

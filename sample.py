# imagesave.py>
# importing pandas as pd
import pandas as pd
import os.path
import datetime

def foldercreate():
    import os
    path = 'data/passport'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
      # Create a new directory because it does not exist 
      os.makedirs(path)
      print("The new directory is created!")

    return path

def accept():
    # list of uid, name, date of birth and depertment
    uid = []
    name = []
    dob = []
    dept = []
    
    # accepting all the data and appending into the lists
    tuid = int(input('ID:'))
    tname = input('Name:')
    tdob = input("enter time in this format yyyy-mm-dd:")
    tdob = datetime.datetime.strptime(tdob, "%Y-%m-%d")
    tdept = input('Dept:')
    
    uid.append(tuid)
    name.append(tname)
    dob.append(tdob)
    dept.append(tdept)
    addcsv(uid, name, dob, dept)


def addcsv(uid, name, dob, dept):
    # dictionary of lists
    dict = {'id': uid, 'name': name, 'dob': dob, 'dept': dept}
    # dictionary into dataframe
    df = pd.DataFrame(dict)

    if os.path.exists('data/data.csv'):
        df.to_csv('data/data.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('data/data.csv', index=False)
#       print(df.to_string())

    passport(uid,path)


def passport(tuid,path):
   
  #Import required Image library
  from PIL import Image

  image = Image.open('cat1.jpg')
  new_image = image.resize((100, 150))
  filename=str(tuid)+'.jpg'
  new_image.save(path+'/'+filename)

  print(image.size) # Output: (100, 150)

path=foldercreate()
accept()
# importing Pandas, OS, Python Pillow
import pandas as pd
import os.path
from PIL import Image


def foldercreate():
    import os
    path = 'data/photo'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)


def append(num, nm, db, dt):
    foldercreate()
    # list of uid, name, date of birth and depertment
    uid = []
    name = []
    dob = []
    dept = []
    uid.append(num)
    name.append(nm)
    dob.append(db)
    dept.append(dt)
    # dictionary of lists
    dict = {'id': uid, 'name': name, 'dob': dob, 'dept': dept}
    # dictionary into dataframe
    df = pd.DataFrame(dict)

    if os.path.exists('data/db.csv'):
        df.to_csv('data/db.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('data/db.csv', index=False)

    return "Success"


def img(uid):
    path = 'data/photo'
    # img_path = str(uid)+'.jpg'

    # #########################################################################################
    # # image processing script
    # basewidth = 300
    # # Create an Image Object from an Image
    # img = Image.open(im_dir)
    # wpercent = (basewidth/float(img.size[0]))
    # hsize = int((float(img.size[1])*float(wpercent)))
    # # Make the new image half the width and half the height of the original image
    # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # # Save the cropped image
    # img.save(sv_dir + img_path, quality=90)
    # ########################################################################################

    image = Image.open('temp.jpg')
    new_image = image.resize((200, 200))
    filename = str(uid)+'.jpg'
    new_image.save(path+'/'+filename)

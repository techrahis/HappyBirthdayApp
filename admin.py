# importing Pandas, OS, Python Pillow
import pandas as pd
import os.path
from PIL import Image


def append(num, nm, db, dt):
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

    if os.path.exists('data.csv'):
        df.to_csv('data.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('data.csv', index=False)

    return "Success"


def img(uid, path_img):
    im_dir = 'img\\'
    img_path = str(uid)+'.jpg'

    #########################################################################################
    # image processing script
    basewidth = 300
    # Create an Image Object from an Image
    img = Image.open(path_img)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    # Make the new image half the width and half the height of the original image
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # Save the cropped image
    img.save(im_dir + img_path, quality=90)
    ########################################################################################

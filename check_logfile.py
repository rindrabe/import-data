import os
import pandas as pd
import math

submissions = pd.read_csv('/.../kcpostlog.csv') #specify the path of your logfile
path = "/.../tempfiles/" # Specify path of your tempfiles

count = 0

for i in range(len(submissions)):
    if submissions['code'][i] == 201 :
        filename = submissions['uuid'][i]+".xml"
        full_filename = path + filename    
        os.remove(full_filename)
        count = count + 1

print("SUCESS --- TOTAL TO BE IMPORTED =",len(submissions)," --> SENT =",count," | | | NOT SENT =",(len(submissions)-count))

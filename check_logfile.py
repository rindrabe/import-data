import os
import pandas as pd
import math

submissions = pd.read_csv('/Users/rindra/Desktop/TheWorldBank/GEMS/consolidated_portfolio/code_and_data/test_repeating_groups/kcpostlog.csv')
path = "/Users/rindra/Desktop/TheWorldBank/GEMS/consolidated_portfolio/code_and_data/test_repeating_groups/tempfiles/"

count = 0

for i in range(len(submissions)):
    if submissions['code'][i] == 201 :
        filename = submissions['uuid'][i]+".xml"
        full_filename = path + filename    
        os.remove(full_filename)
        count = count + 1

print("SUCESS --- TOTAL TO BE IMPORTED =",len(submissions)," --> SENT =",count," | | | NOT SENT =",(len(submissions)-count))

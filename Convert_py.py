
#importing pandas as pd 
import pandas as pd 
import os
import re

path = "D:/DM/"
files = os.listdir(path)

files_xlsx = [f for f in files if f[-4:] == 'xlsx']

for f in files_xlsx:
    csvf = re.sub("xlsx","csv",f)
    if(os.path.isfile(csvf)):
        print(csvf+" file exist")
        continue
    print("old file: "+f+", new file: "+csvf)

    read_file = pd.read_excel (f, sheet_name='工作表1') 
    read_file.to_csv (csvf,  
                    index = None, 
                    header=True) 
    

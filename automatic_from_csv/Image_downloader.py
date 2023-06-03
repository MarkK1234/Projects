#THIS DEMO PROGRAM WILL TAKE IMAGE URL'S AND DOWNLOAD THEM IN A FOLDER

# IMPORTS
import csv
import requests
import os

# GETTING CURRENT WORKING DRIRECTORY
cwd = os.getcwd()
print(cwd)

# MAKES DIRECTORY IF IT DOESNT EXIST YET
os.makedirs(f'{cwd}/All_Images/', exist_ok=True )

# OPENS THE CSV FILE IN THE CORRECT ENCODING AND DOWNLOADS THEM USING THE REQUESTS IMPORT
count = 1
with open(f'{cwd}/pics_ex.csv', 'r', encoding='utf-8-sig') as urls:
    # GOES THROUGHT THE CSV FILE
    reader = csv.reader(urls)
    for rows in reader:
        for item in rows:
            response = requests.get(item).content   
            with open(f'{cwd}/All_Images/img{count}.jpeg', 'wb') as f:
                f.write(response)
                count += 1
    

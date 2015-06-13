import requests, csv, json, os
import pandas as pd

from create_csv import save_to_csv # make sure the file exist in the same folder.

# Access the file
root_folder = os.path.dirname(os.path.realpath(__file__))
data = pd.read_csv(root_folder + "/unmatched postal codes.txt",
    converters={'postal_code': lambda x: str(x)})

# Crude extraction of X and Y
holder = [["Coordinate", "x", "y"]]
for i in data["postal_code"]:
    response = requests.get(url="http://www.onemap.sg/API/services.svc/basicSearch?token=qo/s2TnSUmfLz+32CvLC4RMVkzEFYjxqyti1KhByvEacEdMWBpCuSSQ+IFRT84QjGPBCuz/cBom8PfSm3GjEsGc8PkdEEOEr&searchVal="+ i + "&otptFlds=SEARCHVAL,CATEGORY&returnGeom=0&rset=1")
    x = float(json.dumps(response.json()).split(",")[-1].split(":")[1].split("\"")[1])
    y = float(json.dumps(response.json()).split(",")[-2].split(":")[1].split("\"")[1])
    coordinates = [i,x,y]
    holder.append(coordinates)

data_store = root_folder + "/create_csv_test.txt" # save as txt to account for leading zeros
save_to_csv(data_store, holder)

import csv, os

def save_to_csv(namefile, data):
    with open(namefile,'wb') as outfile:
        f=csv.writer(outfile)
        for i in data:
            f.writerow(i)

# to_load_test = [['One', "Two", "Three" ], ['1','2','3']]
# root_folder = os.path.dirname(os.path.realpath(__file__))
# data_store = root_folder + "/create_csv_test.csv"
# save_to_csv(data_store, to_load_test)

"""
The file should be in the format as shown in to_load_test.

To test, remove comments and a file should be produced into the current directory of this file.Preferred format is a list of lists. This follows the previous formats that I have used for my own side projects, and is the most intuitive approach for me. However, this may not be the most efficient way.
"""

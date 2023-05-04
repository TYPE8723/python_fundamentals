#csv file**
#A CSV (Comma Separated Values) format is one of the most simple and common ways to store tabular data. To represent a CSV file, it must be saved with the .csv file extension.
import csv
#read csv files
#To read a CSV file in Python, we can use the csv.reader() function.
with open('data.csv') as csv_file:
    #arguments in reader
    #delimiter = '\t'
    # skipinitialspace=True
    # *quoting=csv.QUOTE_ALL#Using csv.reader() in minimal mode will result in output with the quotation marks. to remove them we can use this
    # *skipinitialspace=True#skipps initial space
    # *data = csv.reader(csv_file,quoting=csv.QUOTE_ALL, skipinitialspace=True)
    data = csv.reader(csv_file,delimiter = '\t')
    for row in data:
        print(row)

csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open("write_data.csv",'w')as csv_write:
    writer=csv.writer(csv_write)
    #writer.writerow(['row1','row2','row3'])#write a row at a time
    writer.writerows(csv_rowlist)
###REFER DICT READER|DICT WRITER#####
#DICT READER reads as key value pair
with open('data.csv') as csv_file:
    data = csv.DictReader(csv_file)
    for i in data:
        print(i)
#DICT writer writes as key value pair

with open('write_data_dict.csv','w') as write_dict:
    field_list = ['player_name', 'fide_rating']
    writer = csv.DictWriter(write_dict,fieldnames=field_list)
    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
    writer.writerows([
                        {'player_name': 'Magnus Carlsen', 'fide_rating': 2870},
                        {'player_name': 'Fabiano Caruana', 'fide_rating': 2822},
                        {'player_name': 'Ding Liren', 'fide_rating': 2801}
                    ])
    
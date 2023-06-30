import pandas as pd
csvdf=pd.read_csv('pandas_sample.csv')
print(csvdf.head())#first 5 file
print(csvdf)
#createing data frame
# # songs ={
# #     'Album':['Thriller','meanig of life','smooth criminal','do you know who you are?'],
# #     'artist':['MJ','ROBOT','JSPR','JKROWLING'],
# #     'Released':[1982,1239,4235,2312],
# #     'Length':['3min','1hr','5hr','4min']
# # }
# # sdf=pd.DataFrame(songs)
# # print(sdf)
# print(sdf[['artist','Album']])

#finding unique elements
print(csvdf['place'].unique())

#finding price higher than 5 laks
print(csvdf['cost in lk']>=5)

#table of data whos value is higher than 5 laks
print(csvdf[csvdf['cost in lk']>=5])

#to save these in csv use .to_csv
ndf1=csvdf[csvdf['cost in lk']>=5]
ndf1.to_csv('new_dt.csv')

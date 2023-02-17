import pandas

#data = pandas.read_csv('weather_data.csv')
##print(type(data))
##print(data['temp'])
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data['temp'].to_list()
#print(temp_list)
#print(data['temp'].max())
#
##Get Data in Columns
#print(data['condition'])
#print(data.condition)

#Get Data in Row
#print((data[data.day == 'Monday']))
#
#print(data[data.temp == data.temp.max()])

#monday_temp = data[data.day == 'Monday']
#print((monday_temp.temp * 9/5)+32)

#Create a dataFrame from Scratch
#data_dict = {
#    'students': ['Amy', 'James', 'Angela'],
#    'scores': [76, 56, 65]
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv('new_data.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_fur_count = len(data[data['Primary Fur Color'] == 'Gray'])
black_fur_count = len(data[data['Primary Fur Color'] == 'Black'])
cina_fur_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print(grey_fur_count)
print(black_fur_count)
print(cina_fur_count)

data_dict = {
    "Fur Color ": ['Grey', 'Cinnamon', 'Black'],
    'Count': [grey_fur_count, black_fur_count, cina_fur_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv('Squirrel Count.csv')



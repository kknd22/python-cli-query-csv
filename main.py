import re
import sys

# h - headers of displaying column 
h = ['id', 'name', 'type', 'location', 'address', 'status', 'food', 'zip']

# p - position of columns that we are interested
p = [0, 1, 2, 4, 5, 10, 11, 28]

# w - width of displaying of the columns
w = [8, 32 , 10, 48, 16, 10, 48, 5 ]

# in memory db
dataRecords = []

'''
  import (selective) data from the csv file into a list of fixed length list of strings 
'''
def importData(csvFileName):
  import csv
  with open(csvFileName, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lines = []
    for row in csv_reader:
      lines.append([row['locationid'], row['Applicant'], row['FacilityType'], row['LocationDescription'], row['Address'], row['Status'], row['FoodItems'], row['Zip Codes'] ] )
  return lines

'''
  display info and collect user import query
'''
def prompts():
  print('')
  print('Use the following format to query food truck data (case insensetive):')
  print('search format: field=value ')
  print('at present only support these seven searchable fields: name, type, location, address, status, food, zip')
  print('')
  print('example: name=INNOVATION LLC')
  print('example: food=vagan')
  print('example: zip=28855')
  print('')
  print('------------------------------------------------------------------')
  print('To print out a single untruncated record:')
  print('id=value')
  print('')
  print('example: id=1569145')
  print('')
  print('------------------------------------------------------------------')
  print('type "help" to display this')
  print('type "quit" to exit the program')
  print('')
  
'''
  read command and run search
'''
def doSearch():
  s = input()  
  # quit if instructed
  if (s == 'quit'):
    sys.exit()
  
  # help if instructed
  if (s == 'help'):
    prompts()
    return
  # validate input basic format
  kv = s.split("=")
  if (len(kv) != 2):
    print('invalid command')
    return
  # validate input basic format
  k = kv[0].strip()
  v = kv[1].strip()
  if not k in h:
    print(f'"{k}" is not one of the seven supported filed.')
    return
  if k == 'id':
    locateSingleRecordWithId(v)
  else:
    displayQueryResults(k, v)

def locateSingleRecordWithId(id_value):
  results = [x for x in dataRecords if x[0]==id_value]
  if not results:
    print (f'id with "{id_value}" does not exist' )
    print('')
    return
  print (' | '.join(results[0]))
  print('')
  print('input new query: ')

def displayQueryResults(k, v):
  print(f'{h[0]:{w[0]}} | {h[1]:{w[1]}} | {h[2]:{w[2]}} | {h[3]:{w[3]}} | {h[4]:{w[4]}} | {h[5]:{w[5]}} | {h[6]:{w[6]}} | {h[7]:{w[7]}}')
  print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  index = h.index(k)
  count = 0
  for x in dataRecords:
    if re.search(v, x[index], re.IGNORECASE):
      print(f'{x[0]:<{w[0]}} | {x[1][:w[1]]:<{w[1]}} | {x[2]:<{w[2]}} | {x[3][:w[3]]:<{w[3]}} | {x[4][:w[4]]:<{w[4]}} | {x[5]:<{w[5]}} | {x[6][:w[6]]:<{w[6]}} | {x[7]:<{w[7]}} ' )
      count = count+1
  if count==0 :
    print(f'{k} = {v} does not exist')
  else:
   print('')
   print('input new query: ')

# this is the man entry 
if __name__ == "__main__":
  dataRecords=importData('foodtruck.csv')
  prompts()
  while True:
    doSearch()






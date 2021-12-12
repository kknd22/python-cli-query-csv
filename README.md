# python-cli-query-csv
Python CLI to Query Food Truck Data in CVS File

## Overview
The code illustrate a simple Python 3 based CLI program to query a SF food truck data in CSV format.

## Prerequisite
Python 3 

## Usage
unpack the 2 files main.py and foodtruck.csv in a directory
run `python3 main.py`
should see this prompts:
``` 
Use the following format to query food truck data (case insensetive):
search format: field=value 
at present only support these seven searchable fields: name, type, location, address, status, food, zip

example: name=INNOVATION LLC
example: food=vegan
example: zip=28855

------------------------------------------------------------------
To print out a single untruncated record:
id=value

example: id=1569145

------------------------------------------------------------------
type "help" to display this
type "quit" to exit the program
```
sample input and results"
```
food=vegan
id       | name                             | type       | location                                         | address          | status     | food                                             | zip
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1569145  | Casita Vegana                    | Truck      | JOHN MUIR DR: LAKE MERCED BLVD to SKYLINE BLVD ( | Assessors Block  | APPROVED   | Coffee: Vegan Pastries: Vegan Hot Dogs: Vegan Ta | 64    

input new query: 
id=1569145
1569145 | Casita Vegana | Truck | JOHN MUIR DR: LAKE MERCED BLVD to SKYLINE BLVD (200 - 699) | Assessors Block 7283/Lot004 | APPROVED | Coffee: Vegan Pastries: Vegan Hot Dogs: Vegan Tamales: Te: Vegan Shakes | 64

input new query: 
```


## Note
This simple program does not make use all data fields. Only these 7 fields are used:
- locationid (id)
- Applicant (application)
- FacilityType (type)
- LocationDescription (location)
- Address (address)
- Status (status)
- FoodItems (food)
- Zip Codes (zip)

All searches are single field only (case insensitive).  
Search `id=xxxxx` will display a single non trucated data.  
All other searches will display potentional trucated data for easy display purpose.




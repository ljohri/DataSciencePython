import csv
#%precision 2

print ('hello world')

with open('mpg.csv') as csvfile:
    record = list(csv.DictReader(csvfile))
    
print(record[:3]) # The first three dictionaries in our list.
print('\n')
print( record[0].keys())
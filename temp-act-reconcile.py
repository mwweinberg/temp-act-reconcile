import csv

#creates the output list
output_csv_list = []

#turns csvs into lists of lists

with open('old.csv', 'rU') as f:
    reader = csv.reader(f)
    old_csv_list = list(list(rec) for rec in csv.reader(f, delimiter=','))
    #removes the ordinals for each entry because they are not relevant
    for element in old_csv_list:
        del element[0]
    #print(old_csv_list)

with open('new.csv', 'rU') as f:
    reader = csv.reader(f)
    new_csv_list = list(list(rec) for rec in csv.reader(f, delimiter=','))
    for element in new_csv_list:
        del element[0]
    #print(new_csv_list)

# if element is not in old list, add to output list

for element in new_csv_list:
    if element in old_csv_list:
        print('existing entry')
    else:
        print('new entry')
        output_csv_list.append(element)

#Add spaces so the output is correctly formatted

for element in output_csv_list:
    #adds a blank entry to each of these spaces
    element.insert(0, '')
    element.insert(1, '')
    element.insert(2, '')
    element.insert(4, '')
    element.insert(6, '')
    element.insert(7, '')
    element.insert(9, '')
    element.insert(11, '')
    element.insert(12, '')

#output to CSV
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(output_csv_list)

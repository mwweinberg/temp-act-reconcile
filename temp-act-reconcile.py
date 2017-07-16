import csv

#open the output doc as writable

ouput_csv = open("output.csv", "w")


# TODO: import CSV into lists
#turns csvs into lists of lists

with open('old.csv', 'rU') as f:
    reader = csv.reader(f)
    old_csv_list = list(list(rec) for rec in csv.reader(f, delimiter=','))
    #removes the ordinals for each entry because they are not relevant
    for element in old_csv_list:
        del element[0]
    print(old_csv_list)

with open('new.csv', 'rU') as f:
    reader = csv.reader(f)
    new_csv_list = list(list(rec) for rec in csv.reader(f, delimiter=','))
    for element in new_csv_list:
        del element[0]
    print(new_csv_list)


# TODO: Compare new list to old list
# if element is not in old list, add to output list


#TODO: Format output with spaces

#TODO: output to CSV

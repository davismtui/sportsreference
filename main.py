import json

# library that converts an array of arrays into a printable matrix
from tabulate import tabulate

# list of all teams
list_of_teams = ['Tm']


# open JSON
with open('test.json') as f:
    original = json.load(f)


# find all teams
# iterate through the file and get the names of all the teams
# for key in JSON add it to an array
for team in original:
    list_of_teams.append(team)

# create the skeleton of the table:

head = list_of_teams
mydata = [

    head

]

# create a temporary  array for each row entry
temp_array = []

# initialize a counter in order to keep track of which columns need null values
count = 1

# The key is each team ID whos values are subkey's containing Win/Loss data.
for key in original:

    # add the key (team name) to its row that will be entered in the final matrix
    temp_array.append(key)

    # for each team that each "key" played against, add the wins to the row (temp array)
    for subkey in original[key]:
        temp_array.append(original[key][subkey]["W"])

    # insert null value into the row (temp array) based on which iteration we are on.
    # essentially, if we are on iteration 1, key/team BRO cannot play against itself. Add null val.
    temp_array.insert(count, "--")

    # increment the counter for the next
    count += 1

    # add row to the matrix
    mydata.append(temp_array) # adding array to matrix

    # clear array for outer loop
    temp_array = []

mydata.append(head)

print(tabulate(mydata))

# Sports Reference Engineering Prompt 
To run the program simply run the main.py file.

## Explaination
My goal was to replicate each row in the sample matrix, and then combine them all to reproduce that matrix.

The JSON file is a list of alphabetically arranged unique team keys that correspond to subkeys whose values are win-loss data.
Knowing this I iterated through each key and added it to an array called "list_of_teams" This list contains each unique team name. This is the head of the matrix to be built.
"mydata" is initialized as an array that will hold other arrays at each of its indices, i.e. a matrix.

From there, I initialized a temporary array called "temp_array." This array is going to be filled with the data of each row in the matrix.
I also initialized a counter to keep track of which columns need null values.

## Iterating
I looped through each key in the JSON file and added the win data for every subkey into the temporary array.

After adding all the win data to the temp array, the code inserts a null value into the temp array based on which iteration of the outer loop it is currently on.
For example, if it is on iteration 1 it will insert a null value into index 1 of the temporary array. "BRO" is the first key, and the first team at the head of the table a team cannot play itself.
The count is then incremented by 1 after the inner loop ends and the temporary array is added to the mydata array (matrix). 
The temp array is then cleared for the next iteration of the outer loop.

After the outer loop is finished, mydata is complete. I used the tabulate library to make the data more presentable in a printable format.

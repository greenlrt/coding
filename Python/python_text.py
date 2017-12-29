# This program writes into a text file.

# Open text file python_text.rtf in writing mode.
my_file = open("python_text.rtf", "w")

# Delete any data and write the following in the text file.
my_file.write("This is some python text.\n")

# Close the text file.
my_file.close()

# Open the text file in reading mode.
my_file = open("python_text.rtf", "r")

# Print the first line of the text file.
print(my_file.readline())

# Close the text file.
my_file.close()

# Open the text file in appending mode.
my_file = open("python_text.rtf", "a")

# Add the following line to the end of the text file.
my_file.write("This is another line.\n")

# Close the text file.
my_file.close()

# Open the text file in reading mode.
my_file = open("python_text.rtf", "r")

# Print all of the text file.
print(my_file.read())

# Close the text file.
my_file.close()

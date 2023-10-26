# Prompt the user to enter the name of a file
nswr = input("File name: ")

# Make the the file's name lowercase
file_name = nswr.replace(" ", "").lower()

ext = file_name.split(".")
print(ext[1])
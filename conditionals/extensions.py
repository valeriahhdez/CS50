'''
This program prompts the user for the name of a file. 
It outputs the file media type if the file name ends in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
The program is case- and space-insensitive.
If the file has a suffix not contained in the list or has no suffix at all, the program prints the default media type
'''

# Prompt the user to enter the name of a file
nswr = input("File name: ")

# Make the the file's name lowercase
file_name = nswr.replace(" ", "").lower()


# # List of suffixes
my_list = ['.jpg', '.jpeg', '.gif', '.png', '.pdf', '.zip','.txt']


# # Check if the suffix of the file is contained in the list
# # print the media type if TRUE, otherwise 'application/octet-stream'

# Get the index and value of every item of my_list 
for i, val in enumerate(my_list):
    # Check if file_name suffix is contained in my_list
    if file_name.endswith(my_list[i]):
        # If so, check if the media file is jpeg
        if my_list[i] in my_list[0:2]:
            # If so, print 'image' as the media type
            print("image/jpeg")
        # check if the file_name suffix is .png or .gif
        elif my_list[i] in my_list[2:4]:
            # If so, print 'image' as the media type
            print("image/" + my_list[i].replace(".",""))
        # Check if the file is the 4th item of my_list
        elif my_list[i] in my_list[4:6]:
            # Print 'application' as the media type
            print("application/" + my_list[i].replace(".",""))
        else:
            # Print 'text/plain' as the media type
            print("text/plain")
        break
    # If suffix is not contained in my_list or file_name has no suffix at all, print the default media type
else:
    print("application/octet-stream") 




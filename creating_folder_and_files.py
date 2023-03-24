import os

# Getting the current working directory
dir = os.getcwd()
print("Your Current working directory is {dir}")


# Creating a requirements file for installation of all the dependencies

requirements = "requirements.txt"
if os.path.exists(dir):
    open(requirements, 'a').close()
    print(f"{requirements} created successfully")
else:
    print(f"{requirements} already exists")


# Create a FOLDER 
if not os.path.exists(dir):
    os.mkdir("Data")
    print("Data folder already exists")
elif not os.path.exists(dir):
    os.mkdir("SCR")
    print("SCR folder already exists")
elif not os.path.exists(dir):
    os.mkdir("Data Frames")
else:
    print("Folder exists: {dir}")

# Change the current working directory
change_working_directory = os.chdir("SCR")
print("Directory changed {change_working_directory}")

# List of file names to create
file_names = ["convert_video_to_frame.py", "main.py"]

# Loop over file names and create files
for file_name in file_names:
    if not os.path.exists(file_name):
        open(file_name, 'a').close()
        print(f"{file_name} created successfully")
    else:
        print(f"{file_name} already exists")


import shutil
import zipfile
import os
from os.path import basename
import config
import datetime


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


if config.folder["folderName"] == "" or config.destination["directoryName"] == "":
    print(bcolors.FAIL + "config.py has not been configured!")
    print(
        bcolors.WARNING
        + "Make sure that 'folderName' and 'directoryName' have values in the config.py file!"
    )
    exit()

# Find all file paths within the specified directory and its subdirectories
def retrieve_file_paths(dirName):
    # Get the directory where the script is stored
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Change to the directory containing the script
    os.chdir(script_dir)
    filePaths = []

    for root, dirs, files in os.walk(dirName):
        for filename in files:
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)

    return filePaths


folder = config.folder["folderName"]
destination = config.destination["directoryName"]
dateTimeObj = datetime.datetime.now()
now = dateTimeObj.strftime("%d%b%Y-%H%M%S")
ziparchive = config.folder["folderName"] + now + ".zip"
filePaths = retrieve_file_paths(config.folder["folderName"])

print(
    bcolors.HEADER
    + "[+] "
    + bcolors.ENDC
    + "Duplicating "
    + bcolors.BOLD
    + folder
    + bcolors.ENDC
    + "..."
)
for fileName in filePaths:
    print(fileName)

print("")
zip_file = zipfile.ZipFile(ziparchive, "w")
with zip_file:
    for file in filePaths:
        zip_file.write(file)

print(
    bcolors.OKGREEN
    + "[+] "
    + bcolors.ENDC
    + bcolors.BOLD
    + ziparchive
    + bcolors.ENDC
    + " has been created successfully!"
)

print("")
print(
    bcolors.OKGREEN
    + "[+] "
    + bcolors.ENDC
    + "Moving "
    + bcolors.BOLD
    + ziparchive
    + bcolors.ENDC
    + " to the directory: "
    + bcolors.BOLD
    + destination
    + bcolors.ENDC
)
shutil.move(ziparchive, destination + ziparchive)
print(bcolors.OKCYAN + "[+] " + bcolors.OKGREEN + "Moved successfully!")

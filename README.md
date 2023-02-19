# WorldZipper
World Zipper is a simple Python script designed to backup your server game world (Minecraft, Terraria, etc.) by creating a compressed archive of your world and moving 
it to a specified directory. It can be used either by manually calling it in the terminal or by setting it up to run periodically through 
automation tools like cron on Linux or the Task Scheduler on Windows.

# Getting Started
1. Clone the repository or download the script.
2. **Move both the config and worldzipper file in the same directory as your world directory**
3. Navigate to the directory containing the script in your terminal or command prompt.
4. Open the config.py file and specify the name of the folder containing your game world, and the directory where you want the backup archive to be saved.
5. Run the script by typing python worldzipper.py in your terminal or command prompt.
6. If everything is set up correctly, WorldZipper will create a compressed archive of your game world, and move it to the specified directory on your computer.

# Using WorldZipper in Automation
WorldZipper can be used in automation to backup your game world on a regular basis. On Linux systems, you can use cron to schedule the script to run at specific intervals.

Here's how to set up WorldZipper to run automatically using cron on Linux:

Open a terminal window and type `crontab -e` to edit the cron configuration file.

In the editor, add a new line to schedule the script to run at the desired interval. For example, to run the script every day at 2am, you would add the following line:

`0 2 * * * /usr/bin/python /path/to/worldzipper.py`\
This line tells cron to run the script at minute 0, hour 2, every day of the month, every month, every day of the week.

Note: Be sure to update the file paths in the cron command to match the location of the World Zipper script on your system, and make sure that the script is executable (chmod +x worldzipper.py).

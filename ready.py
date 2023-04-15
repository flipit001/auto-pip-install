import os
start = input("BEFORE WE START THIS PROGRAM, SOME PIP LIBRARIES ARE GOING TO BE INSTALLED WHICH ARE GOOGLE AND BEAUTIFULSOUP, IS THAT OK?(y/n)")
if start.lower() == "y":
    os.system("pip install --no-input beautifulsoup4")
    os.system("pip install --no-input google")
print("you are now ready to run main.py")


from bs4 import BeautifulSoup
import urllib.request
import os
import requests
from googlesearch import search
import re

PATH = input("what python file you want this computer to scan and download the packages?: ")
#print("DEBUG1")


def getHTMLdocument(url):
    response = requests.get(url)
      
    return response.text

command = None
soup = None
Link = None
downloads = []
#print("DEBUG2")
with open(PATH, "r") as f:
    for line in f.read().split("\n"):
        line = ''.join(line)
        if line.split(" ")[0] == "import":
            downloads.append(line.split(" ")[1])
#print("DEBUG3")
for download in downloads:
    Link = [j for j in search(f"{download} python library", tld="co.in", num=20, stop=20, pause=2) if "https://pypi.org/project/" in j][0] #idk for some reason it works like this but it does not work when doing normally without the list
    if Link:
        soup = BeautifulSoup(getHTMLdocument(Link), features="html.parser")
        command = soup.find('span', id="pip-command")
        yes = input(f"do you want to run the command '{command.text}'? (y/n): ")
        if yes.lower() == "y":
            os.system(command.text)
        else:
            print("ok next")
    else:
        print(f"could not find package: {download} on pypi")

print("done!")



    
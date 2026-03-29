import os
import sysrsync
import subprocess

from datetime import datetime

syncDir = "/home/blau/sharedfs/plasma/GoodNotes/"

vaultDir = "/home/blau/Documents/Vault/Vault/Imports/"

baseDir = "/home/blau/Documents/Vault/Vault"

lazyBaseDir = "/home/blau/Documents/Vault/Vault/20 - Education/21 - College/"

mappings = {"QF106":f"{baseDir}/20 - Education/21 - College/21.3 Semester 3/21.3.70 QF 106",
            "MA126":f"{baseDir}/20 - Education/21 - College/21.3 Semester 3/21.3.45 MA 126",
            "CS115":f"{baseDir}/20 - Education/21 - College/21.3 Semester 3/21.3.10 CS 115",
            "FIN321":f"{baseDir}/20 - Education/21 - College/21.3 Semester 3/21.3.20 FIN 321",
            "QF101":f"{baseDir}/20 - Education/21 - College/21.3 Semester 3/21.3.60 QF 101",
            "General School":f"{baseDir}/20 - Education/21 - College/21.3 Semester 3",
            "Journal":f"{baseDir}/30 - Journal",
	    "Chem":f"{baseDir}/20 - Education/21 - College/Winter 2025/Chem",
        "MA232":f"{lazyBaseDir}/Semester 5/MA232",
        "MA222":f"{lazyBaseDir}/Semester 5/MA222",
        "CS135":f"{lazyBaseDir}/Semester 5/CS135",
	"CS284":f"{lazyBaseDir}/Semester 5/CS284",
            }


dateStr = datetime.today().strftime("%Y-%m-%d")

def getTemplate():
    templateFile = open("test.md","r")
    templateContents = templateFile.read()
    return templateContents



template = getTemplate()


def dryRun():
    dry_cmd = [
    "rsync", "-an", "--itemize-changes", "--out-format=%n", syncDir, vaultDir
]
    dry = subprocess.run(dry_cmd, stdout=subprocess.PIPE, text=True)
    to_sync = dry.stdout.splitlines() 

    return to_sync[1:]

def populateVault():
    updateList = dryRun()

    filteredList = list(filter(lambda x: x[-4:] == ".pdf", updateList))

    for i in filteredList:
        x = i.split("/")
        dir = x[0]
        fileName = x[1]

        fNameAdjusted = f"Imports/{dir}/{fileName}"
        currentContent = template.format(fname=fNameAdjusted, date=dateStr, subject=dir)
        #debug
        print(mappings[dir] + "/" + f"{fileName[:-4]}.md")
        try:
            file = open(mappings[dir] + "/" + f"{fileName[:-4]}.md","x")
            file.write(currentContent)
            file.close()
        except:
            pass


def main():
    populateVault()
    sysrsync.run(source=syncDir,destination=vaultDir,options=['-rtuv'])


main()

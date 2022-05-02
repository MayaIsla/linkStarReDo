import os
from datetime import datetime
import shutil
import webbrowser
import subprocess
import time

now = datetime.now()
date = now.strftime("%m%d%y")
serverOne = "https://dudesweet.com/"
serverTwo = "https://sweetdude.com/"
webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser('C:/Program Files/Google/Chrome/Application/chrome.exe'))
src_path = r"D:/Desktop/File.txt"
dst_path = r"D:/Desktop/Test Folder" + date
dst_path2 = r"D:/Desktop/Test Folder"
sessionXML = r"C:/Users/Mayaaaaugh/AppData/Roaming/Notepad++/session.xml"
exampleFile = r"D:/Desktop/Notepad"
newFolder = r'D:/Desktop/folder'
newnewFolder = os.makedirs(newFolder + " " + date, mode=0o777, exist_ok=True)
propertiesLink = r"C:\linkstar\html-service.properties"


def menu():
    print("[1] Manual backup... Copy all .jar Only")
    print("[2] Update the Messages and HTML-Service.properties")
    print("[3] Start and Stop the Services Only")
    print("[4] **Starting the Complete Linkstar Job**")
    print("[5] Check two websites for connectivity")
    print("[6] Rollback Procedure #1 - Issues found!")
    print("[7] Logoff Server - WAB-LKRPW01 -SC -Sparce-2 replacement //WAB-LKRPW01")
    print("[8] Rollback Procedure #2 - Back to the First Original Update!")
    print("[9] Shutdown and Restart this Server (Other Failures)")
    print("[0] Exit the Program")


menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        # do option 1 stuff
        print("Option 1 has been called")
        print("Copying files over...")
        # shutil.copy(src_path, newnewFolder)
        os.system("xcopy C:/Linkstar/linkstar.jar 'C:/Backups/Linkstar BU' /Q /S /Y")
        print('Copied')
        print("File copy completed")

    elif option == 2:
        print("Killing program 1..")
        # os.system("TASKKILL /F /IM notepad.exe")  # net stop not working in this environment(Linkstar)
        print("Killing program 2...")
        # os.system("TASKKILL /F /IM cmd.exe")
        os.system("net stop Linkstar")
        os.system("net stop linkstar-pdf")
        os.system("net stop watchman")
        time.sleep(3)
        # os.remove(sessionXML)
        os.system("start notepad++" + propertiesLink)
        time.sleep(3)

        os.system("net start Linkstar")
        os.system("net start Linkstar-pdf")
        os.system("net stop watchman")

        print("Option 2 has been called")

    elif option == 3:

        os.system("net stop Linkstar")
        os.system("net stop Linkstar-PDF")
        os.system("net stop watchman")

        time.sleep(15)

        os.system("net start Linkstar")
        os.system("net start Linkstar-PDF")
        os.system("net start watchman")

        time.sleep(3)
        print("Option 3 has been called")


    elif option == 4:
        os.system("xcopy 'c:\Linkstar\Linkstar.jar' 'C:\Backups\Linkstar BU' /Q /S/Y")
        os.system("xcopy 'c:\Linkstar\Linkstar-reporting.jar' 'C:\Backups\Linkstar BU' /Q /S/Y")
        print("Completed the backup of Jar files")

        time.sleep(3)

        os.system("net stop Linkstar")
        os.system("net stop Linkstar-PDF")
        os.system("net stop watchman")

        time.sleep(3)
        os.system("xcopy 'c:\Mig\LinkStar-Code\linkstar.jar' 'C:\Linkstar' /Q /S/Y")
        os.system("xcopy 'c:\Mig\LinkStar-Code\linkstar-reporting.jar' 'C:\Linkstar' /Q /S/Y")

        time.sleep(3)

        os.system("%windir\explorer.exe 'c:\Mig")
        os.remove(sessionXML)
        os.system("start notepad++" + propertiesLink)

        os.system("net start Linkstar")
        os.system("net start Linkstar-PDF")
        os.system("net start watchman")
        print("Option 4 has been called")

    elif option == 5:
        webbrowser.get('chrome').open(serverOne)
        time.sleep(2)
        webbrowser.get('chrome').open(serverTwo)
        time.sleep(2)
        print("Option 5 has been called")

    elif option == 6:
        os.system("net start Linkstar")
        os.system("net start Linkstar-PDF")
        os.system("net start watchman")

        time.sleep(10)

        os.system("xcopy 'c:\Linkstar\Linkstar.jar' 'C:\Backups\Linkstar BU' /Q /S/Y")
        os.system("xcopy 'c:\Linkstar\Linkstar-reporting.jar' 'C:\Backups\Linkstar BU' /Q /S/Y")
        print("Completed the backup of Jar files")

        os.system("xcopy 'c:\Backups\Linkstar BUI' C:\Linkstar\*")

        os.system("net start Linkstar")
        os.system("net start Linkstar-PDF")
        os.system("net start watchman")

        print("Option 6 has been called")

    elif option == 7:
        yesOrNo = input("Are you sure you want to logoff server?[y/n]")
        if yesOrNo == "y":
            os.system("'%lgoffid%' /server:wab-lkrpw01")
        elif yesOrNo == "n":
            exit()
        else:
            print("Answer not valid")

        print("Option 7 has been called")

    elif option == 8:
        os.system("net start Linkstar")
        os.system("net start Linkstar-PDF")
        os.system("net start watchman")

        os.system("xcopy 'c:\Linkstar\Linkstar.jar' 'C:\Backups\Linkstar BU' /Q /S/Y")
        os.system("xcopy 'c:\Linkstar\Linkstar-reporting.jar' 'C:\Backups\Linkstar BU' /Q /S/Y")
        print("Completed the backup of Jar files")

        time.sleep(5)

        os.system("xcopy 'c:\Backups\Linkstar BUI' C:\Linkstar\*")

        os.system("net start Linkstar")
        os.system("net start Linkstar-PDF")
        os.system("net start watchman")

        print("Option 8 has been called")

    elif option == 9:
        question = input("Are you sure you want to shutdown the server?[y/n]")
        if question == "y":
            os.system("shutdown /r /m \wab-lkrpw01 /t 60 /d u:0:5")
        elif question == "n":
            exit()
        else:
            print("Answer not valid")
        print("Option 9 has been called")

    else:
        print("Invalid Option")
    print()
    menu()
    option = int(input("Enter your option:"))
print("Microsoft OS Windows Server WAB-LKRPW01")

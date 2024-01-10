import os

def isExceptDirs(root, exceptDirectorys):
    if root.replace(".\\", "") in  exceptDirectorys:
        print("Found a directory you don't want: ", root)
        return True
    return False

def isFoundFileException(file, fileExtensions):
    for fileExtension in fileExtensions:
        if file.endswith(fileExtension):
            return True
    return False
    
def copyFile(sourceFile, destinationFile):
    with open(sourceFile, 'rb') as source:
        #read data
        data = source.read()

        #write data
        with open(destinationFile, 'wb') as destination:
            destination.write(data)

def deleteFileExtension(fileExtensions, exceptDirectorys, yourPath='.'): # yourPath='.' is root path
    try: 
        for (root, dirs, files) in os.walk(yourPath, topdown=True):
            # print('root', root)
            # print('dirs', dirs)
            # print('file', files)

            #except directory 
            if exceptDirectorys:
                if isExceptDirs(root, exceptDirectorys):
                    continue

            # delete file extension  
            for file in files:
                if isFoundFileException(file, fileExtensions):
                    os.remove(f"{root}\{file}")
                    print(f'Remove file: {root}\{file}')

    except Exception as e:
        print(e)
    
def cutOrCopyExtensions(yourPath, destinationPath, mode, fileExtensions, exceptDirectorys):
    try: 
        for (root, dirs, files) in os.walk(yourPath, topdown=True):
            # print('root', root)
            # print('dirs', dirs)
            # print('file', files)

            #except directory 
            if exceptDirectorys:
                if isExceptDirs(root, exceptDirectorys):
                    continue

            # check files extension
            for file in files:
                if isFoundFileException(file, fileExtensions):
                    sourceFile = f'{root}\{file}'      
                    destinationFile = f'{destinationPath}\{file}'
                    copyFile(sourceFile, destinationFile) #copy file to destionation
                    print(sourceFile, 'finished')
                    if mode == 2: # 2 is cut mode but 1 copy mode 
                        os.remove(sourceFile)     

    except Exception as e:
        print(e)

def commandLineInterface():
    selectMode = """
          _____      _                 _             _____ _ _      
         | ____|_  _| |_ ___ _ __  ___(_) ___  _ __ |  ___(_) | ___ 
         |  _| \ \/ / __/ _ \ '_ \/ __| |/ _ \| '_ \| |_  | | |/ _ \\
         | |___ >  <| ||  __/ | | \__ \ | (_) | | | |  _| | | |  __/
         |_____/_/\_\\__\___|_| |_|___/_|\___/|_| |_|_|   |_|_|\___|
                                    Created by Sutthirak Sutsaenya

    ░█▀█░█░░░█▀▀░█▀█░█▀▀░█▀▀░░░█▀▀░█▀▀░█░░░█▀▀░█▀▀░▀█▀░░░█▄█░█▀█░█▀▄░█▀▀
    ░█▀▀░█░░░█▀▀░█▀█░▀▀█░█▀▀░░░▀▀█░█▀▀░█░░░█▀▀░█░░░░█░░░░█░█░█░█░█░█░█▀▀
    ░▀░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░░░▀░▀░▀▀▀░▀▀░░▀▀▀                                     

         Please select mode  

            1 DeleteExtentions  ==>
            2 CutExtentions     ==>
            3 CopyExtentions    ==>
    """
    return selectMode

def main():

    while True:
        gui = commandLineInterface()        
        print(gui)

        numberMode = int(input('         Number: '))
        if numberMode == 1:

            inputYourPath = input('         Path to search: ')
            inputFileExtensions = [x for x in input('         Extension to delete: ').split()] 
            inputExcepDirectorys = [x for x in input('         Directory to exclude: ').split()]

            print(inputYourPath)
            print(inputFileExtensions)
            print(inputExcepDirectorys)

            deleteFileExtension(fileExtensions=inputFileExtensions, yourPath=inputYourPath, exceptDirectorys=inputExcepDirectorys)

        elif numberMode == 2: #cut mode

            inputYourPath = input('         Path to search: ')
            inputDestinationPath = input('         Destination path to save file: ')
            inputFileExtensions = input('         Extension to cut: ')
            inputExcepDirectorys = input('         Directory to exclude: ')
            
            cutOrCopyExtensions(yourPath=inputYourPath, destinationPath=inputDestinationPath, 
                                fileExtensions=inputFileExtensions, exceptDirectorys=inputExcepDirectorys,
                                mode=2
                                )

        elif numberMode == 3: #copy mode
            inputYourPath = input('         Path to search: ')
            inputDestinationPath = input('         Destination path to save file: ')
            inputFileExtensions = input('         Extension to copy: ')
            inputExcepDirectorys = input('         Directory to exclude: ')
            
            cutOrCopyExtensions(yourPath=inputYourPath, destinationPath=inputDestinationPath, 
                                fileExtensions=inputFileExtensions, exceptDirectorys=inputExcepDirectorys,
                                mode=1
                                )

if __name__ == '__main__':
    main()













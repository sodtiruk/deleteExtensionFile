import os
import sys
import argparse

def deleteFileExtension(yourPath, fileExtensions, exceptDirectorys):
    try: 
        for (root, dirs, files) in os.walk(yourPath, topdown=True):
            # print('root', root)
            # print('dirs', dirs)
            # print('file', files)

            #except directory 
            if root.replace(".\\", "") in exceptDirectorys:
                print("Found a directory you don't want: ", root) 
                continue

            # check files extension
            for file in files:
                for fileExtension in fileExtensions:                        
                    if file.endswith(fileExtension):
                        os.remove(f"{root}\{file}")
                        print(f'Remove file: {root}/{file}')

    except Exception as e:
        print(e)

def main():

    if len(sys.argv) < 2:
        print("python main.py -r rootpath -fe .txt .jpg -d dir_a dir_b")
        return

    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--rootPath', type=str, default='.', required=False) 
    parser.add_argument('-fe', '--fileExtension', nargs='+', metavar='extension')
    parser.add_argument('-e', '--directoryException', nargs='+', metavar='extension', default=[])
    args = parser.parse_args()

    rootPath = args.rootPath
    fileExtension = args.fileExtension
    directoryException = args.directoryException

    # print(rootPath) 
    # print(fileExtension)
    # print(directoryException)

    deleteFileExtension(yourPath=rootPath, fileExtensions=fileExtension, exceptDirectorys=directoryException)

if __name__ == '__main__':
    main()













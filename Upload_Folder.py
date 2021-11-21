import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
   
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    
                localpath = os.path.join(root, filename)

                    
                relative_path = os.path.relpath(localpath, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = ''
    transferData = TransferData(access_token)

    file_from = input("Enter the folder source  "))
    file_to = input("enter the source dropbox")  

    
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()
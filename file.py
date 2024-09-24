import requests

def download_file(url,file_name):
    response = requests.get(url)
    
    if response.status_code ==200:
        with open(file_name , "wb") as file:
            print(f"File ' {file_name}' downlaod successful ")
            
    else:
        print(f"failed to download file .status code ")
        
if __name__ == "__main__":
    url = "https://github.com/upessocs/B1B2/blob/main/fileOrganizerGui/Organizer.zip"
    file_name = "file.zip"
    download_file(url, file_name)


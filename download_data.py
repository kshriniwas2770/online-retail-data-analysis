import requests
import zipfile
import io
import os

def download_and_extract(url, extract_to='data/'):
    target_file_name = 'Online Retail.xlsx'
    
    file_path = os.path.join(extract_to, target_file_name)

    # check if the file already exists, if yes skip downloading
    if os.path.exists(file_path):
        print(f"Data set already exists: {file_path} \nSkipping downloading")
        return os.path.abspath(file_path)
        
    print(f"Starting download from: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Download successful. Extracting...")
        
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            # extract to the directory
            zip_ref.extractall(extract_to)
            
        print(f"Files extracted successfully to: {os.path.abspath(extract_to)}")
        return os.path.abspath(extract_to)
    else:
        print(f"Failed to download. Status code: {response.status_code}")
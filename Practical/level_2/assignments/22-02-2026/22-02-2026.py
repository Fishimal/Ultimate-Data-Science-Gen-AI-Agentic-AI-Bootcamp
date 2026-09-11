import requests, os


class DownloadDataset:
    def __init__(self):
        pass


    def download_dataset(self, url, path):
        response = requests.get(url)
        file_contents = response.content

        with open(path, 'wb') as f:
            f.write(file_contents)

        
if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv'
    current_directory = os.getcwd()
    sub_folder_name = 'data'
    data_folder_path = os.path.join(current_directory, sub_folder_name)
    os.makedirs(data_folder_path, exist_ok=True)
    file_name = 'titanic_dataset.csv'

    obj = DownloadDataset()
    path = os.path.join(data_folder_path, file_name)
    obj.download_dataset(url, path)

    print('File has been downloaded successfully')
import os

print('Try except block started.')
try:
    folder_name = 'temp'
    file_name = 'temp_2.txt'
    file_path = os.path.join(folder_name, file_name)
    num = 0

    with open(file_path, 'r+') as f:
        contents = f.read()
        print(contents)
    
    cal = (100 / num)       # infinity, not divisible

except FileNotFoundError:
    print('File not found: Please check for correct file name or path.')
    print(os.getcwd())
    print(f'Files present in the specified directory: {os.listdir(os.path.join(os.getcwd(), folder_name))}')
    print(f'File name selected: {file_path}')

except TypeError:
    print('Issue with multiple type operation.')

except Exception as e:
    print(f'Caught in parent exception: {str(e).title()}')


print('Try except block completed.')

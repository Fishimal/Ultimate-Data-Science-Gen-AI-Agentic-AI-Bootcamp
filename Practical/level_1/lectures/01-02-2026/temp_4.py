import os

print('Try except block started.')
try:
    folder_name = 'temp'
    file_name = 'temp_2.txt'
    file_path = os.path.join(folder_name, file_name)
    num = 0

    f = open(file_path, 'r+')
    contents = f.read()
    print(contents)
    
    if (num == 0):
        # raise Exception('our own exception description.')
        raise ZeroDivisionError('You have passed 0 in the denominator which will result in ZeroDivisionError.')
    cal = (100 / num)
    print(cal)

except FileNotFoundError:
    print('File not found: Please check for correct file name or path.')
    print(os.getcwd())
    print(f'Files present in the specified directory: {os.listdir(os.path.join(os.getcwd(), folder_name))}')
    print(f'File name selected: {file_path}')

except TypeError:
    print('Issue with multiple type operation.')

except ZeroDivisionError as z:
    print(f'Issue with arithmetic operation: {z}')

except Exception as e:
    print(f'Caught in parent exception: {str(e).title()}')

else:
    print('Try block got executed successfully.')

finally:
    try:
        f.close()
        print('File is closed.')
    except NameError:
        print('File was never initialised.')


print('Try except block completed.')
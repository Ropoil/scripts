
import zipfile


def crack_password(password_list, obj):
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print(word.decode())

                except:
                    continue



password_list = "change to dictionary file path"

zip_file = "change to zip file path "

obj = zipfile.ZipFile(zip_file)

crack_password(password_list, obj)

obj.extractall()

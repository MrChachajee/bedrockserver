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
os.system("echo LD_LIBRARY_PATH=. ./bedrock_server > run.sh")
os.system("chmod +x ./run.sh")
os.system("nohup ./run.sh > server.out &")
time.sleep(5)


while True:
    result = open('server.out', 'r').read().find('Server started.')
    if result > -1:
        break

print("Ngrok starting... ")
os.system('ngrok tcp -region us 25565 &')
time.sleep(5)

os.system("curl ifconfig.me")

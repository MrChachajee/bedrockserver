import os, time

print("STARTING...")
print("Starting Web...")
os.system('heroku-php-apache2 &')

# os.system("host myip.opendns.com resolver1.opendns.com")
os.system("wget -q -O - https://raw.githubusercontent.com/pmmp/php-build-scripts/master/installer.sh | bash -s -")

time.sleep(5)

os.system("nohup ./start.sh --no-wizard > server.out &")

while True:
    time.sleep(10)
    result = open('server.out', 'r').read().find('Done')
    if result > -1:
        print("Started...")
        break

print("**script**: starting ngrok tcp")
os.system('ngrok tcp -region us 58035 &')


while True:
    result = open('server.out', 'r').read()
    print(result)
    time.sleep(30)


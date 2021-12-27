import os, time

print("STARTING...")
print("Starting Web...")
os.system('heroku-php-apache2 &')

# os.system("host myip.opendns.com resolver1.opendns.com")
os.system("wget -q -O - https://raw.githubusercontent.com/pmmp/php-build-scripts/master/installer.sh | bash -s -")

time.sleep(5)

os.system("./run.sh --no-wizard")

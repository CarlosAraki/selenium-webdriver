# selenium-webdriver
Using selenium for test webdriver

# Run docker-compose up 

# Req

apt update
apt install chromium-chromedriver
apt-get install -y libglib2.0-0=2.50.3-2 \
    libnss3=2:3.26.2-1.1+deb9u1 \
    libgconf-2-4=3.2.6-4+b1 \
    libfontconfig1=2.11.0-6.7+b1
apt-get install libnss3
gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

 wget https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip
 wget https://chromedriver.storage.googleapis.com/92.0.4515.43/chromedriver_linux64.zip
 unzip chromedriver_linux64.zip 
 chmod +x chromedriver
 mv -f chromedriver /usr/local/bin/chromedriver
 pip install pyvirtualdisplay
 pip install selenium  
 sudo apt-get install xvfb
pip install xvfbwrapper

#!/bin/bash
echo Installing python requirements...
pip install -r ./requirements.txt
sudo apt install python3-pyqt5
echo 'Installed python requirements!'
echo Creating desktop shortcut...
echo '#!/bin/bash' >> ~/Desktop/start.sh
echo "cd ~/SmartPET-Feeder/raspberry_pi/src" >> ~/Desktop/start.sh
echo "python ./start.py &" >> ~/Desktop/start.sh
chmod 777 ~/Desktop/start.sh
echo Created desktop shortcut.
echo "Creating database at ~/smartpet.db..."
cd ~
sqlite3 smartpet.db < ./SmartPET-Feeder/raspberry_pi/smartpet.sql
if [ $? != 0 ] 
then
echo Install failed.
exit 1
fi
echo Install successfully completed.

#!/bin/bash
echo Installing python requirements...
pip install -r ./requirements.txt
sudo apt install python3-pyqt5
echo Installed python requirements!
echo Creating desktop shortcut...
echo Enter your host ip address:
read ip
echo "cd ~/SmartPET-Feeder/raspberry_pi/src" >> ~/Desktop/start.sh
echo "python ./ui.py &" >> ~/Desktop/start.sh
echo "python ./query.py &" >> ~/Desktop/start.sh
echo "python -m uvicorn web_api:app --reload --host $ip" >> ~/Desktop/start.sh
echo Created desktop shortcut.
echo "Creating database at ~/smartpet.db..."
cd ~
sqlite3 smartpet.db < smartpet.sql
if [ $? != 0 ] 
then
echo Install failed.
exit 1
fi
echo Install successfully completed.

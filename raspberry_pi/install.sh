echo Installing python requirements...
pip install -r ./raspberry_pi/requirements.txt
sudo apt install python3-pyqt5
echo Installed python requirements!
echo Creating desktop shortcut...
echo Enter your host ip address:
read ip
echo "cd ~/smartpet-feeder/raspberry_pi/src" >> ~/Desktop/start.sh
echo "python ./ui.py &" >> ~/Desktop/start.sh
echo "python ./query.py &" >> ~/Desktop/start.sh
echo "python -m uvicorn web_api:app --reload --host $ip"
echo Install successfully completed.

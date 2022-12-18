echo Installing python requirements...
pip3 install -r ./requirements.txt
echo Installed python requirements!
echo Creating desktop shortcut...
echo Enter your host ip address:
read ip
echo "cd ~/smartpet-feeder" >> ~/Desktop/start.sh
echo "python ./ui.py &" >> ~/Desktop/start.sh
echo "python ./query.py &" >> ~/Desktop/start.sh
echo "uvicorn web_api:app --reload --host $ip"
echo Install successfully completed.

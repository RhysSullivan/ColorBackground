sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt-get install python3-dev
sudo apt-get install python3-setuptools
sudo apt-get install python3-venv
sudo apt-get install build-essential libssl-dev libffi-dev 
sudo apt-get install nginx
python3 -m venv flaskappenv
source flaskappenv/bin/activate
pip install wheel
pip install flask
pip install uwsgi
pip install requests

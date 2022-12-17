sudo apt update
sudo apt upgrade -y
sudo apt install -y git python3 python3-dev python3-pip
sudo apt install -y build-essential libssl-dev libmysqlclient-dev

git clone https://github.com/innosoft-innoweb/innosoft-innoweb-1
cd innosoft-innoweb-1
sudo pip3 install -r requirements.txt

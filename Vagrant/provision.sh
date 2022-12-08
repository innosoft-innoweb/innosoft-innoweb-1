sudo apt update
sudo apt upgrade –y
sudo apt install -y git python3 python3-pip docker docker.io screen
sudo apt install default-libmysqlclient-dev
docker pull mysql:5.7
git clone https://github.com/innosoft-innoweb/innosoft-innoweb-1
cd innosoft-innoweb-1
pip3 install -r requirements.txt

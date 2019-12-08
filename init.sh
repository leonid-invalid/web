sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default.conf
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database stepik;"
sudo mysql -uroot -e "CREATE USER 'leonid'@'localhost' IDENTIFIED BY 'lomtik5455';"
sudo mysql -uroot -e "grant all privileges on stepik.* to 'leonid'@'localhost' with grant option;"
python3 ~/web/ask/manage.py migrate
sudo /etc/init.d/nginx restart
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application



Procedure after creating EC2 Server:

For installing and checking postgresql:
=========================================
---Updating installer package
sudo dnf update -y

---Installing Postgresql
sudo dnf install -y postgresql15-server postgresql15

---Initializing Postgresql DB
sudo postgresql-setup initdb

---Starting Postresql service
sudo sysytemctl start postgresql

---Enabling Postgresql service
sudo systemctl enable postgresql

---Switching to postgres user
sudo -i -u postgres

---opening psql console
psql

---Alter postgres root password
ALTER USER postgres PASSWORD 'Welcome@123';

---Alter config file to listen from all addresses
vi /var/lib/pgsql/data/postgresql.b3
'' ---> set listen_addresses to '*'

---Alter config file to add port
vi /var/lib/pgsql/data/postgresql.conf ----> set port to 5432

---Alter hba config file to accept all hosts
vi /var/lib/pgsql/data/pg_hba.conf  -----> add this line to last - host all all 0.0.0.0/0 md5

---add 5432 port to security group inbound rules

---Restarting Postgresql
sudo systemctl restart postgresql

---Check if postgres is connecting ouside server
Connect in pgadmin with public ipv4 address (54.166.207.117) and postgres password (Welcome@123)




For installing and checking python:
=====================================

---Check python version
python3 --version

---Install pip package installer
sudo dnf install python3-pip -y

---Check pip version
pip3 --version

---Install postgresql connector for python
sudo dnf install python3-psycopg2 -y

---Install logger
pip3 install logger

---Install flask for web applications
pip3 install flask

---Install requests to fetch requests
pip3 install requests

---Install flask CORS
pip3 install flask_cors

---Install gunicorn server to deploy python application
pip3 install gunicorn







# flask-mongo-test
Test environment: Ubuntu 16.04

### install python and pip
	sudo apt install python3
	sudo apt install pip3

### install mongodb
	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
	sudo apt install mongodb-org
	
### install git
	sudo apt install git

### clone this repository
	git clone https://github.com/asulikeit/flask-mongo-test.git

### install python libraries
	pip3 install virtualenv
	virtualenv -p python3 venv
	
	pip3 install -r requirements.txt
	
### run python server
	source venv/bin/activate
	cd flask-mongo-test
	python3 main.py
	
### curl test
	curl -X POST "http://192.168.0.199:5000/pdf/home/daniel/flask/korean.rdf"
	curl "http://192.168.0.199:5000/pdf/home/daniel/flask/korean.rdf"
	curl -X POST "http://192.168.0.199:5000/doc/home/daniel/flask/korean.docx"
	
### Reference
	https://asulikeit.gitbooks.io/developer/content/chapter1/tika-environment.html

# Flask Experiment 
This is a simple web application developed by Flask and it doesn't follow any design architecture. It is required to get performance results for an experiment conducted for a research purposes. 

## Technologies used 
1. Python 
2. Flask
3. SQLite
4. HTML
5. CSS 
6. Flask Debug Toolbar 

## Prerequisites 
1. Download and install Python on your local machine. [Python](https://www.python.org/downloads/)
2. Download and install pip on your local machine. [pip](https://pip.pypa.io/en/stable/installing/)
3. Install **virtualenv** using pip. 
4. Create a folder and download or clone this project to the created folder. 

##### Inside the folder you created, run the following commands:
1. `virtualenv -p python .` to create a virtual environment for the project.
2. `.\Scripts\activate` to activate the virtual environment (This command is for Windows users)
3. `pip install Flask` to install Django in your virtual environment.
4. `pip install flask-debugtoolbar` to install Django debug toolbar in your virtual environment. 

Open the file `application.py` and set your secret key to config the debug toolbar. 

###### Then navigate to the project folder and run the following command:
1. `python database_setup.py`
2. `set FLASK_APP=application.py`
3. `python -m flask run`

Now the project is running in your local host [http://127.0.0.1:5000/](http://127.0.0.1:5000/) along with the Flask debug toolbar.
# Skgt Repo

## Chapter I.

### Exams REST/API:
##### Functionalities:
- addition, edition, deletion of exam sheets by the owner;
- defining the appropriate permissions for the owner and a normal user for individual resources or actions;
- possibility for the exam owner to assess each task, assign points for it and a final grade for the entire exam;
- exam sheets filtering e.g. by users/owners, scores, etc.

##### Technical:
- API written in Python, Django REST Framework.
- The interface by embedded Browsable API.
- To manage this repo was used Git Flow.
- All needed additional libraries for pip are in a separate file requirements.txt in app folder.
- Fixtures necessary to fill the database are in dump file in app folder.
- Clean code and structure is on the highest possible level (for me ;)

### Usage:

##### Test server:
[Exams REST/API](http://radek.me.uk/api/exams/)
- To work with API on test server use login: radek, pass: restapipass

##### Endpoints:
- [api/exams](http://radek.me.uk/api/exams/) - List of exams in db;
- [api/exams/1](http://radek.me.uk/api/exams/1/) - Details about exam id=1;
- [pi/exams/1/tasks](http://radek.me.uk/api/exams/1/tasks/) - List of tasks in exam id=1;
- [api/exams/1/tasks/3](http://radek.me.uk/api/exams/1/tasks/3/) - Details about task id=3 (exam 1; task id independent of the exam number);
- [api-auth/login](http://radek.me.uk/api-auth/login/) - Login;
- [api-auth/logout](http://radek.me.uk/api-auth/logout/) - Logout.

##### Exams filtering :
- api/exams/?ordering=<option> - where options are:
* owner/-owner - by owner ascending/descending;
* final_grade/-final_grade - by final grade ascending/descending;
* date/-date - by date ascending/descending;
* title/-title - by title ascending/descending.
  
##### Access rights:
- showing exams and task: everyone/standard users and logged users;
- creating new exams and tasks - only logged users;
- editing and deleting exams and tasks - only for exams owners.


### Launching:
You can launch API at least in 3 ways:
1. Prepared Bash script.
2. Docker.
3. Needlework.

---

##### 1. Prepared Bash script (designed for Linux):
- From main API folder you can download only file [install.sh](CHAPTER_I/Exams_REST_API/install.sh) or [install_full.sh](CHAPTER_I/Exams_REST_API/install_full.sh);
- If you are a little bit more advanced user I assume that you have already installed Python3, Git, Virtualenv and PostgreSQL. If it is take [install.sh](CHAPTER_I/Exams_REST_API/install.sh) file;
- If you are beginner [install_full.sh](CHAPTER_I/Exams_REST_API/install_full.sh) should help;
- After download this is needed to give the file permissions to execute by entering the command:
- 'sudo chmod 777 ./install.sh' or 'sudo chmod 777 ./install_full.sh'
- Run the file with command: './install.sh' or './install_full.sh'
- After all instructions will be completed Exams REST/API will be running in local mode.
* To work with API in local mode after pg_dump import use login: radek, pass: qwerasdf

##### 2. Docker:
- Pull this repo;
- In main API folder there are files: [Dockerfile](CHAPTER_I/Exams_REST_API/Dockerfile) and [docker-compose.yml](CHAPTER_I/Exams_REST_API/docker-compose.yml);
- Before the run files you can pull image: https://hub.docker.com/r/rbartosinski/exam_rest_api 
- Change two DATABASE SETTINGS in Exams_REST_API/settings.py (prepared to Bash script):
- 'NAME': 'exams_rest_db', -> 'NAME': 'postgres',
- 'HOST': 'localhost', -> 'HOST': 'db',
- In API folder run commands:
- docker-compose run web python manage.py createsuperuser
- docker-compose up

##### 3. Needlework:
- If you want to do this you can manually pull this repo (git clone https://github.com/rbartosinski/skgt-repo.git);
- Create Virtualenv (python3 -m venv myvenv; source myvenv/bin/activate);
- Install all requirements (pip install -r requirements.txt);
- Create and import the database (psql postgres -c "CREATE DATABASE exams_rest_db WITH ENCODING 'UTF8'"; psql exams_rest_db < pg_dump);
- Run REST/API server (python manage.py runserver);
* To work with API in local mode after pg_dump import use login: radek, pass: qwerasdf


## Chapter II.

#### 1. [1_Skyphrases.py](CHAPTER_II/1_Skyphrases.py)

Validating 512 keys from file https://pastebin.com/3u4QViN8

#### 2. [2_json.py](CHAPTER_II/2_json.py)

Adding numbers from cluttered JSON file written by eccentric dictator of the small island somewhere in the middle of the ocean https://pastebin.com/azc6e9fD

---

<img alt="Screen 1" src="https://raw.githubusercontent.com/rbartosinski/skgt-repo/master/screens/1.png" width="800">

<img alt="Screen 2" src="https://raw.githubusercontent.com/rbartosinski/skgt-repo/master/screens/2.png" width="800">

<img alt="Screen 3" src="https://raw.githubusercontent.com/rbartosinski/skgt-repo/master/screens/3.png" width="800">

<img alt="Screen 4" src="https://raw.githubusercontent.com/rbartosinski/skgt-repo/master/screens/4.png" width="800">

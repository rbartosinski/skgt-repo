#!/usr/bin/env bash

# Short install script to Exams REST/API
# Author: Radek Bartosiński

echo "Hello. This is script to install anything you need"
echo "to run Exams REST/API on your machine."
echo "If you want to do this in a few next moments:"
echo "- check your Internet connection,"
echo "- don't escape this window and..."
read -n1 -r -p "press any key to continue"

echo
echo "Creating required files and cloning code repository"

# creating files and cloning code repository
sudo mkdir ~/new_workspace
sudo chmod 777 ~/new_workspace
cd ~/new_workspace

git clone https://github.com/rbartosinski/skgt-repo.git
cd skgt-repo

echo
echo "Creating virtual environment and installing packages"

# creating venv, installing packages
python3 -m venv myvenv
source myvenv/bin/activate
python3 -m pip install --upgrade pip

cd CHAPTER_I/Exams_REST_API
pip install -r requirements.txt

echo
echo "Creating PostgreSQL instance with test/dev example data..."

# creating db instance and importing test/dev data
psql postgres -c "CREATE DATABASE exams_rest_db WITH ENCODING 'UTF8'"
psql exams_rest_db < pg_dump

echo
echo "Running Exams REST/API"

# running REST/API
python manage.py runserver

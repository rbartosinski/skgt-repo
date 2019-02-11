#!/usr/bin/env bash

# Full install script to Exams REST/API 
# Author: Radek Bartosiński

echo "Hello. This is script to install anything you want"
echo "to run Exams REST/API on your machine."
echo "If you want to do this in a few next moments:"
echo "- check your Internet connection,"
echo "- don't escape this window and..."
read -n1 -r -p "press any key to continue"

# pausing updating grub as it might triger ui
sudo apt-mark hold grub*
echo
echo "System updating..."

# update / upgrade
sudo apt update
sudo apt -y upgrade
echo
echo "Installing Python and tools..."

# install python, venv and git
sudo apt install -y python3 virtualenv git
  
echo
echo "Installing PostgreSQL Database..."

# installing PostgreSQL DB, creating new db
sudo apt-get install postgresql postgresql-contrib
psql postgres -c "CREATE DATABASE exams_rest_db WITH ENCODING 'UTF8'"


echo
echo "Again - system updating..."

# update and upgrade all packages
sudo apt update -y
sudo apt upgrade -y

# unpausing updating grub
sudo apt-mark unhold grub*

echo
echo "Creating required files and cloning code repository"

# creating files and cloning code repository
sudo mkdir ~/new_workspace
sudo chmod 777 ~/new_workspace
cd ~/new_workspace

git config --global user.name "user"
git config --global user.email user@user.user

git clone https://github.com/rbartosinski/skgt-repo.git
cd skgt-repo

echo
echo "Creating virtual environment, installing packages,"
echo "and running Exams REST/API"

# creating venv, installing packages and running REST/API
python3 -m venv myvenv
source myvenv/bin/activate
python3 -m pip install --upgrade pip

cd CHAPTER_I/Exams_REST_API
pip install -r requirements.txt
psql exams_rest_db < pg_dump

python manage.py runserver

#!/bin/bash
sudo yum install -y python-devel
sudo yum install -y python-pip
sudo pip install numpy nltk matplotlib pandas
sudo python -m nltk.downloader -d /usr/share/nltk_data punkt
sudo python -m nltk.downloader -d /usr/share/nltk_data averaged_perceptron_tagger

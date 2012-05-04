#!/bin/bash
virtualenv venv
source venv/bin/activate
easy_install -U distribute
pip install django djangorestframework

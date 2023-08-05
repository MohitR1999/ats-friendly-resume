# Resume in python (using reportlab) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an attempt to create an ATS friendly resume in python. I'm intending to maintain and enhance it as per my needs, or in case I get any feedback from the community. I'm trying to keep the code simple and easy to comprehend, and separating the data from the PDF generation logic. All the data that needs to be put in the resume is present in the ```data.json``` file

## Steps to run
- Make sure you have python version 3 installed
- Clone this repository
- Create a virtual environment by running the command ```python3 -m venv env```
- Activate the virtual environment by running the ```activate``` script for your respective operating system 
- Install all the required libraries by running ```pip install requirements.txt```
- Create a ```config.ini``` file as follows:

```
[global]
debug = false
author = <Your name>
email = <Your email>
address = <Your address>
phone = <Your phone number>
```
This will set the debug configuration as false, which will generate the resume without any grid lines. If debug is set to true it will generate the resume with gridlines
- Run the ```main.py``` file by executing the command ```python3 main.py```. This will generate a resume in PDF format with the name ```output.pdf``` in the project directory
- To customize the information in resume, just modify the ```data.json``` file with your required information
- Personal information would be picked up from the ```config.ini``` file that is present in the project root
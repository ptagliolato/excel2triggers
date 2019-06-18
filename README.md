[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

excel2triggers
==============
## Description
The script reads an Excel File "triggerPy.xlsx" with the two sheets: 
    "definizioneRegole" with columns:
        "tipoRegola", "template", "sqlstate" and a variable number of columns starting from column F
    "istanzeRegole" with columns:
        "tabella", "ordine", "tipoRegola", "sqlstate", and a variable number of columns starting from column E
It writes a new file "triggersFromExcel.sql" with mySQL sql statements "CREATE TRIGGER ..." composed from the values in
"istanze regole" and based on rules templates in sheet "definizioniRegole". 

## Usage: 
1. create a folder with an excel file "triggerPy.xlsx". It MUST contain the 2 sheets "definizioneRegole" and "istanzeRegole" with the same structure of the example file provided in this repository. (alternatively you can clone this repo and change the example file);
2. within the terminal cd into the created folder;
3. from the terminal execute the python script excel2trigger.py (input and output file names are currently coded within the python script).

## Docker version:
3.b. In alternative, on a machine with docker installed, you can use the docker image excel2triggers, mounting the current folder as a volume. Use the following statements within Ubuntu bash (but it should also work within windows terminal):

`docker run -v $(pwd):/home/ --rm ptagliolato/excel2triggers`

Find the output in the created triggersFromExcel.sql file (same directory)

### Build your own docker image:
You can build the docker image by yourself with the provided Dockerfile, using the statement:

`docker build -t <the_name_of_your_image> .`

and executing 

`docker run -v $(pwd):/home/ --rm <the_name_of_your_image>`


* Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

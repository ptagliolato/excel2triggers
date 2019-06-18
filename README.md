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
1. clone this repo
2. go into the created directory
3. from ubuntu bash execute

`docker run -v ``pwd``:/home/ --rm ptagliolato/excel2triggers`

or (it should work both on ubuntu bash and windows terminal)

`docker run -v $(pwd):/home/ --rm ptagliolato/excel2triggers`

Find the output in the created .sql file (same directory)

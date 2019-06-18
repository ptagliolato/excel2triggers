import pandas as pd
"""
The script reads an Excel File "triggerPy.xlsx" with the two sheets: 
    "definizioneRegole" with columns:
        "tipoRegola", "template", "sqlstate" and a variable number of columns starting from column F
    "istanzeRegole" with columns:
        "tabella", "ordine", "tipoRegola", "sqlstate", and a variable number of columns starting from column E
It writes a new file "triggersFromExcel.sql" with mySQL sql statements "CREATE TRIGGER ..." composed from the values in
"istanze regole" and based on rules templates in sheet "definizioniRegole". 
"""

trigger_pattern=u'''DELIMITER $$
CREATE TRIGGER `check_{tabella}` {TRIGGER_TYPE} ON `{tabella}` FOR EACH ROW BEGIN
{body}
END
$$
DELIMITER ;
'''

dfdef = pd.read_excel('triggerPy.xlsx', sheetname='definizioneRegole')
df_ord = pd.read_excel('triggerPy.xlsx', sheetname='istanzeRegole').sort_values(by=['tabella','ordine (per tabella)'])

istanze_indiceInizioColonneVariabili=4

# ottengo nuovo dataframe delle istanze con colonna iniziale aggiuntiva che contiene il template corrispondente alla regola
# ATTENZIONE: rispetto al codice precedentemente scritto, avendo invertito l'ordine dei dataframe per avere template come prima colonna,
#  ho anche dovuto modificare il "how" indicando un right join! Altrimenti mi prendeva anche una regola che non aveva
#  istanze...
df = pd.merge(dfdef[["template", "tipoRegola"]], df_ord, how='right',
              left_on='tipoRegola',
              right_on='tipoRegola')


# uso per quanto posso i nomi di colonna per migliore leggibilità (e manutenibilità)
series_triggerValorizzati = df.apply(
    lambda x: x.template.format(*x[istanze_indiceInizioColonneVariabili+1:], sqlstate=x.sqlstate),
    axis=1, result_type='expand'
)

df["triggerValorizzati"] = series_triggerValorizzati

# ottengo un oggetto series ed effettuo cast a dataframe. La colonna triggerValorizzati contiene
# la concatenazione di tutte regole per una singola tabella
df_concatena_regole = df.groupby('tabella')['triggerValorizzati'].apply(lambda x: '\n'.join(x)).to_frame()
df_concatena_regole["tabella"] = df_concatena_regole.index

# output è oggetto series in cui appaiono gli statement di creazione dei trigger di ogni tabella.
output = df_concatena_regole.apply(lambda x: trigger_pattern.format(body=x.triggerValorizzati, tabella=x.tabella, TRIGGER_TYPE='BEFORE INSERT'), axis=1)

fileoutput = open("triggersFromExcel.sql", "w")
for s in output.values:
    print(s) # output in console per debug
    fileoutput.write(s)
fileoutput.close()

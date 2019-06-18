FROM python:3.7
MAINTAINER tagliolato.p@irea.cnr.it
ARG export_file=triggerPy.xlsx
COPY $export_file triggerPy.xlsx
COPY createTriggers.py /
CMD ["python", "./createTriggers.py"]

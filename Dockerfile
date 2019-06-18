FROM amancevice/pandas
MAINTAINER tagliolato.p@irea.cnr.it
RUN pip install xlrd
WORKDIR /home
#ARG export_file=triggerPy.xlsx
#COPY $export_file triggerPy.xlsx
COPY excel2triggers.py /
CMD ["python", "./excel2triggers.py"]

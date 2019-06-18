FROM amancevice/pandas
MAINTAINER tagliolato.p@irea.cnr.it
RUN pip install xlrd
WORKDIR /home
COPY excel2triggers.py /
CMD ["python", "./excel2triggers.py"]

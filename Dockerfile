FROM jupyter/pyspark-notebook:spark-3.3.1
USER root

WORKDIR /work
# add needed packages
RUN apt-get update

# Install Python requirements (Esta imagen no tiene)
# COPY requirements.txt /home/
# RUN pip install -r /home/requirements.txt

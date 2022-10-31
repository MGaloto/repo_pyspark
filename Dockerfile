FROM jupyter/pyspark-notebook:spark-3.3.1
USER root

# add needed packages
RUN apt-get update

# Install Python requirements (Esta imagen no tiene)
# COPY requirements.txt /home/jovyan/
# RUN pip install -r /home/jovyan/requirements.txt

COPY jupyter_config.json /home/jovyan/
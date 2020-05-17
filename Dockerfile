# Dockerfile
FROM python:3.8-alpine
WORKDIR /opt/parrot
COPY * /opt/parrot/
RUN cd /opt/parrot/ && python3 setup.py install
ENTRYPOINT ["/opt/parrot/server.py"]
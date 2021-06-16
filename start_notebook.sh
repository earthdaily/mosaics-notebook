docker build -t mosaics-notebook .
docker run -it --rm -p 8888:8888 -v ${PWD}:/home/jovyan/work mosaics-notebook
docker run -it -p 8888:8888 -v $(pwd):/opt/notebooks -w /opt/notebooks/ pangeo/pangeo-notebook:2021.11.07 jupyter lab --ip 0.0.0.0

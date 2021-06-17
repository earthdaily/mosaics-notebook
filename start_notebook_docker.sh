docker run -it -p 8888:8888 -v $(pwd):/opt/notebooks -w /opt/notebooks/ continuumio/anaconda3 /bin/bash --login -c "source start_notebook_conda.sh"

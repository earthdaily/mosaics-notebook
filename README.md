# EarthDaily Mosaic Usage Example

## Pre-requisites
Docker must be installed. If you do not already have it installed, see https://www.docker.com/ for installation instructions specific to your platform

## Getting Started
- Login at https://mosaics-preview.earthdaily.com/home/login and obtain the signed URL to the mosaic through the web interface
- Run `sh start_notebook.sh` to build the Docker image and launch the Jupyter notebook server. 
- Make note of the URL displayed in the console output. It will look something like this: http://127.0.0.1:8888/?token=613a5f7fe598ceb1f66db705b11f5c2e1d15491cceb01fc0
- In your web browser, enter the URL and you should see a list of files for this notebook displayed
- Select `mosaic_usage_example.ipynb` and run the steps in the notebook. 
- Have fun and explore further! If your signed URL expires, you can go to the web interface to retrieve a new one. 

## Shutting Down 
- Hit Ctrl-C in the terminal to shut down the Jupyter notebook server. 

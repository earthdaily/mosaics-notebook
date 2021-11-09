# EarthDaily Mosaic Usage Example

This notebook demonstrates how to access and get started using EarthDaily's EarthMosaics. For more information about the product and service, see https://mosaics-preview.earthdaily.com/home/

## Pre-requisites
- Docker. If you do not already have it installed, download and run the installer for your platform at https://www.docker.com/products/docker-desktop
- Git must be installed. If you do not already have it installed, download and run the installer for your platform at http://git-scm.com/download 

## Getting Started
- Clone this repository: 
  - `git clone https://<username>:<password>@github.com/earthdaily/mosaics-notebook.git`
  - `cd mosaics-notebook`
- Run the following to build the Conda environment and launch the Jupyter notebook server: 
  - For OSX/Linux: `bash start_notebook_docker.sh`
  - For Windows: `start_notebook_docker.bat`
- The URL to the Jupyter Lab server is shown in the output for command above, open this URL in a web browser, you should see a list of files for this repository displayed.
- Select `mosaic_usage_example.ipynb` and run the steps in the notebook. 
  - Login at https://mosaics-preview.earthdaily.com/home/login and obtain the signed URL to the mosaic through the web interface
- Have fun and explore further! If your signed URL expires, you can go to the web interface to retrieve a new one. 

## Shutting Down 
- Click "Quit" in the browser window containing the list of files to shut down the Jupyter notebook server and exit the docker environment.

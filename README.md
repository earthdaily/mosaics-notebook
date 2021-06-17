# EarthDaily Mosaic Usage Example

## Pre-requisites
- Anaconda must be installed. If you do not already have it installed, download and run the installer for your platform at https://www.anaconda.com/products/individual#Downloads
- Git must be installed. If you do not already have it installed, download and run the installer for your platform at http://git-scm.com/download 

## Getting Started


- Open your Anaconda shell: 
  - For OSX/Linux: Open your terminal
  - For Windows: Open Anaconda Powershell Prompt
- Clone this repository: 
  - `git clone https://<username>:<password>@github.com/earthdaily/mosaics-notebook.git`
  - `cd mosaics-notebook`
- Run the following to build the Conda environment and launch the Jupyter notebook server: 
  - For OSX/Linux: `source start_notebook_conda.sh`
  - For Windows: `start_notebook_conda.bat`
- A web browser window should appear, and you should see a list of files for this notebook displayed
- Select `mosaic_usage_example.ipynb` and run the steps in the notebook. 
  - Login at https://mosaics-preview.earthdaily.com/home/login and obtain the signed URL to the mosaic through the web interface
- Have fun and explore further! If your signed URL expires, you can go to the web interface to retrieve a new one. 

## Shutting Down 
- Click "Quit" in the browser window containing the list of files to shut down the Jupyter notebook server and exit the Conda environment. 

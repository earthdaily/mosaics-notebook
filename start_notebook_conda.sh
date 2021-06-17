conda init bash 
conda env create -p $(pwd)/conda_env -f environment.yml 
conda activate $(pwd)/conda_env
jupyter notebook --allow-root
conda deactivate
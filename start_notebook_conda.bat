CALL conda env create -f environment.yml 
CALL conda activate notebooks
jupyter notebook
CALL conda deactivate
from planetlabs/notebooks:latest

# Install additional requirements
COPY requirements.txt mosaic_requirements.txt
RUN python -m pip install -r mosaic_requirements.txt 

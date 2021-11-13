## Requirements

* Python 3.9.6
* Docker 20.10.8


#### Creating virtual environment
```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

* Note: Please download csv file as "resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv" before training model

* URL to load download csv file
```html
https://data.gov.sg/dataset/resale-flat-prices
```

#### Create Model:
```bash
python model_training/hdb_project.py
```

#### Running tests:

```bash
python -m unittest
```

#### Running the server:
```bash
python -m flask run --host=0.0.0.0
```

### Command to build docker image from dockerfile
```bash
docker build -t ml-app .
```

### Command to run docker container
```bash
docker run -p 5000:5000 -e FLASK_APP=src/app.py -e PYTHONPATH=/app/src ml-app
```

### Command to run docker container
```bash
docker stop <container id>
```

### Example query
```html
localhost:5000/make-prediction?storey-range=7&floor-area-sqm=75&remaining-lease=64&town=PUNGGOL
```
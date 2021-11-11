Activate virtual environment

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
#### Running tests:

```bash
python -m unittest
```

#### Running the server:
```bash
python -m flask run --host=0.0.0.0
```

URL to load download csv file
```html
https://data.gov.sg/dataset/resale-flat-prices
```

### Command to build docker image from dockerfile
```bash
docker build -t ml-app .
```

### Command to run docker container
```bash
docker run -p 5000:5000 ml-app
```

### Example query
```html
make-prediction?storey-range=7&floor-area-sqm=75&remaining-lease=64&town=PUNGGOL
```
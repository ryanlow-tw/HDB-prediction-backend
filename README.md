Activate virtual environment

```bash
source ./environment/bin/activate
```
#### Running tests:

```bash
python -m unittest
```

#### Running the server:
```bash
python -m flask run --host=0.0.0.0
```

URL to load csv file
```html
https://docs.google.com/spreadsheets/d/1EkP-9IdQqu-hQfK-e4wf4ne_s5F54mS7BMvNKDR1Nw8/edit?usp=sharing
```

### Command to run docker container
```bash
docker run -p 5000:5000 ml-app
```
# IBM AI Enterprise Workflow Capstone Submission
Files for the IBM AI Enterprise Workflow Capstone submission. 

## Part 1 - Data Investigation

Open Jupyter Notebook: part1-data-investigation.ipynb

## Part 2 - Model Building/Selection

Open Jupyter Notebook: part2-model-building-and-selection.ipynb

## Part 3 - Model Production
### Application Deployment 
Start the application:
```bash
python run_app.py
```
Test the application:
```bash
python test/run_tests.py
```

### API Endpoints
```bash
GET /logs?type={type}
    where type = ingest|train|predict and is a required parameter.

GET /predict?date={date}&country={country}[&duration={duration}]
    where date is of the format YYYY-MM-DD and is a required parameter,
          country is a required parameter,
          duration defaults to 30 days if not specified.
```

### Docker Image Build
```bash
docker build -t ai-workflow-capstone-app .
```

### Docker Image Run
```bash
docker run \
    -it \
    --rm \
    -p 3000:8080 \
    --name ai-workflow-capstone-app \
    ai-workflow-capstone-app
```

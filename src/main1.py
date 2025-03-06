from fastapi import FastAPI
from google.cloud import bigquery
from typing import List
import os


# Set the path to your service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Aditya Mewada\Desktop\techsimproject\fastapi-with-bigQuery\src\BigQueryConfig.json'

app = FastAPI()

# Initialize BigQuery client
client = bigquery.Client()

# set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\Aditya Mewada\Desktop\techsimproject\fastapi-with-bigQuery\src\BigQueryConfig.json"

# Route to fetch data from BigQuery

@app.get("/bigquery")
async def query_bigquery():


    # Define the SQL query
    # query = """
    #     SELECT name, COUNT(*) as name_count
    #     FROM `bigquery-public-data.usa_names.usa_1910_2013`
    #     WHERE state = 'TX'
    #     GROUP BY name
    #     ORDER BY name_count DESC
    #     LIMIT 10
    # """

    query = """
        SELECT *
        FROM `learn-big-query-449510.sample123.Customer`
    """

    # Execute the query
    query_job = client.query(query)

    # Fetch results
    results = query_job.result()

    # Create a list of dictionaries to return
    response = []
    for row in results:
        response.append({"name": row.name, "age": row.age})
    return response


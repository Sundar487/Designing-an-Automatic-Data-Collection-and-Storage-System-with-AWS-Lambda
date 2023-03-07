import json
import mysql.connector
import urllib.request



# Connect to the database

def lambda_handler(event, context):
# Define the SQL query to create the table if it doesn't exist already
    db = mysql.connector.connect(host='database-2.c6zd23k986sf.us-east-2.rds.amazonaws.com',database='apidatabase',user='admin',password='sundar07')
    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS iss_position (
        id INT AUTO_INCREMENT PRIMARY KEY,
        latitude VARCHAR(255),
        longitude VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

# Execute the query to create the table
    cursor = db.cursor()
    cursor.execute(create_table_query)
    db.commit()

# Define the API endpoint URL
    api_url = 'http://api.open-notify.org/iss-now.json'

# Fetch the data from the API
    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode())

# Extract the latitude and longitude values
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']

# Define the SQL query to insert the data into the table
    insert_query = "INSERT INTO iss_position(latitude, longitude) VALUES (%s, %s)"

# Execute the query to insert the data into the table
    cursor = db.cursor()
    cursor.execute(insert_query, (latitude, longitude))
    db.commit()

# Close the database connection
    db.close()
   
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
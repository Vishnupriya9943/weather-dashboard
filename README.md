## Real-Time Weather Dashboard using AWS

# Step 1: Set Up AWS S3 for Static Website Hosting

1. Create an S3 Bucket
* Go to AWS Console → S3.
* Click “Create bucket”.
* Enter a unique Bucket name (e.g., weather-dashboard).
* Uncheck "Block all public access" under Permissions.
* Click Create bucket.

2. Enable Static Website Hosting
* Open the bucket and go to the Properties tab.
* Scroll down to Static website hosting → Click Edit.
* Select "Enable".
* Set index document as index.html.
* Click Save changes.

#  Step 2: Build the Frontend (HTML, CSS, JavaScript)

1. Create weather-dashboard.html

# Step 3: Deploy AWS Lambda Function

1. Create a Lambda Function
* Go to AWS Console → Lambda → Click Create Function.
* Select "Author from Scratch".
* Enter:
* Function name: WeatherFunction
* Runtime: Python 3.8
* Click Create Function.

# Step 4 : Connect Lambda to API Gateway
1. Add Lambda to API Gateway
* Open API Gateway → WeatherAPI.
* Click Integrations → Manage Integrations.
* Select "Lambda Function" → Choose WeatherFunction.
* Click Save.
2. Deploy the API
* Go to API Gateway → Deploy API.
* Select "Default Stage" → Click Deploy.
* Copy the Invoke URL (e.g., https://your-api-id.execute-api.us-east-1.amazonaws.com/weather).
* Replace "your-api-id" in index.html.

# Step 5: Store User Preferences in DynamoDB
1. Create a DynamoDB Table
* Go to AWS Console → DynamoDB.
* Click "Create Table".
* Table Name: UserPreferences
* Partition Key: userId (String)
* Click Create Table.

# Step 6: Access the Frontend (S3 Hosted Website)
* Go to AWS Console → S3.
* Open the bucket where your index.html is uploaded.
* Click on Properties → Scroll down to Static website hosting.
* Copy the Bucket website endpoint
* Paste this URL into your browser → Weather Dashboard should appear!

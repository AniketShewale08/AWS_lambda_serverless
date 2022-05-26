# AWS_lambda_serverless

# A Serverless Function with AWS Lambda and MongoDB

# I use AWS Lambda as a serverless platform and MongoDB Atlas as a database provider.

# Creating serverless function

    # You can install Serverless using a single command:
        -> sudo npm install -g serverless

    # Let’s configure Serverless:
        -> serverless config credentials --provider aws --key <ACCESS KEY ID> --secret 
           <SECRET KEY>    

    # To create a serverless framework
        ->  serveless create --template aws-python3.
        
        -> In serveless.yml file, do the following:
            - service name, provider
            - Runtime: Python 
            - Function name
                - Give path to the handler function

# To deploy the function to AWS LAMBDA    
    
    -> Once the template files are created, we have a working AWS Lambda function, we need  
       to deploy it:

       - serverless deploy


# AWS API Gateway

    # AWS API Gateway to expose our AWS Lambda function to the Internet.

        -> To do this, Add Trigger button in the Designer section of the page.
        
        -> In the trigger configuration dropdown menu select API Gateway

        -> Create an API 

            - choose REST APIs
            - select Open as securing the API endpoint
            - just hit the Add button to create our API Gateway.

# Getting Up and Running with MongoDB Atlas     

    -> Create a account in MongoDB Atlas- https://www.mongodb.com/cloud/atlas

    -> Click the Build a Cluster button

    -> select the Shared Clusters option

    -> Click on create Cluster button

    -> click on the Add New Database User button and give your user a unique username and password.

    -> Click on the green Add IP Address button 

        - then in the modal that pops up click on Allow Access From Anywhere.
        - Click the green Confirm button to save the change.


# Connecting MongoDB Atlas to AWS Lambda

    ->  To get the mongoDB Atlas connection string.

        - On the Clusters overview page, click on the Connect button.

    -> Select the Connect your application option and you'll be taken to a screen that has your connection string. 
        
        - Your username will be pre-populated, but you'll have to update the password and dbname values. 



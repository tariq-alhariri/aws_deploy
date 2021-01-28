# Deploying a Flask API

This is the project repo for the fourth course in the [Udacity Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004): Server Deployment, Containerization, and Testing.
API endpoint: [http://a4d5c5647129311ea8d420a22cf9d500-2039112863.eu-west-1.elb.amazonaws.com/](http://a4d5c5647129311ea8d420a22cf9d500-2039112863.eu-west-1.elb.amazonaws.com/)

API Documentaion:

- `GET '/'`: returns a response 'Healthy'. 
- `POST '/auth'`: it takes an email and a password as json arguments and returns a JWT based on a custom secret.
- `GET '/contents'`: requires a valid JWT, then returns the unencrpyted contents of that token. 

Postman Collection is in the file: aws_deploy.postman_collection.json

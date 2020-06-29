Steps for Assignment 2:
1: applied django rest framwork for the previous project

2:create api link

3:create react project, used the django rest api for communication with django backend

4:build react project, combine the output to django project template

5:create docker image by docker desktop for the whole project, test the image in local virtual machine

6:upload image to AWS ECR

7:use the ECR url to create container in AWS ECS, deploy a service

8:test the react page and api function in this cloud service.


Difference from assignment 1 to 2:
1.frontend page, 1 is simple html file, 2 appied react to achieve javascript function

2.deploy way, 1 use command to set up a new environment in heroku, while 2 using docker image, which contains the setting of virtual enronment, dependencies, add-on, etc.

3.data communication, 1 use django model to operate database directly, 2 use http api as commands.


Reflection:
The hardest part:

Deploying ECS service. Tutorial from amazon is not up-to-date(for many part), docker containner needs specific setting for access. To find a pratical solution is really consuming time.

The most fun parts:

The Docker. It is a nice experience to try this deploying way. An availabe image can publish my page for many cloud platform and reduce the time for testing. 

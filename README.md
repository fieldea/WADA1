# WebAppDevAssignment2

React page in aws s3:http://a2-react.s3-website-ap-southeast-2.amazonaws.com/


Django rest api:http://3.25.60.214:8080/formats/

AWS ECS page:http://3.25.60.214:8080/


![example](https://github.com/fieldea/WADA1/blob/master/bar.png)
![example](https://github.com/fieldea/WADA1/blob/master/line.png)

# WebAppDevAssignment1

Heroku page:https://frozen-tundra-92450.herokuapp.com/

![erd](https://github.com/fieldea/WADA1/blob/master/vpd.png)

Climate Data Visualize.

Show climate data with diagrams or charts of New Zealand Climate Data.

User can search data and select their prefered data to generate diagrams.

Each user can creat and manage(save/delete/edit/share) their pics/views.

#Server side Rendering
According to users' visiting url path, django finds the binding views matchingthe router rules in urls.py with some parameters to apply templates.
Then the views file use the parameters recieved from url to decide the how and which data to be rendered in the templates by using http response method or switch to other page. Templates will be searched in each folder named 'template' from each app folder. if not found, it will applied 404 page setting, if found, it will applied the templates of html files with data to be rendered

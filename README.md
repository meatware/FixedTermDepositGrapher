
ttps://www.blog.pythonlibrary.org/2017/12/12/flask-101-getting-started/
sitGrapher

### How to run Docker in local

#### Build
`make start` (creates container and installs requirement file)

#### Init Database
1) `make init_migrate` (initialise database & migration folder - run once)
2) `make migrate` (populate db fields from models)
3) `make upgrade` (when changing models to modify db)

#### Run app
`make serve` run app

#### Shutdown app
1) `make stop`
2) `make clean` (clean out all traces of app to start again)

https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one#comments

https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two

https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three

https://www.blog.pythonlibrary.org/2017/12/12/flask-101-getting-started/

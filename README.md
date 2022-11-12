# TNC Task



## Commands

### Specific Commands
* `make dev.all`  : build and start containers
* `make dev.build`  : build containers
* `make dev.up.d`   : start containers in detached mode
* `make dev.up`     : start containers in attached mode
* `make dev.down`   : stop containers and remove networks
* `make dev.restart`: firsts stop containers then start again
* `make dev.logs`   : attach to log console of containers

### Common Commands
* `make dcshell`      : open django container shell
* `make dshell`       : open django shell
* `make ipshell`      : open django ipython shell
* `make dcattach`     : attach to django container
* `make migrate`      : run `makemigrations and migrate` command in django container
* `make collectstatic`: run `collectstatic` command in django container
* `make test`         : run `test` command in django container
* `make psql`         : run `psql` in postgres container
* `make rediscli`     : run `redis cli` in redis container


### Setup
* `Open the terminal containing the project.`
* `Run command make dev.all`
* `This will build and start the containers.`
* `Then open a separate terminal window and run make migrate. This commnad will make and run migrations.`
* `Now run make dcshell. This command will sh into the django container.`
* `Now inside django container run python manage.py createsuperuser.`
* `Provide the username, email, password and confirm password. This will create a user for you.`
* `Now open your browser and go to localhost:8000/admin then provide your credential you used in above step and you will be logged into the admin panel.`
* `Now open postman and send a POST request to localhost:8000/api/v1/get_api_key/ in the body provide the name of API key {"key_name": "<Name of API key.>"}`
* `Open a new window on postman and send a GET request to localhost:8000/api/v1/quotes/ before sending the request in the headers tab add a new header x-api-key the value will be the key you got in previous step.`
* `To give the filter key in the URL provide limit query param. Like localhost:8000/api/v1/quotes/?limit=10`
* `In another window send a request to localhost:8000/api/v1/token/ in the body provide the username and password you used above to create a user {"username": "<Username used above>", "password": "<Password used above>"}`
* `In response of the above step you will get the jwt token. Copy the access from the response.`
* `In an other tab provide the api key like provided int the quotes GET request in the headers also in header provide Authorization header with value "Bearer <Access token you got in previous step.>"`
* `Now in the browser goto localhost:8000 here you will be connected to the socket and after every minute you will get the exchange rate updated on the screen.`

# my-family-api

## build django project 
docker build .

## Create django project 
docker-compose run app sh -c "django-admin.py startproject app ."

## Run migrations 
docker-compose run app sh -c "python manage.py makemigrations"

## Run unit tests
docker-compose run --rm app sh -c "python manage.py test"






## docker commands 
docker images
docker stop $(docker ps -q)
docker rmi -f $(docker images -q)
docker exec -it container_id bash

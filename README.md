# Elementals  backendDeveloper Task

## Setup
Make containers and run
```bash
docker-compose up -d --build
```
Run containers
```bash
docker-compose up
```
Stop containers
```bash
docker-compose down
```
# URL to redirec
In url - write id of link
```bash
http://127.0.0.1:8000/sl/39/
```
# Main APIs
## APIs for all
API for user registration. \
POST - username, password.
```bash
http://127.0.0.1:8000/sl/register/
```
## APIs for authenticated
API to get all own links with counter\
or create the new one. \
POST - link. \
Get - list of links with counter.\
(access only for authenticated)
```bash
http://127.0.0.1:8000/sl/user/create/
```
\
API to update, delete link.\
In url - write id of link.  \
(access only for Owner) \
for example:
```bash
http://127.0.0.1:8000/sl/user/39/
```

## APIs for admin
####admin login: admin admin
\
API to get list with counter of all links\
or create the new one for whatever user. \
(access only for admin)
```bash
http://127.0.0.1:8000/sl/admin/create/
```
\
API to update, delete link. \
You can update whatever link, even change owner.\
In url - write id of link.  \
(access only for admin)\
for example:
```bash
http://127.0.0.1:8000/sl/admin/39/
```
##JWT API
API to take JWT, take access token and use it with `Bearer` to have access to GET and POST API. \
POST - username and password and return JWT.
```bash
http://127.0.0.1:8000/api/token/
```


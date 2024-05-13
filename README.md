## start tips
```
# run the app
uvicorn main:app --reload
#
url/docs


lloggin package
debug
info
warning
error
critical


```

## init requirements
```
fastapi
uvicorn[standard]
python-multipart

python-jose[cryptography]
passlib[bcrypt]
pymongo
python-dotenv

```
## github cli
```
gh repo list
gh repo list --json id,name,url,sshUrl
gh repo view christianbueno1/front-auth-fastapi
gh repo view christianbueno1/front-auth-fastapi --json sshUrl --jq '.[]'
gh repo view christianbueno1/front-auth-fastapi --json sshUrl --jq '.[]' | tee


```

## .env
In the .env file

```
CONNECTION_STRING
MONGO_URL=mongodb://chris:maGazine1!@127.0.0.1:27017
MONGO_DB=register

SECRET_KEY = "secretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
FRONTEND_URL = "http://localhost:5173"
```

## links

- uvicorn  https://codevoweb.com/api-with-python-fastapi-and-mongodb-jwt-authentication/

- files structure https://fastapi.tiangolo.com/tutorial/bigger-applications/

- routers/users.py

## arjancodes

- code class https://github.com/ArjanCodes/examples/blob/main/2022/unit_testing/after_refactor/pay/processor.py


## print
```
import pprint
printer = pprint.PrettyPrinter()

printer.pprint(person)

```


## podman
```
podman image ls
podman pull docker.io/mongodb/mongodb-community-server:latest
podman run -d --name authdb \
-e MONGO_INITDB_ROOT_USERNAME=chris \
-e MONGO_INITDB_ROOT_PASSWORD='maGazine1!' \
-p 27017:27017 \
mongodb-community-server:latest

```

## Create the database


## document
- mongodb name: registerdb
- collection: users
- pass: bob123
```
{
  "username": "bob",
  "fullname": "bob marly",
  "email": "bob@ibm.com",
  "hashed_password": "$2b$12$tbc.zGujzSB/PZh6izzbUu9x.gHrxhi6khP2EzT/F0I8/ZOMeLlGa",
  "disabled": false
}

```

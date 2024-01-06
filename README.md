## tips
```
uvicorn main:app --reload

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

## .env

```
CONNECTION_STRING
MONGO_URL=mongodb://chris:maGazine1!@127.0.0.1:27017
MONGO_DB=register
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
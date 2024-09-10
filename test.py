from datetime import datetime, timedelta, timezone

# now = datetime.utcnow()

# use timezone-aware datetime objects, and always use UTC, assing timezone to now2
now = datetime.now(timezone.utc)
delta15min = timedelta(minutes=15)
expire = now + delta15min
print(f"now: {now}\ndelta15min: {delta15min}\nexpire: {expire}")
# print(f"now2: {now2}")

#
import logging
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    getenv("FRONTEND_URL"),
]

# AttributeError: module 'bcrypt' has no attribute '__about__'
logging.getLogger('passlib').setLevel(logging.ERROR)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
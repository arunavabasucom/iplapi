import os
import uvicorn
import sentry_sdk
from fastapi import FastAPI
from dotenv import load_dotenv
from routes import match , root
from fastapi.middleware.cors import CORSMiddleware 

'''
loading environment variables
'''

load_dotenv() 

'''
app
'''
app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

'''
sentry sdk initialized
'''
def profiles_sampler(sampling_context):
    return 0.5

sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    traces_sample_rate=1.0,
    environment=os.environ['SENTRY_ENVIRONMENT'],
    profiles_sample_rate=1.0,
    profiles_sampler=profiles_sampler
)
'''
routes
'''

app.include_router(root.router)
app.include_router(match.router)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
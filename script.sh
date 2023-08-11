# setup script 
pip install -r requirements.txt 
# start server
uvicorn src.main:app --host 0.0.0.0 --port 8000
#
cp .env.sample .env
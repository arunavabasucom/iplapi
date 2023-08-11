# setup script 
pip install -r requirements.txt 
# start server
uvicorn src.main:app --host 0.0.0.0 --port 8000
# for coping ens 
cp .env.sample .env
# for test and coverage 
coverage run --source=src -m pytest -v __tests__/ && coverage report -m
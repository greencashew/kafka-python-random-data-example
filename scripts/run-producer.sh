cd ../ || exit

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 ./producer.py
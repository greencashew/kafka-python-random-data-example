from kafka import KafkaProducer
import json
import time
import datetime
from faker import Faker

KAFKA_TOPIC = "invoices"
BOOTSTRAP_SERVER = 'localhost:9092'

fake = Faker()

def get_random_invoice():
    tax_percentage = 12
    net_price = fake.random_int(min=3, max=15)
    date_time_invoice_created = fake.date_time_between(start_date='-20y', end_date='now', tzinfo=None) \
        .strftime('%Y-%m-%dT%H:%M:%S')
    return {
        "id": fake.random_number(digits=12),
        "name": fake.name(),
        "date": date_time_invoice_created,
        "address": fake.address().replace("\n", " "),
        "startGate": fake.city(),
        "exitGate": fake.city(),
        "price": {
            "net": net_price,
            "taxPercentage": tax_percentage,
            "total": net_price + (net_price * (tax_percentage / 100))
        }
    }


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1:
        random_invoice = get_random_invoice()
        print("{}: {}".format(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'), random_invoice))
        producer.send(KAFKA_TOPIC, random_invoice)
        time.sleep(fake.random_int(0, 3))

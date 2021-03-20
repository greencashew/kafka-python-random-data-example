from datetime import datetime

from kafka import KafkaConsumer
import sys

KAFKA_TOPIC = "invoices"
BOOTSTRAP_SERVER = 'localhost:9092'
GROUP_ID = 'consumerGroup1'
AUTO_OFFSET_RESET = 'earliest'

if __name__ == "__main__":
    consumer = KafkaConsumer(KAFKA_TOPIC,
                             group_id=GROUP_ID,
                             bootstrap_servers=BOOTSTRAP_SERVER,
                             auto_offset_reset=AUTO_OFFSET_RESET)
    try:
        for message in consumer:
            print("[{}][{}:{}:{}]: {}".format(
                datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
                message.topic,
                message.partition,
                message.offset,
                message.value))

    except KeyboardInterrupt:
        sys.exit()

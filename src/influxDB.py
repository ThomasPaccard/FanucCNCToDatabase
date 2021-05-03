from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


import time

token = "WuAkbaCMucy5L6IKaBroNpSd-XcJiEFRv-RhYrIO-vyK3nis0XP1YGpCRnMx24NxVIWjAkgT_crMw19UZHrVQA=="
org = "remy.cretin@polymtl.ca"
bucket = "fanucCNC"

client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)


def influxDB_send_data(data):
    write_api.write(bucket, org, Point("SpeedCNC").tag("location", "Polytechnique").field("Speed", data))




import boto3
import json

class LimitsService(object):

    def __init__(self):
        self.limit_types = ['rds', 'ec2']

    def execute(self):
        pass

    def fetch_check_ids(self):
        client = boto3.client('support', region_name='us-west-2')
        response = client.describe_trusted_advisor_checks(
            language='en'
        )
        mapped_objects = list(map(lambda l: {l:list(filter(lambda r: l in r['name'] and 'limit' in r['name'], \
            response['checks']))[0]['id']}, self.limit_types))
        return mapped_objects
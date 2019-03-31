from unittest import TestCase, mock
from services.limits_service import LimitsService
from mock_objects import client_invoke_mock

class TestLimits(TestCase):

    def setUp(self):
        self.limit_service = LimitsService()
    
    @mock.patch('services.limits_service.boto3')
    def test_sample(self, boto3):
        boto3.client('support').describe_trusted_advisor_checks.return_value = {
            'checks': [
                {
                    'id' : 'ec2-check-id',
                    'name': 'ec2-limit-name'
                }, 
                {
                    'id' : 'rds-check-id',
                    'name': 'rds-limit-name'
                }      
            ]
        }
        result = self.limit_service.fetch_check_ids()
        self.assertEqual(result, [{'rds': 'rds-check-id'}, {'ec2': 'ec2-check-id'}])
import boto3

def read_credentials():
	headers, content = None, None
	credentials = ()
	with open('credentials.csv', 'r') as f:
		headers, content = f.readlines()
	dictionary = zip(
		headers.strip().split(','),
		content.strip().split(',')
		)
	return {k: v for k, v in dictionary}

credentials = read_credentials()
# print(credentials)

opts = (
	'aws_access_key_id': credentials['Access key ID'],
	'aws_secret_access_key': credentials['secret access key']
	)
ec2 = boto3.client('ec2', **opts)
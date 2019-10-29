import boto3

ec2_client = boto3.client('ec2', region_name='eu-central-1')

hosts_file = '/home/ubuntu/new-test/show_local_ip/hosts'

find_instances = ec2_client.describe_tags(
    Filters=[
        {
            'Name': 'key',
            'Values': [
                'InstanceGroup'
            ],
            'Name': 'value',
            'Values': [
                'webservers'
            ]
        }
    ]
)
res_dict = find_instances['Tags']
instance_ids = []

print(res_dict)
for x in res_dict:
    for k, v in x.items():
        if k == 'ResourceId':
            instance_ids.append(v)
print(instance_ids)

for i in instance_ids:
    get_instance_data = ec2_client.describe_instances(InstanceIds=[i])
    instance_dns = get_instance_data['Reservations'][0]['Instances'][0]['PublicDnsName']
    with open(hosts_file, "r") as in_file:
        buf = in_file.readlines()

    with open(hosts_file, "w") as out_file:
        for line in buf:
            if line == "[webservers]\n":
                line = line + instance_dns + "\n"
            out_file.write(line)

print(instance_dns)

# with open("hosts", "r") as in_file:
#     buf = in_file.readlines()
#
# with open("hosts", "w") as out_file:
#     for line in buf:
#         if line == "[webservers]\n":
#             line = line + "Include below\n"
#         out_file.write(line)

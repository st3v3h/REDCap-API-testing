from requests import post
# Two constants we'll use throughout
TOKEN = '' #Token removed for now
URL = '' #URL removed for now

payload = {'token': TOKEN, 'format': 'json', 'content': 'metadata'}

response = post(URL, data=payload)

print (response.status_code)

print()

metadata = response.json()


print('this project has %d fields' % len(metadata))
print()
print ('field_name (type) ---> field_label')
print('-----------------------')
for field in metadata:
    print('%s (%s) ---> %s' % (field['field_name'], field['field_type'], field['field_label']))

print()
print('Every field has these keys: %s' % ', ' .join(sorted(metadata[0].keys())))


payload['content'] = 'record'
payload['type'] = 'flat'
response = post(URL, data=payload)
data = response.json()

print('THIS PROJECT HAS %d RECORDS' % len(data))

record = data[2]
for field_name, value in record.items():
    print('%s: %s' % (field_name, value))



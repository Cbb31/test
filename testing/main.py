import requests
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))

ip_addr = input("Enter an IP address; ")
print(ip_addr)
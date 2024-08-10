issuer_id = '1234567890'  # Use the Issuer ID you obtained from App Store Connect

# Use the issuer_id in your API requests or configurations
api_request_headers = {
    'Authorization': f'Bearer {access_token}',
    'Issuer-ID': issuer_id
}

# Make API request using the issuer_id
response = requests.get('https://api.appstoreconnect.com/some_endpoint', headers=api_request_headers)

print(response.json())

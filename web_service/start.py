import requests

url = "http://localhost:8000/api/detect/"

payload="{\"lang\": \"fa\",\"docType\": \"33\",\"docTitle\": \"\",\"docBody\": \"یکی نیست بگه بابا این چه وضعشه\",\"docSummary\": \"this is doc Summary\",\"docTags\": [\"tag1\", \"teg2\"]}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'))

print(response.text)

# from google import genai
# client = genai.Client();
# interaction = client.models.generate_content(
#     model="gemini-flash-latest",
#     contents="Explain how quantum computing works in one sentence"
# )

# print(interaction.text)


# Raw HTTP version



# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -X POST \
#   -d '{
#     "contents": [
#       {
#         "parts": [
#           {
#             "text": "Explain how AI works in a few words"
#           }
#         ]
#       }
#     ]
#   }'
import os
import urllib.request
import json

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
headers = {
    "x-goog-api-key":os.environ["GEMINI_API_KEY"],
    "Content-Type": "application/json",
}
payload ={
    "contents":[{
        "parts":[{"text":"Hi"}]
    }]
}
body = json.dumps(payload).encode("utf-8");


req = urllib.request.Request(url, data=body, headers=headers, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        text = result["candidates"][0]["content"]["parts"][0]["text"]
        print(text)

except urllib.error.HTTPError as e:
    print(f"HTTP error {e.code} : {e.reason}")
    print(e.read().decode('utf-8'))


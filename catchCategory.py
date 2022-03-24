import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def getCategory(rawText):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    data = {
        "Inputs": {
            "data":
            [
                {
                    "headline": rawText
                },
            ]
        },
        "GlobalParameters": {
            "method": "predict"
        }
    }

    body = str.encode(json.dumps(data))

    url = 'http://37515208-fb7c-4945-8546-9805166a87c9.eastus.azurecontainer.io/score'
    api_key = '' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = str(result, encoding="utf8") # retrieve data from endpoint
        result = eval(result)
        result = result.get("Results")[0]
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
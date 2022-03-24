import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
# bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


def getBias(rawText):
# Request data goes here
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
    data = {
        "Inputs": {
            "data":
            [
                {
                    "Column1": rawText
                },
            ]
        },
        "GlobalParameters": {
            "method": "predict"
        }
    }

    body = str.encode(json.dumps(data))

    url = 'http://f7798c2b-b6e3-4488-9263-15ad18b13886.eastus.azurecontainer.io/score'
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

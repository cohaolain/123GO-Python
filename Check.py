import os
from Client import Client
import json
from datetime import datetime

variables = ["123GO_ACCESS_TOKEN", "123GO_EMAIL", "123GO_PASSWORD"]
if not any(map(os.getenv, variables)):
    from dotenv import load_dotenv
    load_dotenv()

access_token, email, password = map(os.getenv, variables)
client = Client(access_token=access_token, email=email, password=password)
if client:
    print("Client created.")


def j_print(d):
    print(json.dumps(d, indent=4))


post_endpoints = ["GetUserDetails", "GetPolicyDetails", "GetScores",
                  "GetJourneys", "GetNotifications"]
# There's also the `ReadNotifications` endpoint, that sets notifications as `read`

# There's also the `GetEvents` endpoint, which is a GET endpoint, not POST.
# It gives the details (GPS points) of a given `journeyID`

print("Available POST endpoints:", ", ".join(post_endpoints), "\n")

for endpoint in post_endpoints:
    print(endpoint)
    response = client.make_request(endpoint)
    if endpoint == "GetJourneys":
        latest_journey_id = response['Journeys'][-1]['JourneyId']
    j_print(client.make_request(endpoint))
    print("\n\n\n")


get_endpoints = [("GetEvents", {"journeyId": latest_journey_id})]
for get in get_endpoints:
    print(get[0])
    j_print(client.make_get_request(*get))
    print("\n\n\n")

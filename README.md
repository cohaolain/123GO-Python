# 123GO API Client

This is a Python library allowing you to interact with the 123GO telematics insurance API.  
This is useful if you want to have a record of things like your daily mileage and driving scores.  
The included example code (`Check.py`) shows how to use the library. It prints out some data from each of the endpoints. Instructions are down below!

This is a _work in progress_.  
It hasn't been fully packaged as a library just yet.

## Requirements

You need Python (duh). Python 3.  
Then you just need some dependencies. They're listed in `requirements.txt`.  
You can install them all together with:

```bash
pip3 install -r requirements.txt
```

Sweet - let's go!

## Client

A client object allows you to interact with the API on a per-account basis, giving you the power to request data from any valid endpoint. The client handles requests, authentication etc.

```python
my_client = Client(access_token=access_token)
# OR
my_client = Client(email=email, password=password)
```

Creating a client requires valid credentials for an insurance policy.  
This can take the form of an access token, or an email/password pair.  
If an email/password pair is provided, this is simply used to generate an access token.

This then exposes two functions,
`make_request(endpoint)` and `make_get_request(endpoint, params)`.  
These allow `POST` and `GET` requests respectively to be made to the API.

## Example

There's an example usage included in the `Check.py` file.  
It prints some data from every endpoint, including your policy details, scoring details, journey scores and the GPS markers from your most recent journey.

### Trying it yourself

Start by populating `.env` in the same format as `.sample_env` with your credentials.  
You can provider either an email/password pair, or an existing access token.

Then, you can run `Check.py` with `python3 Check.py`.  
For an interactive prompt with a logged in client object, you can run
`python3 -i Check.py`.

This gives us an output similar to the following:

```
Client created.
Available POST endpoints: GetUserDetails, GetPolicyDetails, GetScores, GetJourneys, GetNotifications

GetUserDetails
{
    "RequestResult": {
        "Success": true,
        "Message": "Successfull request."
    },
    "CustomerRef": "123",
    "FirstName": "Áine",
    "LastName": "Malone",
    "PasswordChangeRequired": false
}
...



GetPolicyDetails
{
    "RequestResult": {
        "Success": true,
        "Message": "Successfull request."
    },
    "PolicyNumber": "123",
    "StartDate": "2019-06-02T12:12:12",
    "PredictedStartDate": "2019-07-01T10:10:10.12345",
    "EndDate": "2020-06-01T23:59:00",
    "MileageAllowance": 10000.0,
...



GetScores
{
    "Scores": [
        {
            "Period": 2,
            "SmoothScore": 7.0,
            "SpeedScore": 10.0,
            "UsageScore": 3.3,
            "OverallScore": 6.8
        },
        {
...



GetJourneys
{
    "RequestResult": {
        "Success": true,
        "Message": "Successfull request."
    },
    "Journeys": [
        {
            "JourneyId": 123192837,
            "JourneyNumber": 1023,
            "StartDate": "2020-02-16T12:12:51",
            "EndDate": "2020-02-16T13:25:48",
            "Overall": 10.0,
            "Smoothness": 10.0,
            "Usage": 10.0,
            "Speed": 10.0,
            "Events": []
        },
...



GetNotifications
{
    "RequestResult": {
        "Success": true,
        "Message": "Successfull request."
    },
    "Notifications": [],
    "UnreadNotifications": 0
}



GetEvents
{
    "RequestResult": {
        "Success": true,
        "Message": "Successfull request."
    },
    "Events": [
        {
            "JourneyId": 0,
            "Latitude": "52.670326",
            "Longitude": "-6.869139",
            "Type": 0
        },
...
```

## Notice of Non-Affiliation and Disclaimer

This project is not affiliated, authorized, endorsed by, or in any way officially connected with [123.ie](https://123.ie), or any of its subsidiaries or affiliates.

The names [123.ie](https://123.ie) and [123GO](https://www.123.ie/young-drivers-car-insurance) as well as related names, marks, emblems and images are registered trademarks of their respective owners.

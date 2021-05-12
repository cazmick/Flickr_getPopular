import requests

expected_status_code = 200
payload = {'method': 'flickr.photos.getPopular', 'api_key': '1785e9ea841ec5764e7770f18edd51b0',
           'user_id': '153795036@N06'}
request_get = requests.get("http://api.flickr.com/services/rest", params=payload)
print("--------------Updated URL After Value--------------- \n" + request_get.url)
print("------------------Json Response----------------------\n" + request_get.text)
try:
    assert expected_status_code == request_get.status_code
    print("Assertion Status : Assertion Passed")
except Exception:
    print("Assertion Failed" + request_get.status_code)

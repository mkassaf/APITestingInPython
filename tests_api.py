import requests
import json
import jsonpath
from assertpy.assertpy import assert_that


def test_Add_new_Data():
    url = "https://skillsmatch.mdx.ac.uk/api/keyword/"

    payload={}
    headers = {
        'Authorization': 'Basic YXNzYWY6QXNzYWZAMTIz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    assert_that(response.status_code).is_equal_to(200)


def test_403_Forbidden():
    url = "https://skillsmatch.mdx.ac.uk/api/keyword/"

    response = requests.request("GET", url)

    assert_that(response.status_code).is_equal_to(403)


def test_create_new_log():
    url = "https://skillsmatch.mdx.ac.uk/api/log/"

    payload = json.dumps({
        "message": "Hellow",
        "type": "testing",
        "created_by": 1
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    id = jsonpath.jsonpath(response.json(), "id")
    message = jsonpath.jsonpath(response.json(), "message")
    type = jsonpath.jsonpath(response.json(), "type")

    assert_that(len(id)).is_equal_to(1)
    

    assert_that(message[0]).is_equal_to("Hellow")

    assert_that(type).contains("testing")

    url += str(id[0])
    
    response_from_get = requests.request("GET", url)

    assert_that(response_from_get.status_code).is_equal_to(200)

    assert_that(response_from_get.text).is_equal_to(response.text)

    response = requests.request("DELETE", url)

    assert_that(response.status_code).is_equal_to(204)

    response = requests.request("GET", url)

    assert_that(response.status_code).is_equal_to(404)
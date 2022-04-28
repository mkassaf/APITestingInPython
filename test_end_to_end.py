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
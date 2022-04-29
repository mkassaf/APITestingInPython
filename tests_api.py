import requests
import json
import jsonpath
from assertpy.assertpy import assert_that
from lxml import html

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


def test_googleHomePage():
    url = "https://skillsmatch.mdx.ac.uk/accounts/login/"

    response = requests.request("GET", url)

    #print(response.text)

    assert_that(response.status_code).is_equal_to(200)

    tree = html.fromstring(response.text)
    username = tree.xpath('//input[@name="username"]')
    password = tree.xpath('//input[@name="password"]')
    signInText = tree.xpath("//div[@class='container col-sm-3']/h2[contains(text(),'Sign in')]")
 
    assert_that(len(username)).is_equal_to(1)
    assert_that(len(password)).is_equal_to(1)
    assert_that(len(signInText)).is_equal_to(1)

    print(username[0])
    print(password[0])
    print(signInText[0])
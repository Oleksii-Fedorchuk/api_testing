import pytest
from requests import get, delete
from http import HTTPStatus

"""Tests GET"""


@pytest.mark.smoke
@pytest.mark.regression
def test_get_status(base_page):
    request = get(base_page.base_url())
    response = request
    assert response.status_code == HTTPStatus.OK, \
        f"Status code is not as expected\nActual: {response.status_code}\nExpected: {HTTPStatus.OK}"


@pytest.mark.regression
def test_get_basic_user_list(base_page, env):  # To fix the problem change "in" with "=="
    request = get(base_page.base_url())
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Response json is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_first_user_data(base_page, env):
    first_user = f"{base_page.base_url()}/1"
    request = get(first_user)
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"][0]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First user data is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_first_user_id(base_page, env):
    first_user = f"{base_page.base_url()}/1"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["id"]
    expected = env.user_list["data"][0]["id"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First user id is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_email_of_first_user(base_page, env):
    first_user = f"{base_page.base_url()}/1"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["email"]
    expected = env.user_list["data"][0]["email"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Email of first user is not as expected \nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_first_name_of_first_user(base_page, env):
    first_user = f"{base_page.base_url()}/1"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["first_name"]
    expected = env.user_list["data"][0]["first_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First name of first user is not as expected \nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_last_name_of_first_user(base_page, env):
    first_user = f"{base_page.base_url()}/1"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["last_name"]
    expected = env.user_list["data"][0]["last_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Last name of first user is not as expected \nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_second_user_data(base_page, env):
    second_user = f"{base_page.base_url()}/2"
    request = get(second_user)
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"][1]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Second user data is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_second_user_id(base_page, env):
    first_user = f"{base_page.base_url()}/2"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["id"]
    expected = env.user_list["data"][1]["id"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Second user id is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_email_of_second_user(base_page, env):
    second_user = f"{base_page.base_url()}/2"
    request = get(second_user)
    response = request.json()
    actual = response["data"]["email"]
    expected = env.user_list["data"][1]["email"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Email of second user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_first_name_of_second_user(base_page, env):
    second_user = f"{base_page.base_url()}/2"
    request = get(second_user)
    response = request.json()
    actual = response["data"]["first_name"]
    expected = env.user_list["data"][1]["first_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First name of second user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_last_name_of_second_user(base_page, env):
    second_user = f"{base_page.base_url()}/2"
    request = get(second_user)
    response = request.json()
    actual = response["data"]["last_name"]
    expected = env.user_list["data"][1]["last_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Last name of second user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_third_user_data(base_page, env):
    third_user = f"{base_page.base_url()}/3"
    request = get(third_user)
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"][2]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Third user data is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_third_user_id(base_page, env):
    first_user = f"{base_page.base_url()}/3"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["id"]
    expected = env.user_list["data"][2]["id"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Third user id is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_email_of_third_user(base_page, env):
    third_user = f"{base_page.base_url()}/3"
    request = get(third_user)
    response = request.json()
    actual = response["data"]["email"]
    expected = env.user_list["data"][2]["email"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Email of third user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_first_name_of_third_user(base_page, env):
    third_user = f"{base_page.base_url()}/3"
    request = get(third_user)
    response = request.json()
    actual = response["data"]["first_name"]
    expected = env.user_list["data"][2]["first_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First name of third user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_last_name_of_third_user(base_page, env):
    third_user = f"{base_page.base_url()}/3"
    request = get(third_user)
    response = request.json()
    actual = response["data"]["last_name"]
    expected = env.user_list["data"][2]["last_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Last name of third user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_fourth_user_data(base_page, env):
    fourth_user = f"{base_page.base_url()}/4"
    request = get(fourth_user)
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"][3]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Fourth user data is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_fourth_user_id(base_page, env):
    first_user = f"{base_page.base_url()}/4"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["id"]
    expected = env.user_list["data"][3]["id"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Fourth user id is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_email_of_fourth_user(base_page, env):
    fourth_user = f"{base_page.base_url()}/4"
    request = get(fourth_user)
    response = request.json()
    actual = response["data"]["email"]
    expected = env.user_list["data"][3]["email"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Email of fourth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_first_name_of_fourth_user(base_page, env):
    fourth_user = f"{base_page.base_url()}/4"
    request = get(fourth_user)
    response = request.json()
    actual = response["data"]["first_name"]
    expected = env.user_list["data"][3]["first_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First name of fourth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_last_name_of_fourth_user(base_page, env):
    fourth_user = f"{base_page.base_url()}/4"
    request = get(fourth_user)
    response = request.json()
    actual = response["data"]["last_name"]
    expected = env.user_list["data"][3]["last_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Last name of fourth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_fifth_user_data(base_page, env):
    fifth_user = f"{base_page.base_url()}/5"
    request = get(fifth_user)
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"][4]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Fifth user data is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_fifth_user_id(base_page, env):
    first_user = f"{base_page.base_url()}/5"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["id"]
    expected = env.user_list["data"][4]["id"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Fifth user id is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_email_of_fifth_user(base_page, env):
    fifth_user = f"{base_page.base_url()}/5"
    request = get(fifth_user)
    response = request.json()
    actual = response["data"]["email"]
    expected = env.user_list["data"][4]["email"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Email of fifth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_fist_name_of_fifth_user(base_page, env):
    fifth_user = f"{base_page.base_url()}/5"
    request = get(fifth_user)
    response = request.json()
    actual = response["data"]["first_name"]
    expected = env.user_list["data"][4]["first_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First name of fifth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_last_name_of_fifth_user(base_page, env):
    fifth_user = f"{base_page.base_url()}/5"
    request = get(fifth_user)
    response = request.json()
    actual = response["data"]["last_name"]
    expected = env.user_list["data"][4]["last_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Last name of fifth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_sixth_user_data(base_page, env):
    sixth_user = f"{base_page.base_url()}/6"
    request = get(sixth_user)
    response = request.json()
    actual = response["data"]
    expected = env.user_list["data"][5]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Sixth user data is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_sixth_user_id(base_page, env):
    first_user = f"{base_page.base_url()}/6"
    request = get(first_user)
    response = request.json()
    actual = response["data"]["id"]
    expected = env.user_list["data"][5]["id"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Sixth user id is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_email_of_sixth_user(base_page, env):
    sixth_user = f"{base_page.base_url()}/6"
    request = get(sixth_user)
    response = request.json()
    actual = response["data"]["email"]
    expected = env.user_list["data"][5]["email"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Email of sixth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_first_name_of_sixth_user(base_page, env):
    sixth_user = f"{base_page.base_url()}/6"
    request = get(sixth_user)
    response = request.json()
    actual = response["data"]["first_name"]
    expected = env.user_list["data"][5]["first_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"First name of sixth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_last_name_of_sixth_user(base_page, env):
    sixth_user = f"{base_page.base_url()}/6"
    request = get(sixth_user)
    response = request.json()
    actual = response["data"]["last_name"]
    expected = env.user_list["data"][5]["last_name"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Last name of sixth user is not as expected.\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_amount_of_users(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = len(response["data"])
    expected = env.user_list["amount_of_users"]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Amount of users is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.skip("Example for skipping tests. Delete this string to pass the test")
@pytest.mark.regression
def test_get_all_emails_from_user_list(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = [user["email"] for user in response["data"]]
    expected = [user["email"] for user in env.user_list["data"]]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Some emails are missed in data\nActual{actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_first_names_from_user_list(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = [user["first_name"] for user in response["data"]]
    expected = [user["first_name"] for user in env.user_list["data"]]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Some first names are missed in data\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_all_last_names_from_user_list(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = [user["last_name"] for user in response["data"]]
    expected = [user["last_name"] for user in env.user_list["data"]]
    assert request.status_code == HTTPStatus.OK
    assert actual == expected, f"Some last names are missed in data\nActual: {actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_support_url(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    expected = env.user_list["support"]["url"]
    assert request.status_code == HTTPStatus.OK
    assert expected in response["support"]["url"], \
        f"Support email is not as expected\nActual: {response['support']['url']}\nExpected: {expected}"


@pytest.mark.regression
def test_support_text(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    expected = env.user_list["support"]["text"]
    assert request.status_code == HTTPStatus.OK
    assert expected == response["support"]["text"], \
        f"Support text is not as expected.\nActual: {response['support']['text']}\nExpected: {expected}"


"""Tests DELETE"""


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user_status(base_page):
    request = delete(f"{base_page.base_url()}/{{id}}")
    response = request
    assert response.status_code == HTTPStatus.NO_CONTENT, \
        f"Status code is not expected\nActual: {response.status_code}\nExpected: {HTTPStatus.NO_CONTENT}"


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_header_access_control(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Access-Control-Allow-Origin"]
    expected = env.user_list["header"]["Access-Control-Allow-Origin"]
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert actual == expected, \
        f"Header Access-Control-Allow-Origin is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.xfail("Example for xfail tests, to fix late. Delete this string to pass the test")
@pytest.mark.regression
def test_delete_header_cf_cache_status(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["CF-Cache-Status"]
    expected = env.user_list["header"]["CF-Cache-Status"]
    assert actual == expected, \
        f"Header CF-Cache-Status is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_delete_header_content_length(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Content-Length"]
    expected = env.user_list["header"]["Content-Length"]
    assert actual == expected, \
        f"Header Content-Length is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_header_etag(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["etag"]
    expected = env.user_list["header"]["etag"]
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert actual == expected, \
        f"Header etag is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_delete_header_cf_ray(base_page):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert 'CF-Ray' in response, f"The CF-Ray is not present in header response"


@pytest.mark.regression
def test_delete_header_date(base_page):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert 'Date' in response, f"The date is not present in header response"


@pytest.mark.regression
def test_delete_header_server(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Server"]
    expected = env.user_list["header"]["server"]
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert actual == expected, \
        f"Header Server is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_delete_header_x_powered_by(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["X-Powered-By"]
    expected = env.user_list["header"]["x_powered_by"]
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert actual == expected, \
        f"Header X-Powered-By is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_header_via(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Via"]
    expected = env.user_list["header"]["via"]
    assert request.status_code == HTTPStatus.NO_CONTENT
    assert actual == expected, \
        f"Header Via is not as expected\nActual: {actual}\nExpected: {expected}"

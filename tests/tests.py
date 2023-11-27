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
    assert actual == expected, f"Response json is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.skip("Example for skipping tests. Delete this string to pass the test")
@pytest.mark.regression
def test_get_all_emails_from_user_list(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = [user["email"] for user in response["data"]]
    expected = [user["email"] for user in env.user_list["data"]]
    assert actual == expected, f"Some emails are missed in data\nActual{actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_first_names_from_user_list(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = [user["first_name"] for user in response["data"]]
    expected = [user["first_name"] for user in env.user_list["data"]]
    assert actual == expected, f"Some first names are missed in data\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_get_all_last_names_from_user_list(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    actual = [user["last_name"] for user in response["data"]]
    expected = [user["last_name"] for user in env.user_list["data"]]
    assert actual == expected, f"Some last names are missed in data\nActual: {actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_support_url(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    expected = env.user_list["support"]["url"]
    assert expected in response["support"]["url"], \
        f"Support email is not as expected\nActual: {response['support']['url']}\nExpected: {expected}"


@pytest.mark.regression
def test_support_text(base_page, env):
    request = get(base_page.base_url())
    response = request.json()
    expected = env.user_list["support"]["text"]
    assert expected == response["support"]["text"], \
        f"Support text is not as expected.\nActual: {response['support']['text']}\nExpected: {expected}"


"""Tests DELETE"""


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_user_status(base_page):
    request = delete(f"{base_page.base_url()}/{{id}}")
    response = request
    print(response)
    assert response.status_code == HTTPStatus.NO_CONTENT, \
        f"Status code is not expected\nActual: {response.status_code}\nExpected: {HTTPStatus.NO_CONTENT}"


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_header_access_control(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Access-Control-Allow-Origin"]
    expected = env.user_list["header"]["Access-Control-Allow-Origin"]
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
    assert actual == expected, \
        f"Header etag is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_delete_header_cf_ray(base_page):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    assert 'CF-Ray' in response, f"The CF-Ray is not present in header response"


@pytest.mark.regression
def test_delete_header_date(base_page):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    assert 'Date' in response, f"The date is not present in header response"


@pytest.mark.regression
def test_delete_header_server(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Server"]
    expected = env.user_list["header"]["server"]
    assert actual == expected, \
        f"Header Server is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.regression
def test_delete_header_x_powered_by(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["X-Powered-By"]
    expected = env.user_list["header"]["x_powered_by"]
    assert actual == expected, \
        f"Header X-Powered-By is not as expected\nActual: {actual}\nExpected: {expected}"


@pytest.mark.smoke
@pytest.mark.regression
def test_delete_header_via(base_page, env):
    request = delete(f"{base_page.base_url()}/{{1}}")
    response = request.headers
    actual = response["Via"]
    expected = env.user_list["header"]["via"]
    assert actual == expected, \
        f"Header Via is not as expected\nActual: {actual}\nExpected: {expected}"

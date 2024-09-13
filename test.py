import pytest
from main import github_user
from main import get_weather
from main import get_random_cat_image

def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }
    api_key = 'fb84801abe556d0fa5a829305ddd718d'
    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data['weather'][0]['description'] == 'clear sky'
    assert weather_data['main']['temp'] == 273.15


def test_get_weather_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    api_key = 'fb84801abe556d0fa5a829305ddd718d'
    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data is None


def test_get_github_user(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'nizavr',
        'id': '345178',
        'name': 'Oleg'
    }

    user_data = github_user('nizavr')
    assert user_data == {
        'login': 'nizavr',
        'id': '345178',
        'name': 'Oleg'
    }

def test_get_github_user_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    user_data = github_user('nizavr')
    assert user_data == None


def test_get_random_cat_image(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/abcd1234.jpg'}
    ]

    cat_image_url = get_random_cat_image()
    assert cat_image_url == 'https://cdn2.thecatapi.com/images/abcd1234.jpg'


def test_get_random_cat_image_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    cat_image_url = get_random_cat_image()
    assert cat_image_url is None

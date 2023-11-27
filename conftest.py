import json
import os

import pytest

from utilities.base_page import BasePage
from utilities.configurations import Configurations


@pytest.fixture(scope="module")
def env():
    """Implementation of a .json config"""
    config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'configurations/config.json'))

    print("Config file path:", config_file_path)

    if os.path.exists(config_file_path):
        with open(config_file_path) as file:
            env_dict = json.loads(file.read())
        return Configurations(**env_dict)
    else:
        raise FileNotFoundError("Error: 'config.json' file not found.")


@pytest.fixture()
def base_page(env):
    return BasePage(env)

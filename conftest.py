#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from mocks.mock_user import MockUser
from mocks.oneanddone_api import OneAndDoneAPI

@pytest.fixture(scope='function')
def new_user(request):
    personatestuser_uri = 'http://personatestuser.org/email'
    
    mozwebqa = request.getfuncargvalue('mozwebqa')
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_user'], credentials['api_key'], mozwebqa.base_url)

    # Request TestUser credentials from http://personatestuser.org
    try:
        response = requests.get(personatestuser_uri)
    except requests.exceptions.RequestException as error:
        print error
        return None

    def fin():
        # delete user after the test from database using API
        if request.new_user:
            api.delete_user(request.new_user)

    request.addfinalizer(fin)
    testuser = response.json()
    return MockUser(email = testuser['email'], password = testuser['pass'])

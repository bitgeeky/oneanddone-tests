#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from mocks.mock_user import MockUser


@pytest.fixture(scope='function')
def new_user():
    personatestuser_uri = 'http://personatestuser.org/email'
    
    # Request TestUser credentials from http://personatestuser.org
    try:
        response = requests.get(personatestuser_uri)
    except requests.exceptions.RequestException as error:
        print error
        return None

    def fin():
        # delete user after the test from database using API
        pass

    testuser = response.json()
    return MockUser(email = testuser['email'], password = testuser['pass'])

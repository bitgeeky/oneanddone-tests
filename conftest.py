#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from mocks.mock_user import MockUser
from mocks.mock_task import MockTask
from utils.oneanddone_api import OneAndDoneAPI


def get_personatestuser():
    # Request TestUser credentials from http://personatestuser.org
    personatestuser_uri = 'http://personatestuser.org/email'
    response = requests.get(personatestuser_uri)
    return response.json()


def delete_user_from_database(mozwebqa, user):
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
    api.delete_user(user)


def create_user_in_database(mozwebqa, user):
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
    return api.create_user(user)


def delete_task_from_database(mozwebqa, task):
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
    api.delete_task(task)


def create_task_in_database(mozwebqa, task):
    credentials = mozwebqa.credentials['default']
    api = OneAndDoneAPI(credentials['api_token'], mozwebqa.base_url)
    return api.create_task(task)


@pytest.fixture(scope='function')
def existing_user(request):
    class UserFactory(object):
        def get(self):
            testuser = get_personatestuser()
            mozwebqa = request.getfuncargvalue('mozwebqa')
            username = testuser['email'].split('@')[0]
            existing_user = create_user_in_database(
                mozwebqa, MockUser(
                    email=testuser['email'],
                    username=username,
                    password=testuser['pass'],
                    profile={'name': 'mozwebqa_testuser',
                             'username': username,
                             'privacy_policy_accepted': True}
                )
            )
            def fin():
                delete_user_from_database(mozwebqa, existing_user)

            request.addfinalizer(fin)
            return existing_user

    return UserFactory()


@pytest.fixture(scope='function')
def new_user(request):
    testuser = get_personatestuser()
    request.new_user = MockUser(
        email=testuser['email'],
        username=testuser['email'].split('@')[0],
        password=testuser['pass']
    )

    def fin():
        # Delete user from application database after the test
        if request.new_user:
            mozwebqa = request.getfuncargvalue('mozwebqa')
            delete_user_from_database(mozwebqa, request.new_user)

    request.addfinalizer(fin)
    return request.new_user


@pytest.fixture(scope='function')
def tasks_for_test_one_time_task(request):
    mozwebqa = request.getfuncargvalue('mozwebqa')
    request.tasks_for_test_one_time_task = create_task_in_database(
        mozwebqa, MockTask(repeatable = False)
    )

    def fin():
        # Delete tasks from application database after the test
        if request.tasks_for_test_one_time_task:
            delete_task_from_database(
                mozwebqa,
                request.tasks_for_test_one_time_task
            )

    request.addfinalizer(fin)
    return request.tasks_for_test_one_time_task


@pytest.fixture(scope='function')
def tasks_for_test_taken_one_time_task(request, existing_user):
    existing_user = existing_user.get()
    mozwebqa = request.getfuncargvalue('mozwebqa')
    taskattempt_set = [{"user": existing_user['email'], "state": 0}]
    request.tasks_for_test_taken_one_time_task = create_task_in_database(
        mozwebqa, MockTask(repeatable = False, taskattempt_set=taskattempt_set)
    )

    def fin():
        # Delete tasks from application database after the test
        if request.tasks_for_test_taken_one_time_task:
            delete_task_from_database(
                mozwebqa,
                request.tasks_for_test_taken_one_time_task
            )

    request.addfinalizer(fin)
    return request.tasks_for_test_taken_one_time_task

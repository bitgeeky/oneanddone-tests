#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

from unittestzero import Assert
import requests


class OneAndDoneAPI:

    def __init__(self, username, api_key, base_url):
        self.params = {
            u'username': unicode(username),
            u'api_key': unicode(api_key),
            u'format': u'json',
        }
        self.base_url = base_url
        self.headers = {'content-type': 'application/json'}

    def _do_delete(self, uri, lookup_field):
        """Make a Delete Request"""
        response = requests.delete(
            "%s/%s/%s" % (self.base_url, uri, lookup_field),
            params=self.params,
            headers=self.headers)
        response.raise_for_status()
        if response.status_code == 204:
            return True
        else:
            print "Failed to delete resource: %s with %s.\n%s" % (
                lookup_field, response.status_code, response.text)
            return False

    def delete_user(self, user):
        uri = 'api/v1/users'
        self.params['permanent'] = True
        Assert.true(self._do_delete(uri, user['email']), 'Deletion of user with email %s failed' % user['email'])

#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class MockTask(dict):

    def __init__(self, **kwargs):

        self['id'] = None
        self['name'] = 'Sample Task'
        self['short_description'] = 'Task Desc'
        self['instructions'] = 'Task Inst'
        self['prerequisites'] = 'Task Prerequisite'
        self['execution_time'] = 30
        self['is_draft'] = False
        self['project'] = 'Automation'
        self['team'] = 'Web QA'
        self['type'] = 'Automated test'
        self['repeatable'] = True
        self['start_date'] = None
        self['end_date'] = None
        self['difficulty'] = 1
        self['why_this_matters'] = 'Task matters'
        self['keyword_list'] = ['testing', 'webqa', 'automation']
        self['taskattempt_set'] = []

        self.update(**kwargs)

    def ___getattr__(self, attr):
        return self[attr]

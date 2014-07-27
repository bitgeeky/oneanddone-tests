#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from pages.tasks.available_tasks import AvailableTasksPage

from unittestzero import Assert
import pytest
from time import sleep

class TestTaskFilter:

    @pytest.mark.credentials
    def test_filter_tasks_according_to_estimated_time(self, mozwebqa, tasks_for_filter_tasks_according_to_estimated_time):
        available_tasks_page = AvailableTasksPage(mozwebqa)
        available_tasks_page.go_to_page()
        available_tasks_page.enter_search_keyword(tasks_for_filter_tasks_according_to_estimated_time[0]['keyword_list'][0])
        available_tasks_page.click_filter_tasks_button()

        Assert.false(available_tasks_page.is_fifteen_min_checkbox_checked)
        Assert.false(available_tasks_page.is_thirty_min_checkbox_checked)
        Assert.false(available_tasks_page.is_fourty_five_min_checkbox_checked)
        Assert.false(available_tasks_page.is_sixty_min_checkbox_checked)

        Assert.true(len(available_tasks_page.available_tasks) == 4)

        # click only fifteen min option
        available_tasks_page.toggle_fifteen_min_checkbox()
        available_tasks_page.click_filter_tasks_button()
        Assert.true(len(available_tasks_page.available_tasks) == 1)

        # click only fourty five  min option
        available_tasks_page.toggle_fifteen_min_checkbox()
        Assert.false(available_tasks_page.is_fifteen_min_checkbox_checked)
        available_tasks_page.toggle_fourty_five_min_checkbox()
        available_tasks_page.click_filter_tasks_button()
        Assert.true(len(available_tasks_page.available_tasks) == 2)

        # click both fifteen and thirty min option
        available_tasks_page.toggle_fourty_five_min_checkbox()
        Assert.false(available_tasks_page.is_fourty_five_min_checkbox_checked)
        available_tasks_page.toggle_fifteen_min_checkbox()
        available_tasks_page.toggle_thirty_min_checkbox()
        available_tasks_page.click_filter_tasks_button()
        Assert.true(len(available_tasks_page.available_tasks) == 2)

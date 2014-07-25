#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage
from pages.tasks.task_details import TaskDetailsPage

from unittestzero import Assert
import pytest


class TestTasks:

    @pytest.mark.credentials
    def test_that_one_time_task_is_marked_completed_on_completion(self, mozwebqa, existing_user, tasks_for_test_one_time_task):
        existing_user = existing_user.get()
        task_details_page = TaskDetailsPage(mozwebqa)
        task_details_page.go_to_page(tasks_for_test_one_time_task['id'])

        login_required_page = task_details_page.click_get_started_button('login_required')
        task_details_page = login_required_page.click_persona_login_button(existing_user)
        task_details_page.click_get_started_button()
        Assert.true(task_details_page.is_save_for_later_button_visible)

        home_page = task_details_page.click_logo_container()
        Assert.true(home_page.is_task_in_progress)

        task_details_page.go_to_page(tasks_for_test_one_time_task['id'])
        task_feedback_page = task_details_page.click_complete_task_button()
        Assert.true(task_feedback_page.is_the_current_page)

        logged_in_home_page_after_task_completion = task_feedback_page.click_no_thanks_button()
        user_profile_details_page = logged_in_home_page_after_task_completion.header.click_user_profile_details()
        Assert.true(user_profile_details_page.is_the_current_page)

        Assert.equal(user_profile_details_page.diplayed_completed_tasks_count, 1)
        Assert.equal(len(user_profile_details_page.completed_tasks), 1)
        Assert.equal(user_profile_details_page.completed_tasks[0].name, tasks_for_test_one_time_task['name'])

        task_details_page = user_profile_details_page.completed_tasks[0].click()
        Assert.true(task_details_page.is_completed_button_visible)

    @pytest.mark.credentials
    def test_taken_one_time_task_cannot_be_taken_by_different_user(self, mozwebqa, existing_user, tasks_for_test_taken_one_time_task):
        existing_user = existing_user.get()
        task_details_page = TaskDetailsPage(mozwebqa)
        task_details_page.go_to_page(tasks_for_test_taken_one_time_task['id'])
        Assert.true(task_details_page.is_taken_button_visible)

        login_required_page = task_details_page.click_get_started_button('login_required')
        task_details_page = login_required_page.click_persona_login_button(existing_user)
        Assert.true(task_details_page.is_taken_button_visible)

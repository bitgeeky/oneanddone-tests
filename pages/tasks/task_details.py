#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.page import PageRegion
from pages.tasks.task_feedback import TaskFeedbackPage


class TaskDetailsPage(Base):

    _name_locator = (By.CSS_SELECTOR, '.content-container > h1')

    _get_started_button_locator = (By.ID, 'get-started')
    _save_for_later_button_locator = (By.ID, 'save-for-later')
    _abandon_task_button_locator = (By.ID, 'abandon-task')
    _complete_task_button_locator = (By.ID, 'complete-task')

    @property
    def _page_title(self):
        return '%s | Mozilla One and Done' % self.name

    @property
    def name(self):
        return self.selenium.find_element(*self._name_locator).text

    @property
    def is_completed_button_visible(self):
        return self.selenium.find_element(*self._get_started_button_locator).text == 'Completed'

    @property
    def is_taken_button_visible(self):
        return self.selenium.find_element(*self._get_started_button_locator).text == 'Taken'

    @property
    def is_get_started_button_visible(self):
        return self.is_element_visible(*self._get_started_button_locator)

    @property
    def is_save_for_later_button_visible(self):
        return self.is_element_visible(*self._save_for_later_button_locator)

    @property
    def is_abandon_task_button_visible(self):
        return self.is_element_visible(*self._abandon_task_button_locator)

    @property
    def is_complete_task_button_visible(self):
        return self.is_element_visible(*self._complete_task_button_locator)

    @property
    def is_get_started_button_not_visible(self):
        return self.is_element_not_visible(*self._get_started_button_locator)

    @property
    def is_save_for_later_button_not_visible(self):
        return self.is_element_not_visible(*self._save_for_later_button_locator)

    @property
    def is_abandon_task_button_not_visible(self):
        return self.is_element_not_visible(*self._abandon_task_button_locator)

    @property
    def is_complete_task_button_not_visible(self):
        return self.is_element_not_visible(*self._complete_task_button_locator)

    def go_to_page(self, task_id):
        self.selenium.get(self.base_url + '/tasks/%d/'%task_id)
        self.is_the_current_page

    def click_get_started_button(self, expected_page='task_details'):
        self.selenium.find_element(*self._get_started_button_locator).click()
        if expected_page == 'login_required':
            from pages.login_required import LoginRequiredPage
            return LoginRequiredPage(self.testsetup)

    def click_save_for_later_button(self):
        self.selenium.find_element(*self._save_for_later_button_locator).click()
        from pages.home import HomePage
        return HomePage(self.testsetup)

    def click_complete_task_button(self):
        self.selenium.find_element(*self._complete_task_button_locator).click()
        return TaskFeedbackPage(self.testsetup)

    def click_abandon_task_button(self):
        self.selenium.find_element(*self._abandon_task_button_locator).click()
        return TaskFeedbackPage(self.testsetup)

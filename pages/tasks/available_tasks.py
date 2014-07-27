#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.page import PageRegion
from pages.tasks.task_details import TaskDetailsPage


class AvailableTasksPage(Base):

    _page_title = 'Tasks | Mozilla One and Done'

    _displayed_profile_name_locator = (By.CSS_SELECTOR, '.content-container > h3')
    _available_tasks_list_locator = (By.CSS_SELECTOR, '.task-list > li')
    _search_textbox_locator = (By.ID, 'id_search')
    _filter_tasks_button_locator = (By.ID, 'filter-tasks')
    _fifteen_min_checkbox_locator = (By.ID, 'id_execution_time_0')
    _thirty_min_checkbox_locator = (By.ID, 'id_execution_time_1')
    _fourty_five_min_checkbox_locator = (By.ID, 'id_execution_time_2')
    _sixty_min_checkbox_locator = (By.ID, 'id_execution_time_3')

    @property
    def displayed_profile_name(self):
        return self.selenium.find_element(*self._displayed_profile_name_locator).text

    @property
    def available_tasks(self):
        return [self.Task(self.testsetup, web_element)
                for web_element in self.selenium.find_elements(*self._available_tasks_list_locator)]

    @property
    def is_fifteen_min_checkbox_checked(self):
        return self.selenium.find_element(*self._fifteen_min_checkbox_locator).is_selected()

    @property
    def is_thirty_min_checkbox_checked(self):
        return self.selenium.find_element(*self._thirty_min_checkbox_locator).is_selected()

    @property
    def is_fourty_five_min_checkbox_checked(self):
        return self.selenium.find_element(*self._fourty_five_min_checkbox_locator).is_selected()

    @property
    def is_sixty_min_checkbox_checked(self):
        return self.selenium.find_element(*self._sixty_min_checkbox_locator).is_selected()

    def go_to_page(self):
        self.selenium.get(self.base_url + '/tasks/available/')
        self.is_the_current_page

    def enter_search_keyword(self, keyword):
        self.type_in_element(self._search_textbox_locator, keyword)

    def click_filter_tasks_button(self):
        self.selenium.find_element(*self._filter_tasks_button_locator).click()

    def toggle_fifteen_min_checkbox(self):
        self.selenium.find_element(*self._fifteen_min_checkbox_locator).click()

    def toggle_thirty_min_checkbox(self):
        self.selenium.find_element(*self._thirty_min_checkbox_locator).click()

    def toggle_fourty_five_min_checkbox(self):
        self.selenium.find_element(*self._fourty_five_min_checkbox_locator).click()

    def toggle_sixty_min_checkbox(self):
        self.selenium.find_element(*self._sixty_min_checkbox_locator).click()

    class Task(PageRegion):
        _name_locator = (By.CSS_SELECTOR, 'a.task-name')

        @property
        def name(self):
            return self.find_element(*self._name_locator).text

        def click(self):
            self.find_element(*self._name_locator).click()
            return TaskDetailsPage(self.testsetup)

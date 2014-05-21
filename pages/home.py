#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.page import Page
from base import Base


class HomePage(Base):

    _page_title = 'Mozilla One and Done'

    def go_to_page(self):
        self.selenium.get(self.base_url + '/')
        self.is_the_current_page

    @property
    def create_profile_page(self):
        return self.CreateProfilePage(self.testsetup)

    class CreateProfilePage(Page):
        """
        Page displayed to user without a Profile
        """
        _name_text_field_locator = (By.CSS_SELECTOR, '.edit-profile #id_name')
        _save_button_locator = (By.CSS_SELECTOR, '.edit-profile > .actions-container > .button')

        def enter_name(self, fullname):
            self.type_in_element(self._name_text_field_locator, fullname)

        def click_save_button(self):
            self.selenium.find_element(*self._save_button_locator).click()

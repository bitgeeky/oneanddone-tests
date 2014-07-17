#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from browserid import BrowserID

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.tasks.task_details import TaskDetailsPage


class LoginRequiredPage(Base):

    _page_title = 'Login required | Mozilla One and Done'

    _persona_login_button = (By.CSS_SELECTOR, 'p.auth-menu > a.browserid-login.persona-button.blue')

    def click_persona_login_button(self, user):
        self.selenium.find_element(*self._persona_login_button).click()
        browser_id = BrowserID(self.selenium, self.timeout)
        browser_id.sign_in(user['email'], user['password'])
        self.wait_for_element_visible(*self._logout_menu_item_locator)
        from pages.tasks.task_details import TaskDetailsPage
        return TaskDetailsPage(self.testsetup)


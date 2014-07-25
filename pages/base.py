#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from browserid import BrowserID

from selenium.webdriver.common.by import By

from pages.page import Page


class Base(Page):

    _logo_container_locator = (By.ID, 'logo-container')
    _browserid_login_locator = (By.CSS_SELECTOR, '.browserid-login > span')
    _logout_menu_item_locator = (By.CSS_SELECTOR, '.auth-menu > .browserid-logout')

    @property
    def header(self):
        return self.HeaderRegion(self.testsetup)

    @property
    def is_user_logged_in(self):
        return self.is_element_not_visible(*self._browserid_login_locator)

    def login(self, user, expectation):
        self.click_browserid_login()
        browser_id = BrowserID(self.selenium, self.timeout)
        browser_id.sign_in(user['email'], user['password'])
        self.wait_for_element_visible(*self._logout_menu_item_locator)
        return self.expected_page(expectation)

    def logout(self):
        self.selenium.find_element(*self._logout_menu_item_locator).click()

    def expected_page(self, expectation):
        if expectation == 'user_profile':
            from pages.user.user_profile_edit import UserProfileEditPage
            return UserProfileEditPage(self.testsetup)
        elif expectation == 'home_page':
            from pages.home import HomePage
            return HomePage(self.testsetup)

    def click_browserid_login(self):
        self.selenium.find_element(*self._browserid_login_locator).click()

    def click_logo_container(self):
        self.selenium.find_element(*self._logo_container_locator).click()
        from pages.home import HomePage
        return HomePage(self.testsetup)

    class HeaderRegion(Page):

        _auth_menu_locator = (By.CSS_SELECTOR, '#nav-main-menu .auth-menu')
        _user_profile_details_locator = (By.ID, 'view-profile')

        @property
        def diplayed_text(self):
            return self.selenium.find_element(*self._auth_menu_locator).text

        def click_user_profile_details(self):
            self.selenium.find_element(*self._user_profile_details_locator).click()
            from pages.user.user_profile_details import UserProfileDetailsPage
            return UserProfileDetailsPage(self.testsetup)

#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest


class TestSignIn:

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    def test_sign_in_for_new_user(self, mozwebqa, new_user):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.false(home_page.is_signed_in)

        home_page.sign_in(new_user)
        Assert.true(home_page.is_signed_in)

        create_profile_page = home_page.create_profile_page
        create_profile_page.enter_name("Test User")
        create_profile_page.click_save_button()

        Assert.true("Test User" in home_page.header.diplayed_text)

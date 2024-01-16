from utilities.Utils import PageUtils
import time
from dataProvider.base import Base


class homepage(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
    check_in = ('xpath', "//*[contains(@content-desc, 'Check-In')]")
    no_thanks = ('xpath', '//android.widget.Button[@content-desc="No, thank you"]')
    yes_agree = ('xpath', '//android.widget.Button[@content-desc="Yes, I agree"]')
    how_to_play = ('xpath', "//*[contains(@content-desc, 'How to play')]")
    start_your_journey = ('xpath', "//*[contains(@content-desc, 'Start your journey')]")
    australia = ('xpath', "//*[contains(@content-desc, 'Australia')]")
    india = ('xpath', "//*[contains(@content-desc, 'India')]")
    playnow = ('xpath', "//*[contains(@content-desc, 'Play Now')]")
    gamepage = ('xpath', "//*[contains(@content-desc, 'Complete')]")
    home = ('xpath', '//android.widget.ImageView[@content-desc="Home"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    information = ('xpath', '//android.widget.ImageView[@content-desc="Information"]')
    settings = ('xpath', '//android.widget.ImageView[@content-desc="Settings"]')
    sound = ('xpath', '//android.view.View[@content-desc="Sounds"]')
    haptics = ('xpath', '//android.view.View[@content-desc="Haptics"]')
    progress_default = ('xpath', "//*[contains(@content-desc, 'No data yet')]")
    brain_health = ('xpath', "//*[contains(@content-desc, 'Brain Health')]")
    settings_researchdata = ('xpath', "//*[contains(@content-desc, 'Research data collection')]")
    Start_checkin = ('xpath', '//android.widget.Button[@content-desc="Start Check-In"]')
    settingsheader = ('xpath', "//*[contains(@content-desc, 'Settings')]")
    ulock_devlopermode = ('xpath', '//android.view.View[@content-desc="Unlock Developer Mode?"]')
    password = ('xpath', "//android.widget.EditText[@index='0']")
    unlock_button = ('xpath', '//android.widget.Button[@content-desc="Unlock"]')
    cancel_button = ('xpath', '//android.widget.Button[@content-desc="Cancel"]')
    test_access = ('xpath', "//*[contains(@content-desc, 'Tester Access')]")
    testeraccess_toggle = (
    'xpath', "//android.view.View/android.view.View/android.view.View[9]/android.view.View/android.view.View[3]")
    testeraccess_warning = ('xpath', '//android.view.View[@content-desc=" If you turn off tester mode, you will lose '
                                     'all your data. Do you wish to proceed?"]')

    def click_next_btn(self):
        self.action_perform(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_testeraccess(self):
        self.action_perform(self.testeraccess_toggle)

    def click_unlock(self):
        self.action_perform(self.unlock_button)

    def click_password(self):
        self.click(self.password)

    def tap_password(self):
        self.action_perform(self.password)

    def enter_password(self, pwd):
        self.set_value(self.password, pwd)

    def click_settingsheader(self):
        x = 247
        y = 242
        self.tap_by_cordinates(x, y)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_settings(self):
        self.click(self.settings)
        # self.action_perform(self.settings)

    def click_checkin(self):
        self.action_perform(self.check_in)

    def click_progress(self):
        self.click(self.progress)

    def click_information(self):
        self.click(self.information)

    def click_start_checkin(self):
        self.action_perform(self.Start_checkin)
        time.sleep(.5)

    def check_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def how_to_play_button_removed(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        return self.is_visible(self.how_to_play)

    def start_your_journey_validation(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(3)
        result = self.page_utils.is_element_present(self.start_your_journey)
        print(result)
        return result

    def test(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(3)
        self.swipeing(self.india)
        self.action_perform(self.india)
        time.sleep(4)

    def verify_playnow_button(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(3)
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            if self.page_utils.is_element_present(self.gamepage):
                return True

    def verify_homepage_menu(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(3)
        if self.page_utils.is_element_present(self.home) and self.page_utils.is_element_present(
                self.progress) and self.page_utils.is_element_present(
            self.information) and self.page_utils.is_element_present(self.settings):
            return True

    def verify_sound_and_haptics_settings(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(3)
        if self.page_utils.is_element_present(self.settings):
            self.click_settings()
            if self.page_utils.is_element_present(self.settings) and self.page_utils.is_element_present(self.haptics):
                return True

    def verify_progress_default(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(3)
        self.click_progress()
        return self.page_utils.is_element_present(self.progress_default)

    def verify_information_page(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(2)
        self.click_information()
        for item in content:
            if self.check_element(item):
                result = True
        return result

    def verify_settings_devlopermode(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(5)
        self.click_settings()
        time.sleep(3)
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        if self.page_utils.is_element_present(self.ulock_devlopermode):
            if self.page_utils.is_element_present(self.unlock_button) and self.page_utils.is_element_present(
                    self.cancel_button):
                return True

    def verify_countrybased_Settings(self, pwd):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(5)
        self.click_settings()
        time.sleep(3)
        self.click_settingsheader()
        time.sleep(1)
        self.click_settingsheader()
        time.sleep(1)
        self.click_settingsheader()
        time.sleep(1)
        self.click_settingsheader()
        time.sleep(1)
        self.click_settingsheader()
        time.sleep(1)
        self.click_settingsheader()
        time.sleep(1)
        if self.page_utils.is_element_present(self.ulock_devlopermode):
            # self.click_password()
            self.tap_password()
            print(pwd)
            self.enter_password(pwd)
            time.sleep(3)

            self.click_unlock()
            return self.page_utils.is_element_present(self.test_access)

    def verify_settings_unlock(self, pwd):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(5)
        self.click_settings()
        time.sleep(3)
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        if self.page_utils.is_element_present(self.ulock_devlopermode):
            # self.click_password()
            self.tap_password()
            print(pwd)
            self.enter_password(pwd)
            time.sleep(3)

            self.click_unlock()
            return self.page_utils.is_element_present(self.test_access)

    def verify_settings_tester_access_toggle(self, pwd):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(5)
        self.click_settings()
        time.sleep(3)
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        self.click_settingsheader()
        if self.page_utils.is_element_present(self.ulock_devlopermode):
            # self.click_password()
            self.tap_password()
            print(pwd)
            self.enter_password(pwd)
            time.sleep(3)

            self.click_unlock()
            self.click_testeraccess()
            return self.page_utils.is_element_present(self.testeraccess_warning)

    def verify_clockin_progress(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(6)
        self.click_progress()
        if self.page_utils.is_element_present(self.progress_default):
            return self.page_utils.get_system_bar()

    def verify_clockin_information(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(6)
        self.click_information()
        if self.page_utils.is_element_present(self.brain_health):
            return self.page_utils.get_system_bar()

    def verify_clockin_settings(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        time.sleep(6)
        self.click_settings()
        if self.page_utils.is_element_present(self.settings_researchdata):
            return self.system_bar()

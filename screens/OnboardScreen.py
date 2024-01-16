import time
from dataProvider.base import Base


class onboardscreen(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
    no_thanks = ('xpath', '//android.widget.Button[@content-desc="No, thank you"]')
    yes_agree = ('xpath', '//android.widget.Button[@content-desc="Yes, I agree"]')
    how_to_play = ('xpath', "//*[contains(@content-desc, 'How to play')]")
    start_your_journey = ('xpath', "//*[contains(@content-desc, 'Start your journey')]")
    australia = ('xpath', "//*[contains(@content-desc, 'Australia')]")
    india = ('xpath', "//*[contains(@content-desc, 'India')]")
    select_year = ('xpath', '//android.widget.Button[@content-desc="Year Select"]')
    done = ('xpath', '//android.view.View[@content-desc="Done"]')
    slpash = ('xpath', "//*[contains(@content-desc, 'BrainTrack Explore your brain health')]")


    def click_next_btn(self):
        self.action_perform(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def verify_select_fields(self, data):

        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        return self.page_utils.is_element_present(value)

    def wait_for_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        return self.wait_visible(value)

    def verify_splash_screen(self):
        return self.is_element_present(self.slpash)

    def verify_onboardscreen(self, msg1, msg2, msg3, msg4, msg5):
        self.wait_for_element(msg1)
        if self.verify_select_fields(msg1):
            self.click_next_btn()
            if self.verify_select_fields(msg2):
                self.click_next_btn()
                if self.verify_select_fields(msg3):
                    self.click_next_btn()
                    if self.verify_select_fields(msg4):
                        self.click_next_btn()
                        if self.verify_select_fields(msg5):
                            return True
        else:
            return False

    def verify_help_our_research_screen(self, help_research):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        time.sleep(3)
        return self.verify_select_fields(help_research)

    def verify_home_page(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()

    def settings(self):
        self.change_accebility()

import time
from dataProvider.base import Base


class checkin(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
    no_thanks = ('xpath', '//android.widget.Button[@content-desc="No, thank you"]')
    yes_agree = ('xpath', '//android.widget.Button[@content-desc="Yes, I agree"]')
    how_to_play = ('xpath', "//*[contains(@content-desc, 'How to play')]")
    start_your_journey = ('xpath', "//*[contains(@content-desc, 'Start your journey')]")
    australia = ('xpath', "//*[contains(@content-desc, 'Australia')]")
    playnow = ('xpath', "//*[contains(@content-desc, 'Play Now')]")
    gamepage = ('xpath', "//*[contains(@content-desc, 'Complete')]")
    home = ('xpath', '//android.widget.ImageView[@content-desc="Home"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    information = ('xpath', '//android.widget.ImageView[@content-desc="Information"]')
    settings = ('xpath', '//android.widget.ImageView[@content-desc="Settings"]')
    lets_play = ('xpath', '//android.widget.Button[@content-desc="Let’s Play"]')
    tutorial = ('xpath', '//android.view.View[@content-desc="Tutorial"]')
    done = ('xpath', '//android.widget.Button[@content-desc="Done"]')
    check_in = ('xpath', "//*[contains(@content-desc, 'Check-In')]")
    Checkin_header = ('xpath', '//android.view.View[@content-desc="Check-In"]')
    Start_checkin = ('xpath', '//android.widget.Button[@content-desc="Start Check-In"]')
    checkin_recommentations = (
        'xpath', "//*[contains(@content-desc, 'Here are some recommendations based on your check-in')]")
    sent_results = ('xpath', '//android.widget.Button[@content-desc="Send Results"]')
    exportpdf = ('xpath', "//android.widget.Button[@index='2']")
    pdfreportname = ('xpath', "//*[contains(@text, 'BrainTrack_Report.pdf')]")
    progress_checkin = ('xpath', "//*[contains(@content-desc, 'Last check-in')]")

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_checkin(self):
        self.action_perform(self.check_in)

    def click_sentresult(self):
        self.action_perform(self.sent_results)

    def click_progress(self):
        self.click(self.progress)

    def click_exportpdf(self):
        self.click(self.exportpdf)

    def check_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def click_start_checkin(self):
        self.action_perform(self.Start_checkin)
        time.sleep(.5)

    def tap_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        self.action_perform(value)
        time.sleep(.5)

    def check_element_swipe(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.swipeing(value)
        return self.page_utils.is_element_present(value)

    def verify_checkin_landing(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_checkin()
            if self.page_utils.is_element_present(self.Checkin_header) and self.page_utils.is_element_present(
                    self.Start_checkin) and self.check_element(description):
                return True
            else:
                return False

    def verify_checkin_game(self, quiz_questions, quiz_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_checkin()
            self.click_start_checkin()
            for item in quiz_questions:
                if self.check_element(item):
                    for items in quiz_answer:
                        self.tap_element(items)
                        self.click_next_btn()
                    return self.page_utils.is_element_present(self.checkin_recommentations)

    def verify_checkin_results(self, quiz_questions, quiz_answer, quiz_Insight, quiz_Recommentation):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_checkin()
            self.click_start_checkin()
            for item in quiz_questions:
                if self.check_element(item):
                    for items in quiz_answer:
                        self.tap_element(items)
                        self.click_next_btn()
                print(quiz_Insight, quiz_Recommentation)
                if self.is_element_present(self.checkin_recommentations):
                    for item in quiz_Insight:
                        self.check_element_swipe(item)
                #if self.check_element_swipe(item2):

    def verify_checkin_game_progress(self, quiz_questions, quiz_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_checkin()
            self.click_start_checkin()
            for item in quiz_questions:
                if self.check_element(item):
                    for items in quiz_answer:
                        self.tap_element(items)
                        self.click_next_btn()

                self.click_done()
                self.back()
                self.click_progress()
                return self.page_utils.is_element_present(self.progress_checkin)

    def verify_checkin_game_generatepdf(self, quiz_questions, quiz_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_checkin()
            self.click_start_checkin()
            for item in quiz_questions:
                if self.check_element(item):
                    for items in quiz_answer:
                        self.tap_element(items)
                        self.click_next_btn()

                self.click_done()
                self.back()
                time.sleep(2)
                self.click_progress()
                self.click_sentresult()
                time.sleep(10)
                self.click_exportpdf()
                if self.page_utils.is_element_present(self.pdfreportname):
                    self.back()
                    return True

    def verify_checkin_game_clock(self, quiz_questions, quiz_answer):
        if self.system_bar():
            self.click_next_btn()
            if self.system_bar():
                self.click_next_btn()
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_next_btn()
                            if self.system_bar():
                                self.click_nothanks()
                                if self.page_utils.is_element_present(self.australia):
                                    if self.system_bar():
                                        self.click_playnow()
                                        if self.system_bar():
                                            self.click_checkin()
                                            if self.system_bar():
                                                self.click_start_checkin()
                                                for item in quiz_questions:
                                                    if self.check_element(item):
                                                        for items in quiz_answer:
                                                            self.tap_element(items)
                                                            if self.system_bar():
                                                                self.click_next_btn()
                                                            else:
                                                                break
                                                        if self.page_utils.is_element_present(
                                                                self.checkin_recommentations):
                                                            return self.system_bar()

from lxml.etree import tounicode

from utilities.Utils import PageUtils
import time
from dataProvider.base import Base


class country(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
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
    check_in = ('xpath', "//*[contains(@content-desc, 'Check-In')]")
    baggage_claim = ('xpath', "//*[contains(@content-desc, 'Baggage Claim')]")
    meetandgreet = ('xpath', "//*[contains(@content-desc, 'Meet & Greet')]")
    marketplace = ('xpath', "//*[contains(@content-desc, 'Marketplace')]")
    play_marketplace = ('xpath', "//*[contains(@content-desc, 'Play Marketplace')]")
    play_baggage_claim = ('xpath', "//*[contains(@content-desc, 'Play Baggage Claim')]")
    Checkin_header = ('xpath', '//android.view.View[@content-desc="Check-In"]')
    Start_checkin = ('xpath', '//android.widget.Button[@content-desc="Start Check-In"]')
    checkin_recommentations = (
        'xpath', "//*[contains(@content-desc, 'Here are some recommendations based on your check-in')]")
    lets_play = ('xpath', '//android.widget.Button[@content-desc="Let’s Play"]')
    tutorial = ('xpath', '//android.view.View[@content-desc="Tutorial"]')
    start_round = ('xpath', "//*[contains(@content-desc, 'Start Round 1')]")
    play_meetandgreet = ('xpath', '//android.widget.Button[@content-desc="Play Meet & Greet"]')
    next = ('xpath', "//*[contains(@content-desc, 'Next')]")
    close = ('xpath',
             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View')
    done = ('xpath', '//android.widget.Button[@content-desc="Done"]')
    progress_checkin = ('xpath', "//*[contains(@content-desc, 'Last check-in')]")
    sent_results = ('xpath', '//android.widget.Button[@content-desc="Send Results"]')
    exportpdf = ('xpath', "//android.widget.Button[@index='2']")
    pdfreportname = ('xpath', "//*[contains(@text, 'BrainTrack_Report.pdf')]")
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    click_image = ('xpath',
                   '//android.view.View[@content-desc="Who is not in this tour group?"]/android.view.View/android.view.View/android.view.View[2]')
    takeabreak = ('xpath', '//android.view.View[@content-desc="Take a break"]')
    video_in_takeabreak = ('xpath', '//android.view.View[@content-desc="00:00 / 00:58"]/android.view.View[1]')
    meetandgreet_result = ('xpath', '//android.widget.Button[@content-desc="Great work!"]')
    meetandgreet_round1_result = ('xpath', '(//android.view.View[@content-desc="100"])[1]')
    meetandgreet_round2_result = ('xpath', '(//android.view.View[@content-desc="100"])[2]')

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_done(self):
        self.action_perform(self.done)

    def click_sentresult(self):
        self.action_perform(self.sent_results)

    def click_exportpdf(self):
        self.click(self.exportpdf)

    def click_secondimagestep2(self):
        self.click(self.click_image)

    def click_progress(self):
        self.click(self.progress)

    def click_start_checkin(self):
        self.action_perform(self.Start_checkin)
        time.sleep(.5)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_close(self):
        self.action_perform(self.close)

    def click_quit(self):
        self.action_perform(self.quit)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_checkin(self):
        self.action_perform(self.check_in)

    def click_baggagecliam(self):
        self.action_perform(self.baggage_claim)

    def click_meetandgreet(self):
        self.action_perform(self.meetandgreet)

    def click_playmeetandgreet(self):
        self.action_perform(self.play_meetandgreet)

    def click_play_baggagecliam(self):
        self.action_perform(self.play_baggage_claim)

    def click_marketplace(self):
        self.action_perform(self.marketplace)

    def click_play_marketplace(self):
        self.action_perform(self.play_marketplace)

    def click_letsplay(self):
        self.action_perform(self.lets_play)

    def check_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def click_imageinmeetandgreet(self, data):
        value = ('xpath',
                 "//android.view.View[@content-desc='" + data + "']/android.view.View/android.view.View/android.view.View[2]")
        self.click(value)

    def check_element_swipe(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.swipeing(value)
        return self.page_utils.is_element_present(value)

    def verify_select_fields(self, data):
        print(data)
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        return self.page_utils.is_element_present(value)

    def verfy_courses_in_country(self, courses):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            for item in courses:
                # print(item)
                if self.check_element(item):
                    result = True
                else:
                    result = False
                    break

            return result

    def tap_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        self.action_perform(value)
        time.sleep(.5)

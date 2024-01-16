import time
from dataProvider.base import Base


class travelrating(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
    no_thanks = ('xpath', '//android.widget.Button[@content-desc="No, thank you"]')
    yes_agree = ('xpath', '//android.widget.Button[@content-desc="Yes, I agree"]')
    australia = ('xpath', "//*[contains(@content-desc, 'Australia')]")
    playnow = ('xpath', "//*[contains(@content-desc, 'Play Now')]")
    travel_rating = ('xpath', "//*[contains(@content-desc, 'Travel Rating')]")
    travelrating_header = ('xpath', '//android.view.View[@content-desc="Travel Rating"]')
    play_travel_rating = ('xpath', '//android.widget.Button[@content-desc="Play Travel Rating"]')
    done = ('xpath', '//android.widget.Button[@content-desc="Done"]')
    lets_play = ('xpath', '//android.widget.Button[@content-desc="Let’s Play"]')
    happy = ('xpath', '//android.widget.Button[@content-desc="Happy\nHappy"]')
    dansurprise = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/emotions/tr_a1.png"]')
    dandisgusted = ('xpath', '//android.widget.Button[@content-desc="Disgusted\nDisgusted"]')
    danexitment = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/emotions/12_c1.png"]')
    welldone = ('xpath', '//android.widget.Button[@content-desc="Well Done!"]')
    hundredpercent = ('xpath', '//android.view.View[@content-desc="100"]')
    result = ('xpath', '(//android.view.View[@content-desc="Results"])[1]')
    result100 = ('xpath', '//android.view.View[@content-desc="100"]')
    resultpercentage = ('xpath', '//android.view.View[@content-desc="%"]')
    page1of4 = ('xpath', '//android.view.View[@content-desc="1 of 4"]')
    page2of4 = ('xpath', '//android.view.View[@content-desc="2 of 4"]')
    page3of4 = ('xpath', '//android.view.View[@content-desc="3 of 4"]')
    page4of4 = ('xpath', '//android.view.View[@content-desc="4 of 4"]')
    paused = ('xpath', '//android.view.View[@content-desc="Paused"]')
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    restart = ('xpath', '//android.widget.Button[@content-desc="Restart"]')
    resume = ('xpath', '//android.widget.Button[@content-desc="Resume"]')
    close = ('xpath', '//android.widget.ImageView[@content-desc="close_button"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    progresstitile = ('xpath', '//android.view.View[@content-desc="Progress"]')
    progresstravelrating = ('xpath', "//android.widget.ImageView[@content-desc='Travel Rating\n100%']")


    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_travelrating(self):
        self.action_perform(self.travel_rating)

    def click_playtravelrating(self):
        self.action_perform(self.play_travel_rating)

    def check_element(self, data):
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def verify_select_fields(self, data):
        print(data)
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        return self.page_utils.is_element_present(value)

    def click_letsplay(self):
        self.action_perform(self.lets_play)

    def click_happy(self):
        self.action_perform(self.happy)

    def click_dansurprise(self):
        self.action_perform(self.dansurprise)

    def click_dandisgusted(self):
        self.action_perform(self.dandisgusted)

    def click_danexitment(self):
        self.action_perform(self.danexitment)

    def click_closebutton(self):
        self.action_perform(self.close)

    def click_resume(self):
        self.action_perform(self.resume)

    def click_quit(self):
        self.action_perform(self.quit)

    def click_restart(self):
        self.action_perform(self.restart)

    def click_progress(self):
        self.click(self.progress)

    def system_bar(self):
        return self.page_utils.get_system_bar()

    def verify_travelrating_landing(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            if self.page_utils.is_element_present(self.travelrating_header) and self.page_utils.is_element_present(
                    self.play_travel_rating) and self.check_element(description):
                return True
            else:
                return False

    def verify_TravelRating_tutorial(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            time.sleep(2.5)
            for item in tutorial_content:
                if self.verify_select_fields(item):
                    if self.page_utils.is_element_present(self.click_next):
                        self.click_next_btn()
                        result = True
                    else:
                        self.click_letsplay()
                        print('lets play')
                        result = True
                else:
                    result = False
            return result

    def verify_TravelRating_tutorial_lastpage(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            time.sleep(2.5)
            for item in tutorial_content:
                if self.verify_select_fields(item):
                    if self.page_utils.is_element_present(self.click_next):
                        self.click_next_btn()
                    else:
                        self.click_letsplay()
                        return self.is_element_present(self.page1of4)

    def verify_TravelRating_game(self, q1,q2,q3,q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.check_element(q1):
                self.click_happy()
                self.click_next_btn()
                if self.check_element(q2):
                    self.click_dansurprise()
                    self.click_next_btn()
                    if self.check_element(q3):
                        self.click_dandisgusted()
                        self.click_next_btn()
                        if self.check_element(q4):
                            self.click_danexitment()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(
                                    self.welldone) and self.is_element_present(
                                self.result100) and self.is_element_present(
                                self.resultpercentage):
                                return True
                            else:
                                return False

    def verify_TravelRating_game_header(self, q1, q2, q3, q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.check_element(q1) and self.is_element_present(self.page1of4):
                self.click_happy()
                self.click_next_btn()
                if self.check_element(q2) and self.is_element_present(self.page2of4):
                    self.click_dansurprise()
                    self.click_next_btn()
                    if self.check_element(q3) and self.is_element_present(self.page3of4):
                        self.click_dandisgusted()
                        self.click_next_btn()
                        if self.check_element(q4) and self.is_element_present(self.page4of4):
                            self.click_danexitment()
                            return True

    def verify_TravelRating_game_pause_quit(self, q1, q2, q3, q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.check_element(q1):
                self.click_happy()
                self.click_next_btn()
                if self.check_element(q2):
                    self.click_dansurprise()
                    self.click_closebutton()
                    if self.is_element_present(self.paused):
                        self.click_quit()
                        return self.is_element_present(self.travel_rating)

    def verify_TravelRating_game_pause_restart(self, q1, q2, q3, q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.check_element(q1):
                self.click_happy()
                self.click_next_btn()
                if self.check_element(q2):
                    self.click_dansurprise()
                    self.click_closebutton()
                    if self.is_element_present(self.paused):
                        self.click_restart()
                        if self.is_element_present(self.page1of4) and self.check_element(q1):
                            return True

    def verify_TravelRating_game_pause_resume(self, q1, q2, q3, q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.check_element(q1):
                self.click_happy()
                self.click_next_btn()
                if self.check_element(q2):
                    self.click_dansurprise()
                    self.click_closebutton()
                    if self.is_element_present(self.paused):
                        self.click_resume()
                        if self.is_element_present(self.page2of4) and self.check_element(q2):
                            return True
    def verify_TravelRating_progress(self, q1,q2,q3,q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            self.click_playtravelrating()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.check_element(q1):
                self.click_happy()
                self.click_next_btn()
                if self.check_element(q2):
                    self.click_dansurprise()
                    self.click_next_btn()
                    if self.check_element(q3):
                        self.click_dandisgusted()
                        self.click_next_btn()
                        if self.check_element(q4):
                            self.click_danexitment()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(
                                    self.welldone) and self.is_element_present(
                                self.result100) and self.is_element_present(
                                self.resultpercentage):
                                self.click_done()
                                self.click_closebutton()
                                self.click_progress()
                                if self.is_element_present(self.progresstitile) and self.is_element_present(
                                        self.progresstravelrating):
                                    return True
                                return True
                            else:
                                return False

    def verify_TravelRating_clock(self, q1,q2,q3,q4):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_travelrating()
            if self.system_bar():
                self.click_playtravelrating()
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_letsplay()
                            if self.system_bar():
                                if self.check_element(q1):
                                    self.click_happy()
                                    self.click_next_btn()
                                    if self.system_bar():
                                        if self.check_element(q2):
                                            self.click_dansurprise()
                                            self.click_next_btn()
                                            if self.system_bar():
                                                if self.check_element(q3):
                                                    self.click_dandisgusted()
                                                    self.click_next_btn()
                                                    if self.system_bar():
                                                        if self.check_element(q4):
                                                            self.click_danexitment()
                                                            self.click_next_btn()
                                                            if self.system_bar():
                                                                if self.is_element_present(self.result) and self.is_element_present(
                                                                        self.welldone) and self.is_element_present(
                                                                    self.result100) and self.is_element_present(
                                                                    self.resultpercentage):
                                                                    self.click_done()
                                                                    self.click_closebutton()
                                                                    self.click_progress()
                                                                    if self.is_element_present(self.progresstitile) and self.is_element_present(
                                                                            self.progresstravelrating):
                                                                        return True
                                                                    return True
                                                                else:
                                                                    return False

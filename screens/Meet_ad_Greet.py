import time
from dataProvider.base import Base


class meetandgreet(Base):
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
    meetandgreet = ('xpath', "//*[contains(@content-desc, 'Meet & Greet')]")
    lets_play = ('xpath', '//android.widget.Button[@content-desc="Let’s Play"]')
    tutorial = ('xpath', '//android.view.View[@content-desc="Tutorial"]')
    start_round = ('xpath', "//*[contains(@content-desc, 'Start Round 1')]")
    play_meetandgreet = ('xpath', '//android.widget.Button[@content-desc="Play Meet & Greet"]')
    next = ('xpath', "//*[contains(@content-desc, 'Next')]")
    done = ('xpath', '//android.widget.Button[@content-desc="Done"]')
    takeabreak = ('xpath', '//android.view.View[@content-desc="Take a break"]')
    video_in_takeabreak = ('xpath', '//android.view.View[@content-desc="00:00 / 00:58"]/android.view.View[1]')
    meetandgreet_result = ('xpath', '//android.widget.Button[@content-desc="Great work!"]')
    meetandgreet_round1_result = ('xpath', '(//android.view.View[@content-desc="100"])[1]')
    meetandgreet_round2_result = ('xpath', '(//android.view.View[@content-desc="100"])[2]')
    meetandgreet_progress = ('xpath', '//android.widget.ImageView[@content-desc="Meet & Greet\nRound 1\n100%\nRound 2\n100%"]')

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_meetandgreet(self):
        self.action_perform(self.meetandgreet)

    def click_letsplay(self):
        self.action_perform(self.lets_play)

    def tap_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        self.action_perform(value)
        time.sleep(.5)

    def check_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def verify_select_fields(self, data):
        print(data)
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        return self.page_utils.is_element_present(value)

    def click_playmeetandgreet(self):
        self.action_perform(self.play_meetandgreet)

    def click_progress(self):
        self.click(self.progress)

    def verify_meet_and_greet(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            return self.verify_select_fields(content)

    def verify_meet_and_greet_tutorial_content(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            time.sleep(2)
            for item in content:
                time.sleep(.5)
                if self.verify_select_fields(item):
                    if self.page_utils.is_element_present(self.click_next):
                        self.click_next_btn()
                        result = True
                    else:
                        self.click_letsplay()
                        result = True
                else:
                    result = False
            return result

    def verify_meet_and_greet_game_details(self, game_details):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            time.sleep(.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            time.sleep(.5)
            for item in game_details:
                if self.verify_select_fields(item):
                    self.click_next_btn()
                    result = True
                else:
                    result = False
            return result

    def verify_meet_and_greet_step1(self, questtion, answer, question2):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(questtion):
                self.tap_element(answer)
                self.click_next_btn()
                return self.check_element(question2)

    def verify_meet_and_greet_step2(self, questtion, answer, question2, question3, answer2):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(questtion):
                self.tap_element(answer)
                self.click_next_btn()
                if self.check_element(question2):
                    self.tap_element(answer2)
                    self.click_next_btn()
                    return self.check_element(question3)

    def verify_meet_and_greet_step3(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        return self.check_element(game_questions[3])

    def verify_meet_and_greet_step4(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            return self.is_element_present(self.takeabreak)

    def verify_meet_and_greet_game_video(self, game_questions, game_answer, toutorial):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                if self.is_element_present(self.video_in_takeabreak):
                                    return self.check_element(toutorial)

    def verify_meet_and_greet_game_round2_Step1(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(22)
                                if self.is_element_present(self.click_next):
                                    self.click_next_btn()
                                    if self.check_element(game_questions[4]):
                                        self.tap_element(game_answer[4])
                                        self.click_next_btn()
                                        return self.check_element(game_questions[5])

    def verify_meet_and_greet_game_round2_Step2(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(22)
                                if self.is_element_present(self.click_next):
                                    self.click_next_btn()
                                    if self.check_element(game_questions[4]):
                                        self.tap_element(game_answer[4])
                                        self.click_next_btn()
                                        if self.check_element(game_questions[5]):
                                            self.tap_element(game_answer[5])
                                            self.click_next_btn()
                                            return self.check_element(game_questions[6])

    def verify_meet_and_greet_game_round2_Step3(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(22)
                                if self.is_element_present(self.click_next):
                                    self.click_next_btn()
                                    if self.check_element(game_questions[4]):
                                        self.tap_element(game_answer[4])
                                        self.click_next_btn()
                                        if self.check_element(game_questions[5]):
                                            self.tap_element(game_answer[5])
                                            self.click_next_btn()
                                            if self.check_element(game_questions[6]):
                                                self.tap_element(game_answer[6])
                                                self.click_next_btn()
                                                return self.check_element(game_questions[7])

    def verify_meet_and_greet_game_round2_Step4(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(22)
                                if self.is_element_present(self.click_next):
                                    self.click_next_btn()
                                    if self.check_element(game_questions[4]):
                                        self.tap_element(game_answer[4])
                                        self.click_next_btn()
                                        if self.check_element(game_questions[5]):
                                            self.tap_element(game_answer[5])
                                            self.click_next_btn()
                                            if self.check_element(game_questions[6]):
                                                self.tap_element(game_answer[6])
                                                self.click_next_btn()
                                                if self.check_element(game_questions[7]):
                                                    self.tap_element(game_answer[7])
                                                    self.click_next_btn()
                                                    return self.is_element_present(self.meetandgreet_result)

    def verify_meet_and_greet_game_result(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(22)
                                self.is_element_present(self.takeabreak)
                                if self.is_element_present(self.click_next):
                                    self.click_next_btn()
                                    if self.check_element(game_questions[4]):
                                        self.tap_element(game_answer[4])
                                        self.click_next_btn()
                                        if self.check_element(game_questions[5]):
                                            self.tap_element(game_answer[5])
                                            self.click_next_btn()
                                            if self.check_element(game_questions[6]):
                                                self.tap_element(game_answer[6])
                                                self.click_next_btn()
                                                if self.check_element(game_questions[7]):
                                                    self.tap_element(game_answer[7])
                                                    self.click_next_btn()
                                                    if self.is_element_present(
                                                            self.meetandgreet_result) and self.is_element_present(
                                                        self.meetandgreet_round1_result) and self.is_element_present(
                                                        self.meetandgreet_round2_result):
                                                        return True

    def verify_meet_and_greet_progress(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            self.click_playmeetandgreet()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            if self.check_element(game_questions[0]):
                self.tap_element(game_answer[0])
                self.click_next_btn()
                if self.check_element(game_questions[1]):
                    self.tap_element(game_answer[1])
                    self.click_next_btn()
                    if self.check_element(game_questions[2]):
                        self.tap_element(game_answer[2])
                        self.click_next_btn()
                        if self.check_element(game_questions[3]):
                            self.tap_element(game_answer[3])
                            self.click_next_btn()
                            if self.is_element_present(self.takeabreak):
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(20)
                                self.is_element_present(self.takeabreak)
                                time.sleep(22)
                                self.is_element_present(self.takeabreak)
                                if self.is_element_present(self.click_next):
                                    self.click_next_btn()
                                    if self.check_element(game_questions[4]):
                                        self.tap_element(game_answer[4])
                                        self.click_next_btn()
                                        if self.check_element(game_questions[5]):
                                            self.tap_element(game_answer[5])
                                            self.click_next_btn()
                                            if self.check_element(game_questions[6]):
                                                self.tap_element(game_answer[6])
                                                self.click_next_btn()
                                                if self.check_element(game_questions[7]):
                                                    self.tap_element(game_answer[7])
                                                    self.click_next_btn()
                                                    if self.is_element_present(
                                                            self.meetandgreet_result) and self.is_element_present(
                                                        self.meetandgreet_round1_result) and self.is_element_present(
                                                        self.meetandgreet_round2_result):
                                                        self.click_done()
                                                        self.back()
                                                        self.click_progress()
                                                        return self.is_element_present(self.meetandgreet_progress)

    def verify_meet_and_greet_clock(self, game_questions, game_answer):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_meetandgreet()
            if self.system_bar():
                self.click_playmeetandgreet()
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_next_btn()
                            if self.system_bar():
                                self.click_letsplay()
                                if self.system_bar():
                                    self.click_next_btn()
                                    if self.system_bar():
                                        self.click_next_btn()
                                        if self.system_bar():
                                            self.click_next_btn()
                                            if self.system_bar():
                                                self.click_next_btn()
                                                if self.system_bar():
                                                    if self.check_element(game_questions[0]):
                                                        self.tap_element(game_answer[0])
                                                        self.click_next_btn()
                                                        if self.system_bar():
                                                            if self.check_element(game_questions[1]):
                                                                self.tap_element(game_answer[1])
                                                                self.click_next_btn()
                                                                if self.system_bar():
                                                                    if self.check_element(game_questions[2]):
                                                                        self.tap_element(game_answer[2])
                                                                        self.click_next_btn()
                                                                        if self.system_bar():
                                                                            if self.check_element(game_questions[3]):
                                                                                self.tap_element(game_answer[3])
                                                                                self.click_next_btn()
                                                                                if self.system_bar():
                                                                                    if self.is_element_present(self.takeabreak):
                                                                                        time.sleep(20)
                                                                                        self.is_element_present(self.takeabreak)
                                                                                        time.sleep(20)
                                                                                        self.is_element_present(self.takeabreak)
                                                                                        time.sleep(22)
                                                                                        self.is_element_present(self.takeabreak)
                                                                                        if self.is_element_present(self.click_next):
                                                                                            self.click_next_btn()
                                                                                            if self.system_bar():
                                                                                                if self.check_element(game_questions[4]):
                                                                                                    self.tap_element(game_answer[4])
                                                                                                    self.click_next_btn()
                                                                                                    if self.system_bar():
                                                                                                        if self.check_element(game_questions[5]):
                                                                                                            self.tap_element(game_answer[5])
                                                                                                            self.click_next_btn()
                                                                                                            if self.system_bar():
                                                                                                                if self.check_element(game_questions[6]):
                                                                                                                    self.tap_element(game_answer[6])
                                                                                                                    self.click_next_btn()
                                                                                                                    if self.system_bar():
                                                                                                                        if self.check_element(game_questions[7]):
                                                                                                                            self.tap_element(game_answer[7])
                                                                                                                            self.click_next_btn()
                                                                                                                            if self.system_bar():
                                                                                                                                if self.is_element_present(
                                                                                                                                        self.meetandgreet_result) and self.is_element_present(
                                                                                                                                    self.meetandgreet_round1_result) and self.is_element_present(
                                                                                                                                    self.meetandgreet_round2_result):
                                                                                                                                    return True
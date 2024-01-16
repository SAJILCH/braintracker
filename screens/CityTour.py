import time
from dataProvider.base import Base

class citytour(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
    no_thanks = ('xpath', '//android.widget.Button[@content-desc="No, thank you"]')
    yes_agree = ('xpath', '//android.widget.Button[@content-desc="Yes, I agree"]')
    how_to_play = ('xpath', "//*[contains(@content-desc, 'How to play')]")
    start_your_journey = ('xpath', "//*[contains(@content-desc, 'Start your journey')]")
    australia = ('xpath', "//*[contains(@content-desc, 'Australia')]")
    playnow = ('xpath', "//*[contains(@content-desc, 'Play Now')]")
    lets_play = ('xpath', '//android.widget.Button[@content-desc="Let’s Play"]')
    tutorial = ('xpath', '//android.view.View[@content-desc="Tutorial"]')
    done = ('xpath', '//android.widget.Button[@content-desc="Done"]')
    citytour = ('xpath', '//*[contains(@content-desc, "City Tour")]')
    play_citytour = ('xpath', "//*[contains(@content-desc, 'Play City Tour')]")
    round1description = ('xpath', '//android.view.View[@content-desc="Take this route to the Harbour Bridge"]')
    round1header = ('xpath', '//android.view.View[@content-desc="Round 1"]')
    letsgo = ('xpath', '//android.widget.Button[@content-desc="Let’s Go"]')
    answer1 = ('xpath', '(//android.widget.Button[@content-desc="1"])')
    answer2 = ('xpath', '(//android.widget.Button[@content-desc="2"])')
    answer3 = ('xpath', '(//android.widget.Button[@content-desc="3"])')
    round2header = ('xpath', '//android.view.View[@content-desc="Round 2"]')
    round2description = ('xpath', '//android.view.View[@content-desc="You made it! Now it’s time to make your way back"]')
    citytourQuestion= ('xpath', '//android.view.View[@content-desc="Which exit do you need\nto take?"]')
    page1of4 = ('xpath', '//android.view.View[@content-desc="1 of 4"]')
    page2of4 = ('xpath', '//android.view.View[@content-desc="2 of 4"]')
    page3of4 = ('xpath', '//android.view.View[@content-desc="3 of 4"]')
    page4of4 = ('xpath', '//android.view.View[@content-desc="4 of 4"]')
    welldone = ('xpath', '//android.widget.Button[@content-desc="Well Done!"]')
    hundredpercent = ('xpath', '//android.view.View[@content-desc="100"]')
    result = ('xpath', '(//android.view.View[@content-desc="Results"])[1]')
    result100 = ('xpath', '//android.view.View[@content-desc="100"]')
    resultpercentage = ('xpath', '//android.view.View[@content-desc="%"]')
    paused = ('xpath', '//android.view.View[@content-desc="Paused"]')
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    restart = ('xpath', '//android.widget.Button[@content-desc="Restart"]')
    resume = ('xpath', '//android.widget.Button[@content-desc="Resume"]')
    close = ('xpath', '//android.widget.ImageView[@content-desc="close_button"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    progresstitile = ('xpath', '//android.view.View[@content-desc="Progress"]')
    progresscitytour = ('xpath', "//android.widget.ImageView[@content-desc='City Tour\n100%']")

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_citytour(self):
        self.action_perform(self.citytour)

    def click_playcitytour(self):
        self.action_perform(self.play_citytour)

    def click_letsgo(self):
        self.action_perform(self.letsgo)

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

    def click_answer1(self):
        self.action_perform(self.answer1)

    def click_answer2(self):
        self.action_perform(self.answer2)

    def click_answer3(self):
        self.action_perform(self.answer3)

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

    def verify_citytour_landing(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            if self.page_utils.is_element_present(self.citytour) and self.page_utils.is_element_present(
                    self.play_citytour) and self.check_element(description):
                return True
            else:
                return False


    def verify_citytour_tutorial(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            self.click_playcitytour()
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

    def verify_citytour_game(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            self.click_playcitytour()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                self.click_letsgo()
                if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                    self.click_answer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page2of4) and self.is_element_present(self.citytourQuestion):
                        self.click_answer1()
                        self.click_next_btn()
                        if self.is_element_present(self.page3of4) and self.is_element_present(self.citytourQuestion):
                            self.click_answer3()
                            self.click_next_btn()
                            if self.is_element_present(self.page4of4) and self.is_element_present(
                                self.citytourQuestion):
                                self.click_answer1()
                                self.click_next_btn()
                                if self.is_element_present(self.round2header) and self.is_element_present(self.round2description):
                                    self.click_letsgo()
                                    if self.is_element_present(self.page1of4) and self.is_element_present(
                                        self.citytourQuestion):
                                        self.click_answer3()
                                        self.click_next_btn()
                                        if self.is_element_present(self.page2of4) and self.is_element_present(
                                                self.citytourQuestion):
                                            self.click_answer2()
                                            self.click_next_btn()
                                            if self.is_element_present(self.page3of4) and self.is_element_present(
                                                    self.citytourQuestion):
                                                self.click_answer3()
                                                self.click_next_btn()
                                                if self.is_element_present(self.page4of4) and self.is_element_present(
                                                        self.citytourQuestion):
                                                    self.click_answer2()
                                                    self.click_next_btn()
                                                    if self.is_element_present(self.result) and self.is_element_present(
                                                            self.welldone) and self.is_element_present(
                                                            self.result100) and self.is_element_present(
                                                            self.resultpercentage):
                                                        return True
                                                    else:
                                                        return False

    def verify_citytour_game_pause_quit(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            self.click_playcitytour()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                self.click_letsgo()
                if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                    self.click_answer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page2of4) and self.is_element_present(self.citytourQuestion):
                        self.click_answer1()
                        self.click_next_btn()
                        self.click_closebutton()
                        if self.is_element_present(self.paused):
                            self.click_quit()
                            return self.is_element_present(self.citytour)

    def verify_citytour_game_pause_restart(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            self.click_playcitytour()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                self.click_letsgo()
                if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                    self.click_answer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page2of4) and self.is_element_present(self.citytourQuestion):
                        self.click_answer1()
                        self.click_next_btn()
                        self.click_closebutton()
                        if self.is_element_present(self.paused):
                            self.click_restart()
                            return self.is_element_present(self.round1header) and self.is_element_present(self.round1description)

    def verify_citytour_game_pause_resume(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            self.click_playcitytour()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                self.click_letsgo()
                if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                    self.click_answer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page2of4) and self.is_element_present(self.citytourQuestion):
                        self.click_answer1()
                        self.click_next_btn()
                        self.click_closebutton()
                        if self.is_element_present(self.paused):
                            self.click_resume()
                            return self.is_element_present(self.page3of4) and self.is_element_present(self.citytourQuestion)

            def verify_citytour_game(self):
                self.click_next_btn()
                self.click_next_btn()
                self.click_next_btn()
                self.click_next_btn()
                self.click_next_btn()
                self.click_nothanks()
                if self.page_utils.is_element_present(self.australia):
                    self.click_playnow()
                    self.scrolling(self.citytour)
                    self.click_citytour()
                    self.click_playcitytour()
                    time.sleep(2.5)
                    self.click_next_btn()
                    self.click_next_btn()
                    self.click_letsplay()
                    if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                        self.click_letsgo()
                        if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                            self.click_answer2()
                            self.click_next_btn()
                            if self.is_element_present(self.page2of4) and self.is_element_present(
                                    self.citytourQuestion):
                                self.click_answer1()
                                self.click_next_btn()
                                if self.is_element_present(self.page3of4) and self.is_element_present(
                                        self.citytourQuestion):
                                    self.click_answer3()
                                    self.click_next_btn()
                                    if self.is_element_present(self.page4of4) and self.is_element_present(
                                            self.citytourQuestion):
                                        self.click_answer1()
                                        self.click_next_btn()
                                        if self.is_element_present(self.round2header) and self.is_element_present(
                                                self.round2description):
                                            self.click_letsgo()
                                            if self.is_element_present(self.page1of4) and self.is_element_present(
                                                    self.citytourQuestion):
                                                self.click_answer3()
                                                self.click_next_btn()
                                                if self.is_element_present(self.page2of4) and self.is_element_present(
                                                        self.citytourQuestion):
                                                    self.click_answer2()
                                                    self.click_next_btn()
                                                    if self.is_element_present(
                                                            self.page3of4) and self.is_element_present(
                                                            self.citytourQuestion):
                                                        self.click_answer3()
                                                        self.click_next_btn()
                                                        if self.is_element_present(
                                                                self.page4of4) and self.is_element_present(
                                                                self.citytourQuestion):
                                                            self.click_answer2()
                                                            self.click_next_btn()
                                                            if self.is_element_present(
                                                                    self.result) and self.is_element_present(
                                                                    self.welldone) and self.is_element_present(
                                                                self.result100) and self.is_element_present(
                                                                self.resultpercentage):
                                                                return True
                                                            else:
                                                                return False

    def verify_citytour_game_progress(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            self.click_playcitytour()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                self.click_letsgo()
                if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                    self.click_answer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page2of4) and self.is_element_present(self.citytourQuestion):
                        self.click_answer1()
                        self.click_next_btn()
                        if self.is_element_present(self.page3of4) and self.is_element_present(self.citytourQuestion):
                            self.click_answer3()
                            self.click_next_btn()
                            if self.is_element_present(self.page4of4) and self.is_element_present(
                                self.citytourQuestion):
                                self.click_answer1()
                                self.click_next_btn()
                                if self.is_element_present(self.round2header) and self.is_element_present(self.round2description):
                                    self.click_letsgo()
                                    if self.is_element_present(self.page1of4) and self.is_element_present(
                                        self.citytourQuestion):
                                        self.click_answer3()
                                        self.click_next_btn()
                                        if self.is_element_present(self.page2of4) and self.is_element_present(
                                                self.citytourQuestion):
                                            self.click_answer2()
                                            self.click_next_btn()
                                            if self.is_element_present(self.page3of4) and self.is_element_present(
                                                    self.citytourQuestion):
                                                self.click_answer3()
                                                self.click_next_btn()
                                                if self.is_element_present(self.page4of4) and self.is_element_present(
                                                        self.citytourQuestion):
                                                    self.click_answer2()
                                                    self.click_next_btn()
                                                    if self.is_element_present(self.result) and self.is_element_present(
                                                            self.welldone) and self.is_element_present(
                                                            self.result100) and self.is_element_present(
                                                            self.resultpercentage):
                                                        self.click_done()
                                                        self.click_closebutton()
                                                        self.click_progress()
                                                        if self.is_element_present(
                                                                self.progresstitile) and self.is_element_present(
                                                                self.progresscitytour):
                                                            return True
                                                        return True
                                                    else:
                                                        return False

    def verify_citytour_game_clock(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_citytour()
            if self.system_bar():
                self.click_playcitytour()
                time.sleep(2.5)
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_letsplay()
                            if self.system_bar():
                                if self.is_element_present(self.round1header) and self.is_element_present(self.round1description):
                                    self.click_letsgo()
                                    if self.system_bar():
                                        if self.is_element_present(self.page1of4) and self.is_element_present(self.citytourQuestion):
                                            self.click_answer2()
                                            self.click_next_btn()
                                            if self.system_bar():
                                                if self.is_element_present(self.page2of4) and self.is_element_present(self.citytourQuestion):
                                                    self.click_answer1()
                                                    self.click_next_btn()
                                                    if self.system_bar():
                                                        if self.is_element_present(self.page3of4) and self.is_element_present(self.citytourQuestion):
                                                            self.click_answer3()
                                                            self.click_next_btn()
                                                            if self.system_bar():
                                                                if self.is_element_present(self.page4of4) and self.is_element_present(
                                                                    self.citytourQuestion):
                                                                    self.click_answer1()
                                                                    self.click_next_btn()
                                                                    if self.system_bar():
                                                                        if self.is_element_present(self.round2header) and self.is_element_present(self.round2description):
                                                                            self.click_letsgo()
                                                                            if self.system_bar():
                                                                                if self.is_element_present(self.page1of4) and self.is_element_present(
                                                                                    self.citytourQuestion):
                                                                                    self.click_answer3()
                                                                                    self.click_next_btn()
                                                                                    if self.system_bar():
                                                                                        if self.is_element_present(self.page2of4) and self.is_element_present(
                                                                                                self.citytourQuestion):
                                                                                            self.click_answer2()
                                                                                            self.click_next_btn()
                                                                                            if self.system_bar():
                                                                                                if self.is_element_present(self.page3of4) and self.is_element_present(
                                                                                                        self.citytourQuestion):
                                                                                                    self.click_answer3()
                                                                                                    self.click_next_btn()
                                                                                                    if self.system_bar():
                                                                                                        if self.is_element_present(self.page4of4) and self.is_element_present(
                                                                                                                self.citytourQuestion):
                                                                                                            self.click_answer2()
                                                                                                            self.click_next_btn()
                                                                                                            if self.system_bar():
                                                                                                                if self.is_element_present(self.result) and self.is_element_present(
                                                                                                                        self.welldone) and self.is_element_present(
                                                                                                                        self.result100) and self.is_element_present(
                                                                                                                        self.resultpercentage):
                                                                                                                    return True
                                                                                                                else:
                                                                                                                    return False
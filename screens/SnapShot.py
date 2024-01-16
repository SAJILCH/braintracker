import time
from dataProvider.base import Base

class snapshot(Base):
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
    snapshot = ('xpath', '//*[contains(@content-desc, "Snapshot")]')
    citytour = ('xpath', '//*[contains(@content-desc, "City Tour")]')
    play_snapshot = ('xpath', "//*[contains(@content-desc, 'Play Snapshot')]")
    page1of4 = ('xpath', '//android.view.View[@content-desc="1 of 4"]')
    page2of4 = ('xpath', '//android.view.View[@content-desc="2 of 4"]')
    page3of4 = ('xpath', '//android.view.View[@content-desc="3 of 4"]')
    page4of4 = ('xpath', '//android.view.View[@content-desc="4 of 4"]')
    welldone = ('xpath', '//android.widget.Button[@content-desc="Well Done!"]')
    hundredpercent = ('xpath', '//android.view.View[@content-desc="100"]')
    result = ('xpath', '(//android.view.View[@content-desc="Results"])[1]')
    result75 = ('xpath', '//android.view.View[@content-desc="75"]')
    resultpercentage = ('xpath', '//android.view.View[@content-desc="%"]')
    paused = ('xpath', '//android.view.View[@content-desc="Paused"]')
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    restart = ('xpath', '//android.widget.Button[@content-desc="Restart"]')
    resume = ('xpath', '//android.widget.Button[@content-desc="Resume"]')
    close = ('xpath', '//android.widget.ImageView[@content-desc="close_button"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    progresstitile = ('xpath', '//android.view.View[@content-desc="Progress"]')
    progresssnapshot = ('xpath', '//android.widget.ImageView[@content-desc="Snapshot\n75%"]')
    snapshotanswer1 = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/snapshot/ss_ques_3_opt_1.png"]')
    snapshotanswer2 = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/snapshot/ss_ques_4_opt_1.png"]')
    snapshotanswer3 = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/snapshot/ss_ques_1_opt_1.png"]')
    rotatebutton = ('xpath', '//android.widget.Button[@content-desc="button_ss_ccw"]')
    summary = ('xpath', '//android.view.View[@content-desc="Your score shows the percentage of correct answers. \n\nVisit the progress page to track your performance. Many factors can influence your score over time."]')

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_snapshot(self):
        self.action_perform(self.snapshot)

    def click_playsnapshot(self):
        self.action_perform(self.play_snapshot)

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

    def click_snapshotanswer1(self):
        self.click(self.snapshotanswer1)

    def click_snapshotanswer2(self):
        self.click(self.snapshotanswer2)

    def click_snapshotanswer3(self):
        self.click(self.snapshotanswer3)

    def click_rotate(self):
        self.click(self.rotatebutton)

    def verify_snapshot_landing(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            if self.page_utils.is_element_present(self.snapshot) and self.page_utils.is_element_present(
                    self.play_snapshot) and self.check_element(description):
                return True
            else:
                return False


    def verify_snapshot_tutorial(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
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

    def verify_snapshot_tutorial_close(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_closebutton()
            self.click_quit()
            return self.page_utils.is_element_present(self.snapshot)

    def verify_snapshot_tutorial_content(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            for item in tutorial_content:
                if self.verify_select_fields(item) and self.is_element_present(self.tutorial):
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

    def verify_snapshot_game(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page3of4):
                        self.click_snapshotanswer3()
                        self.click_next_btn()
                        if self.is_element_present(self.page4of4):
                            self.click_rotate()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(self.welldone) and self.is_element_present(
                                self.result75) and self.is_element_present(self.resultpercentage):
                                return True
                            else:
                                return False

    def verify_snapshot_game_close(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_closebutton()
                    self.click_quit()
                    if self.is_element_present(self.snapshot) and self.check_element(description):
                        return True

    def verify_snapshot_game_titile(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4) and self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4) and self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page3of4) and self.is_element_present(self.page3of4):
                        self.click_snapshotanswer3()
                        self.click_next_btn()
                        if self.is_element_present(self.page4of4) and self.is_element_present(self.page4of4):
                            self.click_rotate()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(
                                    self.welldone) and self.is_element_present(
                                    self.result75) and self.is_element_present(self.resultpercentage):
                                return True
                            else:
                                return False

    def verify_snapshot_progress(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page3of4):
                        self.click_snapshotanswer3()
                        self.click_next_btn()
                        if self.is_element_present(self.page4of4):
                            self.click_rotate()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(self.welldone) and self.is_element_present(
                                self.result75) and self.is_element_present(self.resultpercentage):
                                self.click_done()
                                self.click_closebutton()
                                self.click_progress()
                                if self.is_element_present(self.progresstitile) and self.is_element_present(self.progresssnapshot):
                                    return True
                                else:
                                    return False

    def verify_snapshot_Quit(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_closebutton()
                    if self.is_element_present(self.paused):
                        self.click_quit()
                        return self.is_element_present(self.snapshot)

    def verify_snapshot_restart(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_closebutton()
                    if self.is_element_present(self.paused):
                        self.click_restart()
                        return self.is_element_present(self.page1of4)

    def verify_snapshot_resume(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_closebutton()
                    if self.is_element_present(self.paused):
                        self.click_resume()
                        return self.is_element_present(self.page2of4)

    def verify_snapshot_resultscreen_componets(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            self.click_playsnapshot()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.page1of4):
                self.click_snapshotanswer1()
                self.click_next_btn()
                if self.is_element_present(self.page2of4):
                    self.click_snapshotanswer2()
                    self.click_next_btn()
                    if self.is_element_present(self.page3of4):
                        self.click_snapshotanswer3()
                        self.click_next_btn()
                        if self.is_element_present(self.page4of4):
                            self.click_rotate()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(self.welldone) and self.is_element_present(
                                self.result75) and self.is_element_present(self.resultpercentage) and self.is_element_present(self.summary) and self.is_element_present(self.done):
                                self.click_done()
                                return self.is_element_present(self.snapshot)

    def verify_snapshot_clock(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_snapshot()
            if self.system_bar():
                self.click_playsnapshot()
                time.sleep(2.5)
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_letsplay()
                            if self.system_bar():
                                if self.is_element_present(self.page1of4):
                                    self.click_snapshotanswer1()
                                    self.click_next_btn()
                                    if self.system_bar():
                                        if self.is_element_present(self.page2of4):
                                            self.click_snapshotanswer2()
                                            self.click_next_btn()
                                            if self.system_bar():
                                                if self.is_element_present(self.page3of4):
                                                    self.click_snapshotanswer3()
                                                    self.click_next_btn()
                                                    if self.system_bar():
                                                        if self.is_element_present(self.page4of4):
                                                            self.click_rotate()
                                                            self.click_next_btn()
                                                            if self.system_bar():
                                                                if self.is_element_present(self.result) and self.is_element_present(
                                                                        self.welldone) and self.is_element_present(
                                                                    self.resultpercentage) and self.is_element_present(
                                                                    self.summary) and self.is_element_present(self.done):
                                                                    return True



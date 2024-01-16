import time
from dataProvider.base import Base


class marketplace(Base):
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
    marketplace = ('xpath', "//*[contains(@content-desc, 'Marketplace')]")
    play_marketplace = ('xpath', "//*[contains(@content-desc, 'Play Marketplace')]")
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    close = ('xpath','//android.widget.ImageView[@content-desc="close_button"]')
    tendollarindexone = ('xpath', '(//*[contains(@content-desc, "10\n$\n$")])[1]')
    fivedollar = ('xpath', '(//*[contains(@content-desc, "5\n$\n$")])[1]')
    twodollarindexone = ('xpath', '(//*[contains(@content-desc, "2\n$\n$")])[1]')
    twodollarindextwo = ('xpath', '(//*[contains(@content-desc, "2\n$\n$")])[2]')
    twentydollarindexone = ('xpath', '(//*[contains(@content-desc, "20\n$\n$")])[1]')
    twentydollarindextwo = ('xpath', '(//*[contains(@content-desc, "20\n$\n$")])[2]')
    onedollarindexone = ('xpath', '(//*[contains(@content-desc, "1\n$\n$")])[1]')
    onedollar = ('xpath', '(//*[contains(@content-desc, "1\n$\n$")])[1]')
    welldone = ('xpath', '//android.widget.Button[@content-desc="Well Done!"]')
    hundredpercent = ('xpath', '//android.view.View[@content-desc="100"]')
    result = ('xpath', '(//android.view.View[@content-desc="Results"])[1]')
    result100 = ('xpath', '//android.view.View[@content-desc="100"]')
    resultpercentage = ('xpath', '//android.view.View[@content-desc="%"]')
    resultsummary = ('xpath', '//android.view.View[@content-desc="Your score shows the percentage of correct answers. \n\nVisit the progress page to track your performance. Many factors can influence your score over time."]')
    page1of4 =('xpath', '//android.view.View[@content-desc="1 of 4"]')
    page2of4 = ('xpath', '//android.view.View[@content-desc="2 of 4"]')
    page3of4 = ('xpath', '//android.view.View[@content-desc="3 of 4"]')
    page4of4 = ('xpath', '//android.view.View[@content-desc="4 of 4"]')
    marketplaceprogress = ('xpath', '//android.widget.ImageView[@content-desc="Marketplace\n100%"]')
    marketplaceprogressscreen = ('xpath', '//*[contains(@content-desc, "Marketplace results")]')
    austrailancurrency = ('xpath', '//*[contains(@content-desc, "A$")]')

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_done(self):
        self.action_perform(self.done)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_marketplace(self):
        self.action_perform(self.marketplace)

    def click_play_marketplace(self):
        self.action_perform(self.play_marketplace)

    def verify_select_fields(self, data):
        print(data)
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        return self.page_utils.is_element_present(value)

    def click_letsplay(self):
        self.action_perform(self.lets_play)

    def click_close(self):
        self.action_perform(self.close)

    def click_progress(self):
        self.click(self.progress)

    def click_marketplaceprogress(self):
        self.action_perform(self.marketplace)

    def click_quit(self):
        self.action_perform(self.quit)

    def check_element(self, data):
        value = ('xpath', "//*[contains(@content-desc, '" + data + "')]")
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def click_10dollarindex1(self):
        self.action_perform(self.tendollarindexone)

    def click_5dollarindex1(self):
        self.action_perform(self.fivedollar)

    def click_20dollarindex1(self):
        self.action_perform(self.twentydollarindexone)

    def click_20dollarindex2(self):
        self.action_perform(self.twentydollarindextwo)

    def click_2dollarindex1(self):
        self.action_perform(self.twodollarindexone)

    def click_2dollarindex2(self):
        self.action_perform(self.twodollarindextwo)

    def click_1dollarindex1(self):
        self.action_perform(self.onedollarindexone)

    def click_1dollar(self):
        self.action_perform(self.onedollar)

    def verify_marketplace(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            self.click_play_marketplace()
            time.sleep(2)
            for item in content:
                time.sleep(.5)
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

    def verify_marketplace_backbutton(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            self.click_play_marketplace()
            time.sleep(2)
            for item in content:
                time.sleep(.5)
                if self.verify_select_fields(item):
                    if self.page_utils.is_element_present(self.click_next):
                        self.click_next_btn()
                    else:
                        self.click_letsplay()
                        print('lets play')
                self.click_close()
                self.click_quit()
                return self.page_utils.is_element_present(self.marketplace)

    def verify_marketplace_intro_screen_discription(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            return self.check_element(content)

    def verify_marketplace_intro_screen_name(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            return self.page_utils.is_element_present(self.marketplace)

    def verify_marketplace_play_button(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()

            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                for item in content:
                    time.sleep(.5)
                    return self.verify_select_fields(item)

    def verify_marketplace_tutorial(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
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

    def verify_marketplace_Game(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                return self.is_element_present(self.welldone)

    def verify_marketplace_Game_result(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                return self.is_element_present(self.result)

    def verify_marketplace_Game_result_welldone(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                return self.is_element_present(self.welldone)

    def verify_marketplace_Game_result_percentage(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                if self.is_element_present(self.welldone) and self.is_element_present(self.result100) and self.is_element_present(self.resultpercentage):
                                    return True
                                else:
                                    return False

    def verify_marketplace_Game_result_summary(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                if self.is_element_present(self.welldone) and self.is_element_present(self.resultsummary) :
                                    return True
                                else:
                                    return False

    def verify_marketplace_Game_done(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                if self.is_element_present(self.welldone) and self.is_element_present(self.resultsummary) :
                                    self.click_done()
                                    return self.is_element_present(self.australia)

    def verify_marketplace_Game_header(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                return self.is_element_present(self.welldone)

    def verify_marketplace_Game_titile(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    if self.is_element_present(self.page1of4):
                        self.click_10dollarindex1()
                        self.click_5dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[1]):
                            if self.is_element_present(self.page2of4):
                                self.click_20dollarindex1()
                                self.click_20dollarindex2()
                                self.click_1dollarindex1()
                                self.click_2dollarindex1()
                                self.click_next_btn()
                                if self.verify_select_fields(content[2]):
                                    if self.is_element_present(self.page3of4):
                                        self.click_20dollarindex1()
                                        self.click_20dollarindex2()
                                        self.click_2dollarindex1()
                                        self.click_2dollarindex2()
                                        self.click_1dollar()
                                        self.click_next_btn()
                                        if self.verify_select_fields(content[3]):
                                            if self.is_element_present(self.page4of4):
                                                self.click_10dollarindex1()
                                                self.click_1dollar()
                                                self.click_next_btn()
                                                return self.is_element_present(self.welldone)

    def verify_marketplace_Game_clock(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.system_bar():
                if self.page_utils.is_element_present(self.play_marketplace):
                    self.click_play_marketplace()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_next_btn()
                            if self.system_bar():
                                self.click_letsplay()
                                if self.system_bar():
                                    if self.verify_select_fields(content[0]):
                                        self.click_10dollarindex1()
                                        self.click_5dollarindex1()
                                        self.click_2dollarindex1()
                                        self.click_next_btn()
                                        if self.system_bar():
                                            if self.verify_select_fields(content[1]):
                                                self.click_20dollarindex1()
                                                self.click_20dollarindex2()
                                                self.click_1dollarindex1()
                                                self.click_2dollarindex1()
                                                self.click_next_btn()
                                                if self.system_bar():
                                                    if self.verify_select_fields(content[2]):
                                                        self.click_20dollarindex1()
                                                        self.click_20dollarindex2()
                                                        self.click_2dollarindex1()
                                                        self.click_2dollarindex2()
                                                        self.click_1dollar()
                                                        self.click_next_btn()
                                                        if self.system_bar():
                                                            if self.verify_select_fields(content[3]):
                                                                self.click_10dollarindex1()
                                                                self.click_1dollar()
                                                                self.click_next_btn()
                                                                if self.system_bar():
                                                                    return self.is_element_present(self.welldone)

    def verify_marketplace_progess(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    self.click_10dollarindex1()
                    self.click_5dollarindex1()
                    self.click_2dollarindex1()
                    self.click_next_btn()
                    if self.verify_select_fields(content[1]):
                        self.click_20dollarindex1()
                        self.click_20dollarindex2()
                        self.click_1dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[2]):
                            self.click_20dollarindex1()
                            self.click_20dollarindex2()
                            self.click_2dollarindex1()
                            self.click_2dollarindex2()
                            self.click_1dollar()
                            self.click_next_btn()
                            if self.verify_select_fields(content[3]):
                                self.click_10dollarindex1()
                                self.click_1dollar()
                                self.click_next_btn()
                                if self.is_element_present(self.welldone) and self.is_element_present(self.resultsummary) :
                                    self.click_done()
                                    self.back()
                                    self.click_progress()
                                    return self.is_element_present(self.marketplaceprogress)

    def verify_marketplace_currency(self, content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_marketplace()
            if self.page_utils.is_element_present(self.play_marketplace):
                self.click_play_marketplace()
                self.click_next_btn()
                self.click_next_btn()
                self.click_letsplay()
                if self.verify_select_fields(content[0]):
                    if self.austrailancurrency:
                        self.click_10dollarindex1()
                        self.click_5dollarindex1()
                        self.click_2dollarindex1()
                        self.click_next_btn()
                        if self.verify_select_fields(content[1]):
                            if self.austrailancurrency:
                                self.click_20dollarindex1()
                                self.click_20dollarindex2()
                                self.click_1dollarindex1()
                                self.click_2dollarindex1()
                                self.click_next_btn()
                                if self.verify_select_fields(content[2]):
                                    if self.austrailancurrency:
                                        self.click_20dollarindex1()
                                        self.click_20dollarindex2()
                                        self.click_2dollarindex1()
                                        self.click_2dollarindex2()
                                        self.click_1dollar()
                                        self.click_next_btn()
                                        if self.verify_select_fields(content[3]):
                                            if self.austrailancurrency:
                                                self.click_10dollarindex1()
                                                self.click_1dollar()
                                                self.click_next_btn()
                                                return self.is_element_present(self.welldone) and self.is_element_present(
                                                        self.resultsummary)



import time
from dataProvider.base import Base


class ticketbox(Base):
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
    ticketbox = ('xpath', '//*[contains(@content-desc, "Ticket Box")]')
    citytour = ('xpath', '//*[contains(@content-desc, "City Tour")]')
    play_ticketbox = ('xpath', "//*[contains(@content-desc, 'Play Ticket Box')]")
    rowandseat = ('xpath', "//android.widget.Button[@content-desc='Row & Seat\nSelect']")
    seekbardone = ('xpath', "//android.view.View[@content-desc='container_tb_cancel\nDone']")
    welldone = ('xpath', '//android.widget.Button[@content-desc="Well Done!"]')
    hundredpercent = ('xpath', '//android.view.View[@content-desc="100"]')
    result = ('xpath', '(//android.view.View[@content-desc="Results"])[1]')
    resultsummary = ('xpath',
                     '//android.view.View[@content-desc="Your score shows the percentage of correct answers. \n\nVisit the progress page to track your performance. Many factors can influence your score over time."]')
    page1of4 = ('xpath', '//android.view.View[@content-desc="1 of 4"]')
    page2of4 = ('xpath', '//android.view.View[@content-desc="2 of 4"]')
    page3of4 = ('xpath', '//android.view.View[@content-desc="3 of 4"]')
    page4of4 = ('xpath', '//android.view.View[@content-desc="4 of 4"]')
    resultpercentage = ('xpath', '//android.view.View[@content-desc="%"]')
    paused = ('xpath', '//android.view.View[@content-desc="Paused"]')
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    restart = ('xpath', '//android.widget.Button[@content-desc="Restart"]')
    resume = ('xpath', '//android.widget.Button[@content-desc="Resume"]')
    close = ('xpath', '//android.widget.ImageView[@content-desc="close_button"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    progresstitile = ('xpath', '//android.view.View[@content-desc="Progress"]')
    progressticketbox = ('xpath', "//android.widget.ImageView[@content-desc='Ticket Box\n100%']")

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_rowandseat(self):
        self.action_perform(self.rowandseat)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_ticketbox(self):
        self.action_perform(self.ticketbox)

    def click_playticketbox(self):
        self.action_perform(self.play_ticketbox)

    def check_element(self, data):
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        self.scrolling(value)
        return self.page_utils.is_element_present(value)

    def click_seekbarrow(self, data):
        seekbar = ('xpath', '//android.widget.SeekBar[@content-desc="' + data + '"]')
        self.seekbarrow_scroll(seekbar)

    def click_seekbarseat(self, data):
        seekbar = ('xpath', '//android.widget.SeekBar[@content-desc="' + data + '"]')
        self.seekbarseat_scroll(seekbar)

    def verify_select_fields(self, data):
        print(data)
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        return self.page_utils.is_element_present(value)

    def click_letsplay(self):
        self.action_perform(self.lets_play)

    def click_seekbardone(self):
        self.action_perform(self.seekbardone)

    def click_close_button(self):
        self.action_perform(self.close)

    def click_quit(self):
        self.action_perform(self.quit)

    def click_restart(self):
        self.action_perform(self.restart)

    def click_resume(self):
        self.action_perform(self.resume)

    def system_bar(self):
        return self.page_utils.get_system_bar()

    def click_progress(self):
        self.click(self.progress)

    def click_done(self):
        self.click(self.done)

    def verify_ticketbox_landing(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            if self.page_utils.is_element_present(self.ticketbox) and self.page_utils.is_element_present(
                    self.play_ticketbox) and self.check_element(description):
                return True
            else:
                return False

    def verify_ticketbox_tutorial(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
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

    def verify_ticketbox_game(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()

            if self.verify_select_fields(game[0]):
                self.click_rowandseat()
                self.click_seekbarrow(str(row[0]))
                self.click_seekbarseat(str(seat[0]))
                self.click_seekbardone()
                self.click_next_btn()
                if self.verify_select_fields(game[1]):
                    self.click_rowandseat()
                    self.click_seekbarrow(str(row[1]))
                    self.click_seekbarseat(str(seat[1]))
                    self.click_seekbardone()
                    self.click_next_btn()
                    if self.verify_select_fields(game[2]):
                        self.click_rowandseat()
                        self.click_seekbarrow(str(row[2]))
                        self.click_seekbarseat(str(seat[2]))
                        self.click_seekbardone()
                        self.click_next_btn()
                        if self.verify_select_fields(game[3]):
                            self.click_rowandseat()
                            self.click_seekbarrow(str(row[3]))
                            self.click_seekbarseat(str(seat[3]))
                            self.click_seekbardone()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(
                                    self.welldone) and self.is_element_present(
                                    self.hundredpercent) and self.is_element_present(self.resultsummary):
                                return True

    def verify_ticketbox_game_titile(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()

            if self.is_element_present(self.page1of4) and self.verify_select_fields(game[0]):
                self.click_rowandseat()
                self.click_seekbarrow(str(row[0]))
                self.click_seekbarseat(str(seat[0]))
                self.click_seekbardone()
                self.click_next_btn()
                if self.is_element_present(self.page2of4) and self.verify_select_fields(game[1]):
                    self.click_rowandseat()
                    self.click_seekbarrow(str(row[1]))
                    self.click_seekbarseat(str(seat[1]))
                    self.click_seekbardone()
                    self.click_next_btn()
                    if self.is_element_present(self.page3of4) and self.verify_select_fields(game[2]):
                        self.click_rowandseat()
                        self.click_seekbarrow(str(row[2]))
                        self.click_seekbarseat(str(seat[2]))
                        self.click_seekbardone()
                        self.click_next_btn()
                        if self.is_element_present(self.page4of4) and self.verify_select_fields(game[3]):
                            self.click_rowandseat()
                            self.click_seekbarrow(str(row[3]))
                            self.click_seekbarseat(str(seat[3]))
                            self.click_seekbardone()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(
                                    self.welldone) and self.is_element_present(
                                self.hundredpercent) and self.is_element_present(self.resultsummary):
                                return True

    def verify_ticketbox_game_pause(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()

            if self.is_element_present(self.page1of4) and self.verify_select_fields(game[0]):
                self.click_rowandseat()
                self.click_seekbarrow(str(row[0]))
                self.click_seekbarseat(str(seat[0]))
                self.click_seekbardone()
                self.click_next_btn()
                if self.is_element_present(self.page2of4) and self.verify_select_fields(game[1]):
                    self.click_rowandseat()
                    self.click_seekbarrow(str(row[1]))
                    self.click_seekbarseat(str(seat[1]))
                    self.click_seekbardone()
                    self.click_next_btn()
                    self.click_close_button()
                    if self.is_element_present(self.paused):
                        self.click_quit()
                        return self.is_element_present(self.ticketbox)

    def verify_ticketbox_game_restart(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()

            if self.is_element_present(self.page1of4) and self.verify_select_fields(game[0]):
                self.click_rowandseat()
                self.click_seekbarrow(str(row[0]))
                self.click_seekbarseat(str(seat[0]))
                self.click_seekbardone()
                self.click_next_btn()
                if self.is_element_present(self.page2of4) and self.verify_select_fields(game[1]):
                    self.click_rowandseat()
                    self.click_seekbarrow(str(row[1]))
                    self.click_seekbarseat(str(seat[1]))
                    self.click_seekbardone()
                    self.click_next_btn()
                    self.click_close_button()
                    if self.is_element_present(self.paused):
                        self.click_restart()
                        return self.verify_select_fields(game[0])

    def verify_ticketbox_game_resume(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()

            if self.is_element_present(self.page1of4) and self.verify_select_fields(game[0]):
                self.click_rowandseat()
                self.click_seekbarrow(str(row[0]))
                self.click_seekbarseat(str(seat[0]))
                self.click_seekbardone()
                self.click_next_btn()
                if self.is_element_present(self.page2of4) and self.verify_select_fields(game[1]):
                    self.click_rowandseat()
                    self.click_seekbarrow(str(row[1]))
                    self.click_seekbarseat(str(seat[1]))
                    self.click_seekbardone()
                    self.click_next_btn()
                    self.click_close_button()
                    if self.is_element_present(self.paused):
                        self.click_resume()
                        return self.verify_select_fields(game[2])

    def verify_ticketbox_clock(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            if self.system_bar():
                self.click_playticketbox()
                time.sleep(2.5)
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_next_btn()
                        if self.system_bar():
                            self.click_next_btn()
                            if self.system_bar():
                                self.click_letsplay()
                                if self.system_bar():
                                    if self.verify_select_fields(game[0]):
                                        self.click_rowandseat()
                                        self.click_seekbarrow(str(row[0]))
                                        self.click_seekbarseat(str(seat[0]))
                                        self.click_seekbardone()
                                        self.click_next_btn()
                                        if self.system_bar():
                                            if self.verify_select_fields(game[1]):
                                                self.click_rowandseat()
                                                self.click_seekbarrow(str(row[1]))
                                                self.click_seekbarseat(str(seat[1]))
                                                self.click_seekbardone()
                                                self.click_next_btn()
                                                if self.system_bar():
                                                    if self.verify_select_fields(game[2]):
                                                        self.click_rowandseat()
                                                        self.click_seekbarrow(str(row[2]))
                                                        self.click_seekbarseat(str(seat[2]))
                                                        self.click_seekbardone()
                                                        self.click_next_btn()
                                                        if self.system_bar():
                                                            if self.verify_select_fields(game[3]):
                                                                self.click_rowandseat()
                                                                self.click_seekbarrow(str(row[3]))
                                                                self.click_seekbarseat(str(seat[3]))
                                                                self.click_seekbardone()
                                                                self.click_next_btn()
                                                                if self.system_bar():
                                                                    if self.is_element_present(
                                                                            self.result) and self.is_element_present(
                                                                            self.welldone) and self.is_element_present(
                                                                            self.hundredpercent) and self.is_element_present(
                                                                            self.resultsummary):
                                                                        return True

    def verify_ticketbox_progress(self, game, row, seat):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.scrolling(self.citytour)
            self.click_ticketbox()
            self.click_playticketbox()
            time.sleep(2.5)
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()

            if self.verify_select_fields(game[0]):
                self.click_rowandseat()
                self.click_seekbarrow(str(row[0]))
                self.click_seekbarseat(str(seat[0]))
                self.click_seekbardone()
                self.click_next_btn()
                if self.verify_select_fields(game[1]):
                    self.click_rowandseat()
                    self.click_seekbarrow(str(row[1]))
                    self.click_seekbarseat(str(seat[1]))
                    self.click_seekbardone()
                    self.click_next_btn()
                    if self.verify_select_fields(game[2]):
                        self.click_rowandseat()
                        self.click_seekbarrow(str(row[2]))
                        self.click_seekbarseat(str(seat[2]))
                        self.click_seekbardone()
                        self.click_next_btn()
                        if self.verify_select_fields(game[3]):
                            self.click_rowandseat()
                            self.click_seekbarrow(str(row[3]))
                            self.click_seekbarseat(str(seat[3]))
                            self.click_seekbardone()
                            self.click_next_btn()
                            if self.is_element_present(self.result) and self.is_element_present(
                                    self.welldone) and self.is_element_present(
                                    self.hundredpercent) and self.is_element_present(self.resultsummary):
                                self.click_done()
                                self.click_close_button()
                                self.click_progress()
                                if self.is_element_present(self.progresstitile) and self.is_element_present(
                                        self.progressticketbox):
                                    return True

import time
from dataProvider.base import Base

class packyourbag(Base):
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
    packyourbag = ('xpath', "//*[contains(@content-desc, 'Pack Your Bags')]")
    snapshot = ('xpath', '//*[contains(@content-desc, "Snapshot")]')
    play_packyourbag = ('xpath', "//*[contains(@content-desc, 'Play Pack Your Bags')]")
    round1description = ('xpath', '//android.view.View[@content-desc="Marie is visiting the coral reef. What items will Marie need for diving in the reef?"]')
    round1 = ('xpath', '//android.view.View[@content-desc="Round 1"]')
    letsgo = ('xpath', '//android.widget.Button[@content-desc="Let’s Go"]')
    divingboots = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Diving01 - 08.png"]/android.widget.ImageView[1]')
    correctanswer =('xpath', '//android.widget.ImageView[@content-desc="button_pyb_tick"]')
    wronganswer = ('xpath', '//android.widget.ImageView[@content-desc="button_pyb_cross"]')
    hikingboots = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Camping02 - 28.png"]/android.widget.ImageView[1]')
    oxygencylinder = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Diving01 - 05.png"]/android.widget.ImageView[1]')
    divingglass = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Diving01 - 26.png"]/android.widget.ImageView[1]')
    jacket = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Fashion02 - 11.png"]/android.widget.ImageView[1]')
    trimmer =('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Bath02 - 04.png"]/android.widget.ImageView[1]')
    climber = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Diving01 - 27.png"]/android.widget.ImageView[1]')
    nightdress = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Travel02 - 05.png"]/android.widget.ImageView[1]')
    round2 =('xpath', '//android.view.View[@content-desc="Round 2"]')
    round2discription = ('xpath', '//android.view.View[@content-desc="Name these other items to add to the packing list"]')
    startround2 = ('xpath', '//android.widget.Button[@content-desc="Start Round 2"]')
    startround3 = ('xpath', '//android.widget.Button[@content-desc="Start Round 3"]')
    round2question = ('xpath', '//android.view.View[@content-desc="What item is this?"]')
    round3 = ('xpath', '//android.view.View[@content-desc="Round 3"]')
    round3discription = ('xpath', "//android.view.View[@content-desc='There's been a change of plans. Listen to the voicemail.']")
    gotit = ('xpath', '//android.widget.Button[@content-desc="Got It"]')
    audiofile = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]')
    round3question = ('xpath', '//android.view.View[@content-desc="Which of these will you need to pack?"]')
    slipper = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Travel04 - 02.png"]')
    passport = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Travel03 - 01.png"]')
    hat = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Beach03 - 04.png"]')
    suite = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Fashion02 - 09.png"]')
    heels = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Shoes02 - 02.png"]')
    hoodies = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Camping02 - 05.png"]')
    sunscreen = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Travel02 - 18.png"]')
    towels = ('xpath', '//android.widget.ImageView[@content-desc="assets/media/images/pack_ur_bags/Beach03 - 18.png"]')
    greatwork = ('xpath', '//android.widget.Button[@content-desc="Great work!"]')
    firstletter =('xpath', '//android.widget.EditText[1]')
    secondletter =('xpath', '//android.widget.EditText[2]')
    thirdletter =('xpath', '//android.widget.EditText[3]')
    forthletter = ('xpath', '//android.widget.EditText[4]')
    fifthletter =('xpath', '//android.widget.EditText[5]')
    sixthletter = ('xpath', '//android.widget.EditText[6]')
    seventhletter = ('xpath', '//android.widget.EditText[7]')
    round1100 = ('xpath','(//android.view.View[@content-desc="100"])[1]')
    round2100 = ('xpath', '(//android.view.View[@content-desc="100"])[2]')
    round3100 = ('xpath', '(//android.view.View[@content-desc="100"])[3]')
    round1question = ('xpath', '//android.view.View[@content-desc="Is this item required for diving?"]')
    paused = ('xpath', '//android.view.View[@content-desc="Paused"]')
    quit = ('xpath', '//android.widget.Button[@content-desc="Quit"]')
    restart = ('xpath', '//android.widget.Button[@content-desc="Restart"]')
    resume = ('xpath', '//android.widget.Button[@content-desc="Resume"]')
    close = ('xpath', '//android.widget.ImageView[@content-desc="close_button"]')
    summary = ('xpath',
               '//android.view.View[@content-desc="Your score shows the percentage of correct answers. \n\nVisit the progress page to track your performance. Many factors can influence your score over time. "]')
    welldone = ('xpath', '//android.widget.Button[@content-desc="Well Done!"]')
    progress = ('xpath', '//android.widget.ImageView[@content-desc="Progress"]')
    progresstitile = ('xpath', '//android.view.View[@content-desc="Progress"]')
    progresspackbag = ('xpath', '//android.widget.ImageView[@content-desc="Pack Your Bags\nRound 1\n100%\nRound 2\n100%\nRound 3\n100%"]')

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(1)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_done(self):
        self.action_perform(self.done)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_packyourbag(self):
        self.scrolling(self.snapshot)
        self.action_perform(self.packyourbag)

    def click_playpackyourbag(self):
        self.action_perform(self.play_packyourbag)

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

    def click_letsgo(self):
        self.action_perform(self.letsgo)

    def click_correctanswer(self):
        self.action_perform(self.correctanswer)

    def click_wronganswer(self):
        self.action_perform(self.wronganswer)

    def click_startround2(self):
        self.action_perform(self.startround2)

    def click_startround3(self):
        self.action_perform(self.startround3)

    def click_firstletter(self):
        self.action_perform(self.firstletter)

    def sentkeys(self, element, value):
        self.send_keys(element,value)

    def click_onaudio(self):
        self.click(self.audiofile)

    def click_ongotit(self):
        self.action_perform(self.gotit)

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

    def verify_packyourbag_landing(self, description):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            if self.page_utils.is_element_present(self.packyourbag) and self.page_utils.is_element_present(
                    self.play_packyourbag) and self.check_element(description):
                return True
            else:
                return False

    def verify_Packyourbag_tutorial(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
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

    def verify_Packyourbag_game(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber):
                                        self.click_correctanswer()
                                        if self.is_element_present(self.nightdress):
                                            self.click_wronganswer()
                                            if self.is_element_present(self.round2) and self.is_element_present(self.round2discription) and self.is_element_present(self.startround2):
                                                self.click_startround2()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'T')
                                                self.sentkeys(self.secondletter,'O')
                                                self.sentkeys(self.thirdletter, 'E')
                                                self.sentkeys(self.forthletter, 'L')
                                                self.sentkeys(self.fifthletter,'S')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'S')
                                                self.sentkeys(self.secondletter,'O')
                                                self.sentkeys(self.thirdletter, 'R')
                                                self.sentkeys(self.forthletter, 'T')
                                                self.sentkeys(self.fifthletter, 'S')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'H')
                                                self.sentkeys(self.secondletter, 'T')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'B')
                                                self.sentkeys(self.secondletter, 'A')
                                                self.click_next_btn()
                                                if self.is_element_present(self.round3):
                                                    self.click_onaudio()
                                                    time.sleep(7)
                                                    self.click_ongotit()
                                                    if self.is_element_present(self.round3question) and self.is_element_present(self.round3) and self.is_element_present(self.slipper):
                                                        self.click_correctanswer()
                                                        if self.is_element_present(self.passport):
                                                            self.click_wronganswer()
                                                            if self.is_element_present(self.hat):
                                                                self.click_correctanswer()
                                                                if self.is_element_present(self.suite):
                                                                    self.click_wronganswer()
                                                                    if self.is_element_present(self.heels):
                                                                        self.click_wronganswer()
                                                                        if self.is_element_present(self.hoodies):
                                                                            self.click_wronganswer()
                                                                            if self.is_element_present(self.sunscreen):
                                                                                self.click_correctanswer()
                                                                                if self.is_element_present(self.towels):
                                                                                    print('true')
                                                                                    self.click_correctanswer()
                                                                                    time.sleep(2)
                                                                                    if self.is_element_present(self.greatwork):
                                                                                        return True

    def verify_Packyourbag_game_titile(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots) and self.is_element_present(self.round1):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots) and self.is_element_present(self.round1):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder) and self.is_element_present(self.round1):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass) and self.is_element_present(self.round1):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket) and self.is_element_present(self.round1):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer) and self.is_element_present(self.round1):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber) and self.is_element_present(self.round1):
                                        self.click_correctanswer()
                                        if self.is_element_present(self.nightdress) and self.is_element_present(self.round1):
                                            self.click_wronganswer()
                                            if self.is_element_present(self.round2) and self.is_element_present(self.round2discription) and self.is_element_present(self.startround2):
                                                self.click_startround2()
                                                if self.is_element_present(self.round2):
                                                    self.click_firstletter()
                                                    self.sentkeys(self.firstletter, 'T')
                                                    self.sentkeys(self.secondletter,'O')
                                                    self.sentkeys(self.thirdletter, 'E')
                                                    self.sentkeys(self.forthletter, 'L')
                                                    self.sentkeys(self.fifthletter,'S')
                                                    self.click_next_btn()
                                                    if self.is_element_present(self.round2):
                                                        self.click_firstletter()
                                                        self.sentkeys(self.firstletter, 'S')
                                                        self.sentkeys(self.secondletter,'O')
                                                        self.sentkeys(self.thirdletter, 'R')
                                                        self.sentkeys(self.forthletter, 'T')
                                                        self.sentkeys(self.fifthletter, 'S')
                                                        self.click_next_btn()
                                                        if self.is_element_present(self.round2):
                                                            self.click_firstletter()
                                                            self.sentkeys(self.firstletter, 'H')
                                                            self.sentkeys(self.secondletter, 'T')
                                                            self.click_next_btn()
                                                            if self.is_element_present(self.round2):
                                                                self.click_firstletter()
                                                                self.sentkeys(self.firstletter, 'B')
                                                                self.sentkeys(self.secondletter, 'A')
                                                                self.click_next_btn()
                                                                if self.is_element_present(self.round3):
                                                                    self.click_onaudio()
                                                                    time.sleep(7)
                                                                    self.click_ongotit()
                                                                    if self.is_element_present(self.round3question) and self.is_element_present(self.round3) and self.is_element_present(self.slipper):
                                                                        self.click_correctanswer()
                                                                        if self.is_element_present(self.passport) and self.is_element_present(self.round3):
                                                                            self.click_wronganswer()
                                                                            if self.is_element_present(self.hat) and self.is_element_present(self.round3):
                                                                                self.click_correctanswer()
                                                                                if self.is_element_present(self.suite) and self.is_element_present(self.round3):
                                                                                    self.click_wronganswer()
                                                                                    if self.is_element_present(self.heels) and self.is_element_present(self.round3):
                                                                                        self.click_wronganswer()
                                                                                        if self.is_element_present(self.hoodies) and self.is_element_present(self.round3):
                                                                                            self.click_wronganswer()
                                                                                            if self.is_element_present(self.sunscreen) and self.is_element_present(self.round3):
                                                                                                self.click_correctanswer()
                                                                                                if self.is_element_present(self.towels) and self.is_element_present(self.round3):
                                                                                                    self.click_correctanswer()
                                                                                                    time.sleep(2)
                                                                                                    if self.is_element_present(self.greatwork) and self.is_element_present(self.summary):
                                                                                                        return True

    def verify_Packyourbag_game_header(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber) and self.is_element_present(self.round1) and self.is_element_present(self.round1question):
                                        self.click_correctanswer()
                                        if self.is_element_present(self.nightdress) and self.is_element_present(
                                                self.round1) and self.is_element_present(self.round1question):
                                            self.click_wronganswer()
                                            if self.is_element_present(self.round2) and self.is_element_present(
                                                    self.round2discription) and self.is_element_present(
                                                    self.startround2):
                                                self.click_startround2()
                                                if self.is_element_present(self.round2) and self.is_element_present(self.round2question):
                                                    self.click_firstletter()
                                                    self.sentkeys(self.firstletter, 'T')
                                                    self.sentkeys(self.secondletter, 'O')
                                                    self.sentkeys(self.thirdletter, 'E')
                                                    self.sentkeys(self.forthletter, 'L')
                                                    self.sentkeys(self.fifthletter, 'S')
                                                    self.click_next_btn()
                                                    if self.is_element_present(self.round2) and self.is_element_present(self.round2question):
                                                        self.click_firstletter()
                                                        self.sentkeys(self.firstletter, 'S')
                                                        self.sentkeys(self.secondletter, 'O')
                                                        self.sentkeys(self.thirdletter, 'R')
                                                        self.sentkeys(self.forthletter, 'T')
                                                        self.sentkeys(self.fifthletter, 'S')
                                                        self.click_next_btn()
                                                        if self.is_element_present(self.round2) and self.is_element_present(self.round2question):
                                                            self.click_firstletter()
                                                            self.sentkeys(self.firstletter, 'H')
                                                            self.sentkeys(self.secondletter, 'T')
                                                            self.click_next_btn()
                                                            if self.is_element_present(self.round2) and self.is_element_present(self.round2question):
                                                                self.click_firstletter()
                                                                self.sentkeys(self.firstletter, 'B')
                                                                self.sentkeys(self.secondletter, 'A')
                                                                self.click_next_btn()
                                                                if self.is_element_present(self.round3):
                                                                    self.click_onaudio()
                                                                    time.sleep(7)
                                                                    self.click_ongotit()
                                                                    if self.is_element_present(self.round3question) and self.is_element_present(
                                                                            self.round3) and self.is_element_present(
                                                                            self.slipper):
                                                                        self.click_correctanswer()
                                                                        if self.is_element_present(
                                                                                self.passport) and self.is_element_present(
                                                                                self.round3) and self.is_element_present(self.round3question):
                                                                            self.click_wronganswer()
                                                                            if self.is_element_present(
                                                                                    self.hat) and self.is_element_present(
                                                                                    self.round3) and self.is_element_present(self.round3question):
                                                                                self.click_correctanswer()
                                                                                if self.is_element_present(
                                                                                        self.suite) and self.is_element_present(
                                                                                        self.round3) and self.is_element_present(self.round3question):
                                                                                    self.click_wronganswer()
                                                                                    if self.is_element_present(
                                                                                            self.heels) and self.is_element_present(
                                                                                            self.round3) and self.is_element_present(self.round3question):
                                                                                        self.click_wronganswer()
                                                                                        if self.is_element_present(
                                                                                                self.hoodies) and self.is_element_present(
                                                                                                self.round3) and self.is_element_present(self.round3question):
                                                                                            self.click_wronganswer()
                                                                                            if self.is_element_present(
                                                                                                    self.sunscreen) and self.is_element_present(
                                                                                                    self.round3) and self.is_element_present(self.round3question):
                                                                                                self.click_correctanswer()
                                                                                                if self.is_element_present(
                                                                                                        self.towels) and self.is_element_present(
                                                                                                        self.round3) and self.is_element_present(self.round3question):
                                                                                                    self.click_correctanswer()
                                                                                                    time.sleep(2)
                                                                                                    if self.is_element_present(
                                                                                                            self.greatwork):
                                                                                                        return True

    def verify_Packyourbag_game_round_Actionbuttons(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            if self.is_element_present(self.lets_play):
                self.click_letsplay()
                self.click_letsgo()
                if self.is_element_present(self.divingboots) and self.is_element_present(self.round1):
                    self.click_correctanswer()
                    if self.is_element_present(self.hikingboots) and self.is_element_present(self.round1):
                        self.click_wronganswer()
                        if self.is_element_present(self.oxygencylinder) and self.is_element_present(self.round1):
                            self.click_correctanswer()
                            if self.is_element_present(self.divingglass) and self.is_element_present(self.round1):
                                self.click_correctanswer()
                                if self.is_element_present(self.jacket) and self.is_element_present(self.round1):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.trimmer) and self.is_element_present(self.round1):
                                        self.click_wronganswer()
                                        if self.is_element_present(self.climber) and self.is_element_present(self.round1):
                                            self.click_correctanswer()
                                            if self.is_element_present(self.nightdress) and self.is_element_present(
                                                    self.round1):
                                                self.click_wronganswer()
                                                if self.is_element_present(self.round2) and self.is_element_present(
                                                        self.round2discription) and self.is_element_present(
                                                        self.startround2):
                                                    self.click_startround2()
                                                    if self.is_element_present(self.round2):
                                                        self.click_firstletter()
                                                        self.sentkeys(self.firstletter, 'T')
                                                        self.sentkeys(self.secondletter, 'O')
                                                        self.sentkeys(self.thirdletter, 'E')
                                                        self.sentkeys(self.forthletter, 'L')
                                                        self.sentkeys(self.fifthletter, 'S')
                                                        self.click_next_btn()
                                                        if self.is_element_present(self.round2):
                                                            self.click_firstletter()
                                                            self.sentkeys(self.firstletter, 'S')
                                                            self.sentkeys(self.secondletter, 'O')
                                                            self.sentkeys(self.thirdletter, 'R')
                                                            self.sentkeys(self.forthletter, 'T')
                                                            self.sentkeys(self.fifthletter, 'S')
                                                            self.click_next_btn()
                                                            if self.is_element_present(self.round2):
                                                                self.click_firstletter()
                                                                self.sentkeys(self.firstletter, 'H')
                                                                self.sentkeys(self.secondletter, 'T')
                                                                self.click_next_btn()
                                                                if self.is_element_present(self.round2):
                                                                    self.click_firstletter()
                                                                    self.sentkeys(self.firstletter, 'B')
                                                                    self.sentkeys(self.secondletter, 'A')
                                                                    self.click_next_btn()
                                                                    if self.is_element_present(self.round3):
                                                                        self.click_onaudio()
                                                                        time.sleep(7)
                                                                        if self.is_element_present(self.gotit):
                                                                            return True

    def verify_Packyourbag_game_close(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            if self.is_element_present(self.lets_play):
                self.click_letsplay()
                self.click_letsgo()
                if self.is_element_present(self.divingboots) and self.is_element_present(self.round1):
                    self.click_correctanswer()
                    if self.is_element_present(self.hikingboots) and self.is_element_present(self.round1):
                        self.click_wronganswer()
                        if self.is_element_present(self.oxygencylinder) and self.is_element_present(self.round1):
                            self.click_correctanswer()
                            if self.is_element_present(self.divingglass) and self.is_element_present(self.round1):
                                self.click_closebutton()
                                self.click_quit()
                                return self.is_element_present(self.packyourbag)

    def verify_Packyourbag_game_result(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber):
                                        self.click_correctanswer()
                                        if self.is_element_present(self.nightdress):
                                            self.click_wronganswer()
                                            if self.is_element_present(self.round2) and self.is_element_present(self.round2discription) and self.is_element_present(self.startround2):
                                                self.click_startround2()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'T')
                                                self.sentkeys(self.secondletter,'O')
                                                self.sentkeys(self.thirdletter, 'E')
                                                self.sentkeys(self.forthletter, 'L')
                                                self.sentkeys(self.fifthletter,'S')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'S')
                                                self.sentkeys(self.secondletter,'O')
                                                self.sentkeys(self.thirdletter, 'R')
                                                self.sentkeys(self.forthletter, 'T')
                                                self.sentkeys(self.fifthletter, 'S')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'H')
                                                self.sentkeys(self.secondletter, 'T')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'B')
                                                self.sentkeys(self.secondletter, 'A')
                                                self.click_next_btn()
                                                if self.is_element_present(self.round3):
                                                    self.click_onaudio()
                                                    time.sleep(7)
                                                    self.click_ongotit()
                                                    if self.is_element_present(self.round3question) and self.is_element_present(self.round3) and self.is_element_present(self.slipper):
                                                        self.click_correctanswer()
                                                        if self.is_element_present(self.passport):
                                                            self.click_wronganswer()
                                                            if self.is_element_present(self.hat):
                                                                self.click_correctanswer()
                                                                if self.is_element_present(self.suite):
                                                                    self.click_wronganswer()
                                                                    if self.is_element_present(self.heels):
                                                                        self.click_wronganswer()
                                                                        if self.is_element_present(self.hoodies):
                                                                            self.click_wronganswer()
                                                                            if self.is_element_present(self.sunscreen):
                                                                                self.click_correctanswer()
                                                                                if self.is_element_present(self.towels):
                                                                                    print('true')
                                                                                    self.click_correctanswer()
                                                                                    time.sleep(2)
                                                                                    if self.is_element_present(self.welldone) and self.is_element_present(self.round1100) and self.is_element_present(self.round2100) and self.is_element_present(self.round3100) and self.is_element_present(self.done) and self.is_element_present(self.summary):
                                                                                        print("true")
                                                                                        return True

    def verify_Packyourbag_game_restart(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber):
                                        self.click_closebutton()
                                        self.click_restart()
                                        return self.is_element_present(self.round1) and self.is_element_present(self.round1description)

    def verify_Packyourbag_game_resume(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber):
                                        self.click_closebutton()
                                        self.click_resume()
                                        time.sleep(5)
                                        return self.is_element_present(self.round1) and self.is_element_present(
                                            self.climber)

    def verify_Packyourbag_game_progress(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            self.click_letsgo()
            if self.is_element_present(self.divingboots):
                self.click_correctanswer()
                if self.is_element_present(self.hikingboots):
                    self.click_wronganswer()
                    if self.is_element_present(self.oxygencylinder):
                        self.click_correctanswer()
                        if self.is_element_present(self.divingglass):
                            self.click_correctanswer()
                            if self.is_element_present(self.jacket):
                                self.click_wronganswer()
                                if self.is_element_present(self.trimmer):
                                    self.click_wronganswer()
                                    if self.is_element_present(self.climber):
                                        self.click_correctanswer()
                                        if self.is_element_present(self.nightdress):
                                            self.click_wronganswer()
                                            if self.is_element_present(self.round2) and self.is_element_present(
                                                    self.round2discription) and self.is_element_present(
                                                    self.startround2):
                                                self.click_startround2()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'T')
                                                self.sentkeys(self.secondletter, 'O')
                                                self.sentkeys(self.thirdletter, 'E')
                                                self.sentkeys(self.forthletter, 'L')
                                                self.sentkeys(self.fifthletter, 'S')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'S')
                                                self.sentkeys(self.secondletter, 'O')
                                                self.sentkeys(self.thirdletter, 'R')
                                                self.sentkeys(self.forthletter, 'T')
                                                self.sentkeys(self.fifthletter, 'S')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'H')
                                                self.sentkeys(self.secondletter, 'T')
                                                self.click_next_btn()
                                                self.click_firstletter()
                                                self.sentkeys(self.firstletter, 'B')
                                                self.sentkeys(self.secondletter, 'A')
                                                self.click_next_btn()
                                                if self.is_element_present(self.round3):
                                                    self.click_onaudio()
                                                    time.sleep(7)
                                                    self.click_ongotit()
                                                    if self.is_element_present(
                                                            self.round3question) and self.is_element_present(
                                                            self.round3) and self.is_element_present(self.slipper):
                                                        self.click_correctanswer()
                                                        if self.is_element_present(self.passport):
                                                            self.click_wronganswer()
                                                            if self.is_element_present(self.hat):
                                                                self.click_correctanswer()
                                                                if self.is_element_present(self.suite):
                                                                    self.click_wronganswer()
                                                                    if self.is_element_present(self.heels):
                                                                        self.click_wronganswer()
                                                                        if self.is_element_present(self.hoodies):
                                                                            self.click_wronganswer()
                                                                            if self.is_element_present(self.sunscreen):
                                                                                self.click_correctanswer()
                                                                                if self.is_element_present(self.towels):
                                                                                    print('true')
                                                                                    self.click_correctanswer()
                                                                                    time.sleep(2)
                                                                                    if self.is_element_present(
                                                                                            self.round1100) \
                                                                                            and self.is_element_present(
                                                                                        self.round2100) and self.is_element_present(
                                                                                        self.round3100) \
                                                                                            and self.is_element_present(
                                                                                        self.done) and self.is_element_present(
                                                                                        self.summary):
                                                                                        self.click_done()
                                                                                        self.click_closebutton()
                                                                                        self.click_progress()
                                                                                        if self.is_element_present(
                                                                                                self.progresspackbag):
                                                                                            return True
                                                                                        else:
                                                                                            return False

    def verify_Packyourbag_game_clock(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_packyourbag()
            self.click_playpackyourbag()
            if self.system_bar():
                self.click_next_btn()
                if self.system_bar():
                    self.click_next_btn()
                    if self.system_bar():
                        self.click_letsplay()
                        if self.system_bar():
                            self.click_letsgo()
                            if self.system_bar() and self.is_element_present(self.divingboots):
                                self.click_correctanswer()
                                if self.system_bar() and self.is_element_present(self.hikingboots):
                                    self.click_wronganswer()
                                    if self.system_bar() and self.is_element_present(self.oxygencylinder):
                                        self.click_correctanswer()
                                        if self.system_bar() and self.is_element_present(self.divingglass):
                                            self.click_correctanswer()
                                            if self.system_bar() and self.is_element_present(self.jacket):
                                                self.click_wronganswer()
                                                if self.system_bar() and self.is_element_present(self.trimmer):
                                                    self.click_wronganswer()
                                                    if self.system_bar() and self.is_element_present(self.climber):
                                                        self.click_correctanswer()
                                                        if self.system_bar() and self.is_element_present(self.nightdress):
                                                            self.click_wronganswer()
                                                            if self.system_bar() and self.is_element_present(self.round2) and self.is_element_present(
                                                                    self.round2discription) and self.is_element_present(
                                                                    self.startround2):
                                                                self.click_startround2()
                                                                if self.system_bar():
                                                                    self.click_firstletter()
                                                                    self.sentkeys(self.firstletter, 'T')
                                                                    self.sentkeys(self.secondletter, 'O')
                                                                    self.sentkeys(self.thirdletter, 'E')
                                                                    self.sentkeys(self.forthletter, 'L')
                                                                    self.sentkeys(self.fifthletter, 'S')
                                                                    self.click_next_btn()
                                                                    if self.system_bar():
                                                                        self.click_firstletter()
                                                                        self.sentkeys(self.firstletter, 'S')
                                                                        self.sentkeys(self.secondletter, 'O')
                                                                        self.sentkeys(self.thirdletter, 'R')
                                                                        self.sentkeys(self.forthletter, 'T')
                                                                        self.sentkeys(self.fifthletter, 'S')
                                                                        self.click_next_btn()
                                                                        if self.system_bar():
                                                                            self.click_firstletter()
                                                                            self.sentkeys(self.firstletter, 'H')
                                                                            self.sentkeys(self.secondletter, 'T')
                                                                            self.click_next_btn()
                                                                            if self.system_bar():
                                                                                self.click_firstletter()
                                                                                self.sentkeys(self.firstletter, 'B')
                                                                                self.sentkeys(self.secondletter, 'A')
                                                                                self.click_next_btn()
                                                                                if self.system_bar() and self.is_element_present(self.round3):
                                                                                    self.click_onaudio()
                                                                                    time.sleep(7)
                                                                                    self.click_ongotit()
                                                                                    if self.system_bar() and self.is_element_present(
                                                                                            self.round3question) and self.is_element_present(
                                                                                            self.round3) and self.is_element_present(self.slipper):
                                                                                        self.click_correctanswer()
                                                                                        if self.system_bar() and self.is_element_present(self.passport):
                                                                                            self.click_wronganswer()
                                                                                            if self.system_bar() and self.is_element_present(self.hat):
                                                                                                self.click_correctanswer()
                                                                                                if self.system_bar() and self.is_element_present(self.suite):
                                                                                                    self.click_wronganswer()
                                                                                                    if self.system_bar() and self.is_element_present(self.heels):
                                                                                                        self.click_wronganswer()
                                                                                                        if self.system_bar() and self.is_element_present(self.hoodies):
                                                                                                            self.click_wronganswer()
                                                                                                            if self.system_bar() and self.is_element_present(self.sunscreen):
                                                                                                                self.click_correctanswer()
                                                                                                                if self.system_bar() and self.is_element_present(self.towels):
                                                                                                                    self.click_correctanswer()
                                                                                                                    time.sleep(2)
                                                                                                                    if self.system_bar() and self.is_element_present(
                                                                                                                            self.round1100) \
                                                                                                                            and self.is_element_present(
                                                                                                                        self.round2100) and self.is_element_present(
                                                                                                                        self.round3100) \
                                                                                                                            and self.is_element_present(
                                                                                                                        self.done) and self.is_element_present(
                                                                                                                        self.summary):
                                                                                                                        return True

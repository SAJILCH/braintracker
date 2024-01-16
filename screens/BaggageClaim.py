from lxml.etree import tounicode

from utilities.Utils import PageUtils
import time
from dataProvider.base import Base


class BaggageClaim(Base):
    click_next = ('xpath', '//android.widget.Button[@content-desc="Next"]')
    no_thanks = ('xpath', '//android.widget.Button[@content-desc="No, thank you"]')
    yes_agree = ('xpath', '//android.widget.Button[@content-desc="Yes, I agree"]')
    how_to_play = ('xpath', "//*[contains(@content-desc, 'How to play')]")
    australia = ('xpath', "//*[contains(@content-desc, 'Australia')]")
    done = ('xpath', '//android.widget.Button[@content-desc="Done"]')
    playnow = ('xpath', "//*[contains(@content-desc, 'Play Now')]")
    baggage_claim = ('xpath', "//*[contains(@content-desc, 'Baggage Claim')]")
    play_baggage_claim = ('xpath', "//*[contains(@content-desc, 'Play Baggage Claim')]")
    lets_play = ('xpath', '//android.widget.Button[@content-desc="Let’s Play"]')
    start_round = ('xpath', "//*[contains(@content-desc, 'Start Round 1')]")
    round1description = ('xpath', '//android.view.View[@content-desc="Collect these bags"]')
    baggageimageelement= ('xpath', '//android.widget.ImageView[contains(@content-desc, *)]/android.widget.ImageView')
    handbagmustadhandbagsuqure = ('xpath', '//android.widget.ImageView[@content-desc="handbag-mustard-squares"]/android.widget.ImageView')
    briefcaseemeraldzigzag = ('xpath', '//android.widget.ImageView[@content-desc="briefcase-emerald-vzigzag"]/android.widget.ImageView')
    handbagskybuletriangle = ('xpath', '//android.widget.ImageView[@content-desc="handbag-skyblue-triangles"]/android.widget.ImageView')
    brieflightgreenirregularexagon = ('xpath', '//android.widget.ImageView[@content-desc="briefcase-lightgreen-irregularexagons"]/android.widget.ImageView')
    suitecaseemeraldzigzag = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-emerald-vzigzag"]/android.widget.ImageView')
    suitecaserosedzigzag = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-rose-zigzag"]/android.widget.ImageView')
    handbaglightgreenirregularexagon = ('xpath', '//android.widget.ImageView[@content-desc="handbag-lightgreen-irregularexagons"]/android.widget.ImageView')
    briefcasenavystripes = ('xpath', '//android.widget.ImageView[@content-desc="briefcase-navy-stripes"]/android.widget.ImageView')
    suitcaselavenderspot = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-lavendar-spots"]/android.widget.ImageView')
    suitcaseskybluetriangle = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-skyblue-triangles"]/android.widget.ImageView')
    suitcasesklightgreenirregularexgagon = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-lightgreen-irregularexagons"]/android.widget.ImageView')
    handbagemeraldzigzag = ('xpath', '//android.widget.ImageView[@content-desc="handbag-emerald-vzigzag"]/android.widget.ImageView')
    suitecaserubystripes = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-ruby-vstripes"]/android.widget.ImageView')
    briefcaseorangepolygon = ('xpath', '//android.widget.ImageView[@content-desc="briefcase-orange-polygons"]/android.widget.ImageView')
    handbagorangepolygon = ('xpath', '//android.widget.ImageView[@content-desc="handbag-orange-polygons"]/android.widget.ImageView')
    suitecasenavystripes = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-navy-stripes"]/android.widget.ImageView')
    briefcaserubystripes = ('xpath', '//android.widget.ImageView[@content-desc="briefcase-ruby-vstripes"]/android.widget.ImageView')
    suitecaselavenderspot = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-lavendar-spots"]/android.widget.ImageView')
    handbagrubystripes = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-lavendar-spots"]/android.widget.ImageView')
    suitecasemustardsquare = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-mustard-squares"]/android.widget.ImageView')
    suitecaseskybluetriangle = ('xpath', '//android.widget.ImageView[@content-desc="suitcase-skyblue-triangles"]/android.widget.ImageView')
    briefcaseskybluetriangle = ('xpath','//android.widget.ImageView[@content-desc="briefcase-skyblue-triangles"]/android.widget.ImageView')

    def click_next_btn(self):
        self.click(self.click_next)
        time.sleep(.5)

    def click_done(self):
        self.action_perform(self.done)

    def click_nothanks(self):
        self.action_perform(self.no_thanks)

    def click_playnow(self):
        self.action_perform(self.playnow)

    def click_baggagecliam(self):
        self.action_perform(self.baggage_claim)

    def click_play_baggagecliam(self):
        self.action_perform(self.play_baggage_claim)

    def verify_select_fields(self, data):
        print(data)
        value = ('xpath', '//*[contains(@content-desc, "' + data + '")]')
        return self.page_utils.is_element_present(value)

    def click_startround(self):
        self.action_perform(self.start_round)

    def click_letsplay(self):
        self.action_perform(self.lets_play)


    def verify_baggage_game(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_baggagecliam()
            return self.page_utils.is_element_present(self.play_baggage_claim)

    def verify_baggageclaim_toutorial(self, tutorial_content):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_baggagecliam()
            self.click_play_baggagecliam()
            time.sleep(2.5)
            for item in tutorial_content:
                if self.verify_select_fields(item):
                    self.click_next_btn()
                    result = True
            return result

    def verify_baggageclaim_round(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_baggagecliam()
            self.click_play_baggagecliam()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            return self.page_utils.is_element_present(self.start_round)

    def verify_baggageclaim_Game(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_nothanks()
        if self.page_utils.is_element_present(self.australia):
            self.click_playnow()
            self.click_baggagecliam()
            self.click_play_baggagecliam()
            self.click_next_btn()
            self.click_next_btn()
            self.click_next_btn()
            self.click_letsplay()
            if self.is_element_present(self.round1description) and self.is_element_present(self.baggageimageelement):
                print("continue")
                a = self.page_utils.is_element_presenttest(self.baggageimageelement)
                print(a)

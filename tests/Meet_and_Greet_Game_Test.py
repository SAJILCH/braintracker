import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.Meet_ad_Greet import *
from utilities.ReadExcel import *
from utilities.Utils import PageUtils


class meetandgreet_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_023")
    def test_verify_meet_and_greet(self):
        cntry = meetandgreet(self.driver)
        description = PageUtils.read_datas_from_excel(self.driver, 'OnboardScreen', 'A20')
        self.assertTrue(cntry.verify_meet_and_greet(description))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_024")
    def test_verify_meet_and_greet_tutorial(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreettutorial')
        tutorial_cnt = []
        for inner_list in content:
            tutorial_cnt.append(inner_list[0])
        self.assertTrue(cntry.verify_meet_and_greet_tutorial_content(tutorial_cnt))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_025")
    def test_verify_meet_and_greet_game_details(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreettutorial')
        game_deatils = []
        for inner_list in content:
            game_deatils.append(inner_list[1])
        self.assertTrue(cntry.verify_meet_and_greet_game_details(game_deatils))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_026")
    def test_verify_meet_and_greet_game_step1(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
        print(game_deatils[0])
        question_1 = game_deatils[0]
        question_2 = game_deatils[1]
        game_answer_1 = game_answer[0]
        self.assertTrue(cntry.verify_meet_and_greet_step1(question_1, game_answer_1, question_2))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_027")
    def test_verify_meet_and_greet_game_step2(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
        print(game_deatils[0])
        question_1 = game_deatils[0]
        question_2 = game_deatils[1]
        question_3 = game_deatils[2]
        game_answer_1 = game_answer[0]
        game_answer_2 = game_answer[1]
        self.assertTrue(
            cntry.verify_meet_and_greet_step2(question_1, game_answer_1, question_2, question_3, game_answer_2))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_028")
    def test_verify_meet_and_greet_game_step3(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
        self.assertTrue(cntry.verify_meet_and_greet_step3(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_029")
    def test_verify_meet_and_greet_game_step4(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
        self.assertTrue(cntry.verify_meet_and_greet_step4(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_030")
    def test_verify_meet_and_greet_game_video(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_game_video(game_deatils, game_answer, game_toutorial[0]))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_031")
    def test_verify_meet_and_greet_round2_step1(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_game_round2_Step1(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_032")
    def test_verify_meet_and_greet_round2_step2(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_game_round2_Step2(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_033")
    def test_verify_meet_and_greet_round2_step3(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_game_round2_Step3(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_034")
    def test_verify_meet_and_greet_round2_step4(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_game_round2_Step4(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_035")
    def test_verify_meet_and_greet_gameresult(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_game_result(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_039")
    def test_verify_meet_and_greet_progress(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_progress(game_deatils, game_answer))

    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BT_TC_P3_024")
    def test_verify_meet_and_greet_clock(self):
        cntry = meetandgreet(self.driver)
        content = read_excel('Austraila_MeetandGreet')
        game_deatils = []
        game_answer = []
        game_toutorial = []
        for inner_list in content:
            game_deatils.append(inner_list[2])
            game_answer.append(inner_list[3])
            game_toutorial.append(inner_list[4])
        self.assertTrue(cntry.verify_meet_and_greet_progress(game_deatils, game_answer))


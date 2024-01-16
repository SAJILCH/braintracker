import softest
import pytest
from flaky import flaky

from tests.base_test import BaseTests
from screens.Country_and_Game import *
from utilities.ReadExcel import *


class country_test(BaseTests, softest.TestCase):
    @flaky(configuration.initial_setup.get("re_run_count"))
    @pytest.mark.regression
    @pytest.mark.describe("Test case Id - BP_TC_012")
    def test_verify_visiblity_of_how_to_play(self):
        cntry = country(self.driver)
        courses = read_excel('Austraila_courses')
        course_name = []
        for inner_list in courses:
            course_name.append(inner_list[0])
        self.assertTrue(cntry.verfy_courses_in_country(course_name))


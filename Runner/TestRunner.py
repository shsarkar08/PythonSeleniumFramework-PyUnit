import unittest
import SN_Tests.Test_SN_Auto
import os, datetime
import HtmlTestRunner


                                            ###############################################
                                            ####      Service NOW Ticket Creation      ####
                                            ####      Test Runner File                 ####
                                            ###############################################


class TestRunnerTestSuite(unittest.TestCase):

    current_directory = os.getcwd()
    time_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def test_runner(self):
        # Create a TestSuite comprising the test cases.
        suite_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        suite_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SN_Tests.Test_SN_Auto.TestServiceNow)
            # unittest.defaultTestLoader.loadTestsFromModule(SN_Tests.Test_SN_Auto.ServiceNow)
        ])

        output_file = open(self.current_directory + "\\Test Summary_" + self.time_now + "", "w")

        # Add Report path
        report_path = "..\\Reports"

        html_runner = HtmlTestRunner.HTMLTestRunner(

            stream=output_file,
            output=report_path,
            report_title='Test Results',
            # report_name=''
            # To combine reports for test cases
            # combine_reports = True

        )

        html_runner.run(suite_test)

# if __name__=='__main__':
#     unittest.main()

from log_files import show_time_of_pid
import unittest

class TestLogTimeOfPID(unittest.TestCase):
    def test_string_not_found(self):
        testcase = "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"
        expected = None

        self.assertEqual(show_time_of_pid(testcase), expected)

    def test_found_string(self):
        testcase = "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
        expected = "Jul 6 14:01:2 pid:29440"

        self.assertEqual(show_time_of_pid(testcase), expected)

if __name__ == '__main__':
    unittest.main()

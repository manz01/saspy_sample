import os
import unittest
from unittest.mock import patch, MagicMock

# Patch saspy before importing sas_setup
with patch.dict('sys.modules', {'saspy': MagicMock()}):
    from utils import sas_setup

class TestSasSetup(unittest.TestCase):

    @patch('utils.sas_setup.saspy.SASsession')
    def test_start_sas_session_with_env_set(self, mock_sassession):
        os.environ["SASPY_CFG"] = "/fake/path/to/sascfg_personal.py"

        mock_instance = MagicMock()
        mock_sassession.return_value = mock_instance

        session = sas_setup.start_sas_session()

        mock_sassession.assert_called_once_with(cfgfile="/fake/path/to/sascfg_personal.py")
        self.assertEqual(session, mock_instance)

    def test_start_sas_session_with_env_missing(self):
        if "SASPY_CFG" in os.environ:
            del os.environ["SASPY_CFG"]

        with self.assertRaises(EnvironmentError):
            sas_setup.start_sas_session()

    def test_print_sas_log(self):
        result = {"LOG": "This is a SAS log"}
        with patch("builtins.print") as mock_print:
            sas_setup.print_sas_log(result)
            mock_print.assert_any_call("-" * 25, "SAS LOG", "-" * 25)
            mock_print.assert_any_call("This is a SAS log")

    def test_sas_output_creates_file(self):
        test_dir = "/tmp/test_sas_output"
        test_filename = "output.html"
        test_content = "<html><body>Hello</body></html>"

        output_path = sas_setup.sas_output(test_dir, test_filename, test_content)

        self.assertTrue(os.path.exists(output_path))
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, test_content)

        # Cleanup
        os.remove(output_path)
        os.rmdir(test_dir)

if __name__ == '__main__':
    unittest.main()

"""
    DiGA API

    API zum DiGA-Verzeichnis https://diga.bfarm.de/de/ des Bundesinstituts für Arzneimittel und Medizinprodukte BfArM. Das Verzeichnis bietet eine Auswahl an digitalen Gesundheitsanwendungen (DiGA), die vom BfArM gemäß § 139e SGB V bewertet wurden.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.diga.api.default_api import DefaultApi  # noqa: E501

from deutschland import diga


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_apps_get(self):
        """Test case for apps_get

        Liste aller DiGAs  # noqa: E501
        """
        pass

    def test_apps_id_get(self):
        """Test case for apps_id_get

        Detail-Informationen zu einer DiGa.  # noqa: E501
        """
        pass

    def test_prescriptions_get(self):
        """Test case for prescriptions_get

        Technische Informationen zu einer DiGa.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

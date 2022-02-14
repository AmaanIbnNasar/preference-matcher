import unittest

from PreferenceMatcher import PreferenceMatcher

preferencesObj = {
      "placements": [
          {
            "directorate": "Data Services",
            "name": "Adult Social Care Statistics",
            "numberOfGrads": 1
          },
          {
            "directorate": "Data Services",
            "name": "Business Intelligence/Data Visualisation",
            "numberOfGrads": 1
          },
          {
            "directorate": "Data Services",
            "name": "Data Management/Engineering",
            "numberOfGrads": 2
          },
          {
            "directorate": "Data Services",
            "name": "Turing Tribe",
            "numberOfGrads": 1
          },
          {
            "directorate": "Platforms",
            "name": "Data Quality Dashboards",
            "numberOfGrads": 2
          },
          {
            "directorate": "Platforms",
            "name": "Spine Core",
            "numberOfGrads": 3
          },
          {
            "directorate": "Product Development",
            "name": "NHS Pathways - Development Team",
            "numberOfGrads": 1
          },
          {
            "directorate": "Product Development",
            "name": "NHS Pathways - Reporting Team",
            "numberOfGrads": 1
          },
          {
            "directorate": "Product Development",
            "name": "111 Online - Developer",
            "numberOfGrads": 1
          },
          {
            "directorate": "IT Operations (Including Cyber Security)",
            "name": "Cyber Security",
            "numberOfGrads": 1
          },
          {
            "directorate": "IT Operations (Including Cyber Security)",
            "name": "Core Infrastructure Services - Networks",
            "numberOfGrads": 1
          },
          {
            "directorate": "IT Operations (Including Cyber Security)",
            "name": "Core Infrastructure Services - Sustainable Hybrid Cloud",
            "numberOfGrads": 1
          },
          {
            "directorate": "IT Operations (Including Cyber Security)",
            "name": "Live Services - IT Operations Centre",
            "numberOfGrads": 1
          }
        ],
      "preferences": [
        {
          "name": "Amaan Ibn-Nasar",
          "firstPreference": "Spine Core",
          "secondPreference": "Adult Social Care Statistics",
          "thirdPreference": "111 Online - Developer"
        },
        {
          "name": "Abbie Prescott",
          "firstPreference": "Live Services - IT Operations Centre",
          "secondPreference": "Cyber Security",
          "thirdPreference": "Data Quality Dashboards"
        },
        {
          "name": "Adam Carruthers",
          "firstPreference": "Core Infrastructure Services - Networks",
          "secondPreference": "Spine Core",
          "thirdPreference": "111 Online - Developer"
        },
        {
          "name": "Alice Tapper",
          "firstPreference": "Business Intelligence/Data Visualisation",
          "secondPreference": "Cyber Security",
          "thirdPreference": "Turing Tribe"
        },
        {
          "name": "Amelia Noonan",
          "firstPreference": "Data Quality Dashboards",
          "secondPreference": "Business Intelligence/Data Visualisation",
          "thirdPreference": "Cyber Security"
        },
        {
          "name": "Anna Evans",
          "firstPreference": "Cyber Security",
          "secondPreference": "Turing Tribe",
          "thirdPreference": "NHS Pathways - Development Team"
        },
        {
          "name": "Benjamin Wallace",
          "firstPreference": "Adult Social Care Statistics",
          "secondPreference": "111 Online - Developer",
          "thirdPreference": "Spine Core"
        },
        {
          "name": "Joel Helbling",
          "firstPreference": "NHS Pathways - Development Team",
          "secondPreference": "Cyber Security",
          "thirdPreference": "Turing Tribe"
        },
        {
          "name": "Joseph Wilson",
          "firstPreference": "Spine Core",
          "secondPreference": "Data Quality Dashboards",
          "thirdPreference": "Core Infrastructure Services - Networks"
        },
        {
          "name": "Laura Thirft",
          "firstPreference": "Data Management/Engineering",
          "secondPreference": "NHS Pathways - Reporting Team",
          "thirdPreference": "Core Infrastructure Services - Networks"
        },
        {
          "name": "Maisie Blyth",
          "firstPreference": "Spine Core",
          "secondPreference": "Turing Tribe",
          "thirdPreference": "Core Infrastructure Services - Sustainable Hybrid Cloud"
        },
        {
          "name": "Mitul Dattani",
          "firstPreference": "Core Infrastructure Services - Sustainable Hybrid Cloud",
          "secondPreference": "Data Quality Dashboards",
          "thirdPreference": "Spine Core"
        },
        {
          "name": "Nathan Gregory",
          "firstPreference": "Live Services - IT Operations Centre",
          "secondPreference": "Data Management/Engineering",
          "thirdPreference": "Cyber Security"
        },
        {
          "name": "Nathan Pettit",
          "firstPreference": "111 Online - Developer",
          "secondPreference": "Spine Core",
          "thirdPreference": "Turing Tribe"
        },
        {
          "name": "Oluwadamiloju Makinde",
          "firstPreference": "Data Quality Dashboards",
          "secondPreference": "Business Intelligence/Data Visualisation",
          "thirdPreference": "Turing Tribe"
        },
        {
          "name": "Roshaan Bajwa",
          "firstPreference": "Turing Tribe",
          "secondPreference": "Spine Core",
          "thirdPreference": "Cyber Security"
        },
        {
          "name": "Scott Caldwell-Nichols",
          "firstPreference": "Data Management/Engineering",
          "secondPreference": "NHS Pathways - Reporting Team",
          "thirdPreference": "Spine Core"
        },
        {
          "name": "Zahra Ahmed",
          "firstPreference": "NHS Pathways - Reporting Team",
          "secondPreference": "111 Online - Developer",
          "thirdPreference": "Data Management/Engineering"
        }
      ]
    }

class PreferenceMatcherTest(unittest.TestCase):

  def setUp(self) -> None:
    self.preferenceMatcher = PreferenceMatcher()
  
  
  def test_readPreferenceFile(self):
    self.assertEqual(preferencesObj, self.preferenceMatcher.readPreferenceFile())
    

if __name__ == "__main__":
  unittest.main()
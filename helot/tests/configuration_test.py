import os
import unittest

from helot.configuration import configuration, ConfigurationError

_CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
_RESOURCES_DIR = os.path.join(_CURRENT_DIR, 'resources')
_CONIFIGURATION_FILENAME = os.path.join(_RESOURCES_DIR, 'sample.yaml')
_INVALID_CONIFIGURATION_FILENAME = os.path.join(_RESOURCES_DIR, 'invalid.yaml')
configuration.initialize(_CONIFIGURATION_FILENAME)


class TestConfiguration(unittest.TestCase):
    def test_testing_mode(self):
        self.assertEqual(configuration.name, "Martin D'vloper")
        self.assertEqual(configuration.job, "Developer")
        self.assertEqual(configuration.skill, "Elite")
        self.assertEqual(configuration.employed, True)
        self.assertEqual(configuration.age, 24)
        self.assertEqual(configuration.foods, ['Apple', 'Mango', 1234])
        self.assertEqual(configuration.languages.perl, 'Elite')
        self.assertEqual(configuration.languages.object_oriented.best,
                         ['C++', 'C#'])
        self.assertEqual(configuration.languages.object_oriented.great, 'Java')

    def test_invalid_configuration_filename(self):
        with self.assertRaises(FileNotFoundError):
            configuration.initialize("invalid.nonexisting")

    def test_invalid_yaml(self):
        with self.assertRaises(ConfigurationError):
            configuration.initialize(_INVALID_CONIFIGURATION_FILENAME)

    def test_instantiation_of_configuration(self):
        with self.assertRaises(ConfigurationError):
            _ = configuration()

"""Implements the configuration details."""

import yaml


class ConfigurationError(Exception):
    """Configuration Error."""


class _ConfigurationMeta(type):
    """Metaclass for configuration adding class level properties."""

    def __getattr__(self, item):
        """Propagates the item to the object representing the yaml."""
        if item == '__test__':
            return
        if self._configuration and hasattr(self._configuration, item):
            return getattr(self._configuration, item)

    def __call__(self, *args, **kwargs):
        """Disallows instantiation."""
        raise ConfigurationError


class configuration(metaclass=_ConfigurationMeta):
    """Exposes configuration settings.

    A setting can be accessed using "dot" resolution, meaning like a class level
    attribute following the structure of the yaml configuration file that was
    used to call the initialize method.

    This class is never supposed to be instantiated; instead it must be used as
    a "static" C++ class meaning proving access only to its class level members.
    """

    _configuration = None

    @classmethod
    def initialize(cls, filename):
        """Sets the execution mode.

        :parameter filename: (str) The yaml configuration filename.

        :raises FileNotFoundError: filename does not exist.
        :raises ConfigurationError: Parsing error.
        """
        try:
            with open(filename, 'r') as stream:
                configuration._configuration = _make_obj(yaml.load(stream))
        except yaml.parser.ParserError:
            raise ConfigurationError('Parsing error')


class _Object(object):
    """Dummy class used for the conversion of a dict to a python object."""


def _make_obj(item):
    """Used to convert a dictionary to a python object.

    :param item: Can either be a dictionary, a list / tuple or a scalar.

    :return: The corresponding python object.
    """
    if isinstance(item, dict):
        obj = _Object()
        for key, value in item.items():
            setattr(obj, key, _make_obj(value))
        return obj
    elif isinstance(item, (list, tuple)):
        return [_make_obj(x) for x in item]
    return item

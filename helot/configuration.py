"""Implements the configuration details."""
import os
import yaml
import json
import logging


class ConfigurationError(Exception):
    """Configuration Error."""


class DataHolderObject(object):
    """Used for the conversion of a dict to a python object."""

    def __getattr__(self, item):
        """Permits for x1.x2.y1 = value syntax."""
        if item == '__test__':
            return

        if item not in self.__dict__:
            setattr(self, item, DataHolderObject())

        return self.__dict__.get(item)


class _ConfigurationMeta(type, DataHolderObject):
    """Metaclass for configuration adding class level properties."""

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

    @classmethod
    def reset(cls):

        to_delete = []
        for attr_name in dir(cls):
            if attr_name.startswith('__') and attr_name.endswith('__'):
                continue
            if callable(getattr(cls, attr_name)):
                continue
            to_delete.append(attr_name)

        for attr_name in to_delete:
            delattr(cls, attr_name)



    @classmethod
    def initialize(cls, data_holder=None, **kwargs):
        """Sets the execution mode.

        :parameter data_holder: Can be one of the following:
            (str) The yaml configuration filename.
            (dict) A dict containing key - value pairs.

        :parameter **kwargs: key-value pairs to add in the configuration.

        :raises FileNotFoundError: filename does not exist.
        :raises ConfigurationError: Parsing error.
        """
        try:
            cls.reset()
            if not data_holder:
                data_holder = {}
            data_as_dict = None
            if isinstance(data_holder, dict):
                data_as_dict = data_holder
            elif isinstance(data_holder, str) and os.path.isfile(data_holder):
                if data_holder.endswith('json'):
                    data_as_dict = json.load(open(data_holder))
                elif data_holder.endswith('yaml'):
                    data_as_dict = yaml.load(open(data_holder))
            data_as_dict.update(kwargs)
            for key, value in data_as_dict.items():
                setattr(cls, key, _make_obj(value))
        except Exception as ex:
            logging.exception(ex)
            raise ConfigurationError(ex)


def _make_obj(item):
    """Used to convert a dictionary to a python object.

    :param item: Can either be a dictionary, a list / tuple or a scalar.

    :return: The corresponding python object.
    """
    if isinstance(item, dict):
        obj = DataHolderObject()
        for key, value in item.items():
            setattr(obj, key, _make_obj(value))
        return obj
    elif isinstance(item, (list, tuple)):
        return [_make_obj(x) for x in item]
    else:
        return item

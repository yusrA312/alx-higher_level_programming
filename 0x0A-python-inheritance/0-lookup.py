#!/usr/bin/python3
'''Module for lookup method.'''


def lookup(obj):
    '''Looks up object.
    Args:
        obj (object):to list.

    Returns:
	list: of attributes.
    '''
    return dir(obj)

# -*- coding: utf-8 -*-

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# Memoize.py ---
#                     --------------------------------
#                          Copyright (c) 2013
#                           Laurent CAPOCCHI
#                         University of Corsica
#                     --------------------------------
# Version 3.1                                        last modified: 11/12/2012
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# GENERAL NOTES AND REMARKS:
#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# GLOBAL VARIABLES AND FUNCTIONS
#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

class memoized(object):
	"""Decorator that caches a function's return value each time it is called.
		If called later with the same arguments, the cached value is returned, and
		not re-evaluated.
	"""

	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args):
		try:
			return self.cache[args]
		except KeyError:
			value = self.func(*args)
			self.cache[args] = value
			return value
		except TypeError:
			# uncachable -- for instance, passing a list as an argument.
			# Better to not cache than to blow up entirely.
			return self.func(*args)

	def __repr__(self):
		"""Return the function's docstring."""
		return self.func.__doc__

	def __get__(self, obj, objtype):
		"""Support instance methods."""
		return functools.partial(self.__call__, obj)
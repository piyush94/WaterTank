__author__ = 'piyush'

from distutils.core import setup
import py2exe

setup(windows=["WaterTank.py"], options={"py2exe" : {"includes" : ["sip"]}})

#!/usr/bin/python3
import sys
from configparser import ConfigParser

class ReadConfig():
    def __init__(self, config_file):
        try:
            f = open(config_file)
            f.close()
        except FileNotFoundError:
            print("Config File Doesn't exist")
            sys.exit()
        except:
            print("Unexpected Error:", sys.exc_info())
            sys.exit()
        parser = ConfigParser()
        parser.read(config_file)
        self.parser = parser


    def get_config(self, sections, keys):
        return self.parser.get(sections, keys)
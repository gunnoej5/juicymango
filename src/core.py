#########################################################################
# Filename: core.py
# Description: Core functions for SpicyMango.
# Copyright (C) 2011-2012 Chris Centore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or any later 
#    version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# SpicyMango written by: Chris Centore, Steve Swann, Jason Gunnoe
# Website: https://github.com/gunnoej5/juicymango
# Download: svn co http://spicymango.googlecode.com/svn/trunk/ spicymango/
#
#########################################################################

import os,re,sys,json,configparser,logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Read in code to dynamically get the name of this module.
from src.getname import module








# Get configuation options from the config file.
def check_config(param):
	config = configparser.ConfigParser()
	config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
	try:
		config.read(config_path)
		# Remove the trailing '=' from the parameter name
		param_name = param.rstrip('=')
		return config['DEFAULT'][param_name]
	except Exception as e:
		logging.error(f"{module}: Cannot read configuration file or parameter: {e}")
		sys.exit()

# Get Keyword/Module pairs from the keywords file.
def get_keywords(param):
        path = os.path.join(os.path.dirname(__file__), '..', 'keywords')
        try:
                fileopen = open(path, "r")
        except:
                logging.error(f"{module}: Cannot find keywords file. Make sure its in the spicymango directory.")
		sys.exit()
	wordlist = []
        # iterate through lines in file
        for line in fileopen:
                if not re.search('#.', line):
                        match = re.search(param, line)
                        if match:
				wordlist.append(json.loads(line))
        return wordlist

def get_feeds(param):
	path = os.path.join(os.path.dirname(__file__), '..', 'feeds')
        try:
                fileopen = open(path, "r")
        except:
                logging.error(f"{module}: Cannot find feeds file. Make sure its in the spicymango directory.")
                sys.exit()
        feedlist = []
        # iterate through lines in file
        for line in fileopen:
                if not re.search('^#.', line):
			match = re.search('http', line)
                	if match:
				feedlist.append(json.loads(line))
        return feedlist

def log_error(mod, keyword, error):
	import datetime
	sys.stderr.write('%s | %s | SEARCH_TERM: %s | ERROR: %s\n' % (datetime.datetime.now(), mod, keyword, error))
	logging.error(f"{mod}: Keyword: {keyword} - Thread exited with Error")

# -*- coding: utf-8 -*-
"""
	MongoHQURL
	~~~~~~~~~~

	A utility for converting a MONGOHQ  url to an object so that mongo engine can connect to it.

	usage:
	------
	from util import MongoHQURL
	from mongoengine import *

	con_obj = MongoHQURL('mongodb://user:pass@server.mongohq.com/db_name')
	connect(con_obj.database, username=con_obj.username, password=con_obj.password, port=int(con_obj.port), host=con_obj.host)

	:copyright: (c) 2012 by Trevor Kimenye.
	:license: http://www.apache.org/licenses/LICENSE-2.0.txt.
"""
class MongoHQURL():
	def __init__(self,connection_str):
		self.c_str = connection_str.lstrip('mongodb://')

		has_sec = self.c_str.find("@") > -1
		usr_idx = self.c_str.find(':')

		if has_sec:
			if usr_idx > -1:
				self.username = self.c_str[:usr_idx]
				self.c_str = self.c_str.lstrip(self.username)
				self.c_str = self.c_str.lstrip(':')

			pass_idx = self.c_str.find('@')
			if pass_idx > -1:
				self.password = self.c_str[:pass_idx]
				self.c_str = self.c_str.lstrip(self.password)
				self.c_str = self.c_str.lstrip('@')
		else:
			self.username = ''
			self.password = ''

		has_port = self.c_str.find(':') > -1

		host_idx = self.c_str.find('/')
		if host_idx > -1:
			host_hldr = self.c_str[:host_idx]
			if has_port:
				tokens = host_hldr.split(':')
				self.host = tokens[0]
				self.port = tokens[1]
			self.c_str = self.c_str.lstrip(host_hldr)
			self.c_str = self.c_str.lstrip('/')
		else:
			self.host = 'localhost'

		self.database = self.c_str

# -*- coding: utf-8 -*-
# Copyright (c) 2021, irenee and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name}'
	def after_insert(self):
		doc = frappe.get_doc('Library Member', self.name)
	# 	full_name = doc.get_full_name()
	# 	frappe.msgprint(f'{full_name}thank you for registering')
    # def get_full_name(self):
	# 	frappe.msgprint(f'{self.first_name} {self.last_name}')

	
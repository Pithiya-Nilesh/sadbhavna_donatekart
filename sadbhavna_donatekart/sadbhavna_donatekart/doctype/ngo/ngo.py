# Copyright (c) 2023, Sanskar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries
from frappe.utils import get_datetime_str, formatdate


class NGO(Document):
	def autoname(self):
		_date = formatdate(get_datetime_str(self.creation), "dd-mm-yyyy")
		org_name = self.organisation_name.strip()[0:5].replace(" ","-") if self.requester_type == 'NGO' else self.full_name.strip()[0:5]
		autoname = "{0}-{1}-{2}-".format(self.requester_type.strip()[0:3],org_name,_date)
		self.name = autoname.upper()+getseries(org_name, 2)
	pass

# Copyright (c) 2023, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import getseries
from frappe.utils import get_datetime_str, formatdate
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class DonationCampaign(WebsiteGenerator):
	def autoname(self):
		_date = formatdate(get_datetime_str(self.creation), "dd-mm-yyyy")
		org_name = self.campaign_title.strip()[0:7].replace(" ","-")
		autoname = "{0}-{1}-".format(org_name,_date)
		self.name = autoname.upper()+getseries(org_name, 4)

	def before_save(self):
		if self.status=='Live' and frappe.get_doc("Donation Campaign", self.name).status!="Live":
			ngo=frappe.get_doc("NGO", self.ngo)
			# print("\n\n\Changed",self.ngo.email,frappe.db.exists("User", "jane@example.org"))
	pass

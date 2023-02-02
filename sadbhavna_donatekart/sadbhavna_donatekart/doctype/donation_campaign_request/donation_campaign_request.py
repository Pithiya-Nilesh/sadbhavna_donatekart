# Copyright (c) 2023, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class DonationCampaignrequest(Document):
	pass

@frappe.whitelist()
def check_ngo_exists(ngo):
	# check ngo exists with ngo email
	ngo_exists_flag = ''
	filters = frappe.db.sql(
		"SELECT `name` FROM `tabNGO` WHERE email=%s",(ngo),
		as_dict=1,
	)
	if filters:
		ngo_exists_flag = filters[0].name
	return ngo_exists_flag
	
@frappe.whitelist()
def update_campaign_request(campaign_request,ngo,campaign,update_status_to):
	# update Campaign request 
	campaign_request = frappe.get_doc("Donation Campaign request", campaign_request)
	campaign_request.status = update_status_to
	campaign_request.ngo = ngo
	campaign_request.campaign = campaign
	campaign_request.save()
	

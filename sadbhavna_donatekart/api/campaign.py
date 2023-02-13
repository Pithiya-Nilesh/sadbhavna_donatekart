import frappe

@frappe.whitelist(allow_guest=True)
def get_campaign_detail(name):
    # return name
    return frappe.db.get_value("Donation Campaign", filters={"name": name}, fieldname=["*"], as_dict=True)
    # return frappe.db.get_all("Donation Campaign", )


# @frappe.whitelist(allow_guest=True)
# def get_campaign_detail(name):
#     doc = frappe.get_doc("Donation Campaign", name)
#     doc = doc.__dict__
#     return doc

@frappe.whitelist(allow_guest=True)
def request_campaign(full_name, email, phone, campaign_story, social_media_page, beneficiary_group, campaign_type, organisation_website='', organisation_name='',):
    doc = frappe.get_doc({"doctype": "Donation Campaign request", "full_name": f"{full_name}", "email": f"{email}", "phone": f"{phone}", "campaign_story": f"{campaign_story}", "requester_type": f"{campaign_type}", "beneficiary_group": f"{beneficiary_group}", "social_media_page": f"{social_media_page}", "organisation_website": f"{organisation_website}", "organisation_name": f"{organisation_name}" })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    
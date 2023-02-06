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
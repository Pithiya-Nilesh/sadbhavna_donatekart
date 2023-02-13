# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_recent_donation(name):
#     return frappe.db.get_value("Donation", filters={"campaign": name, "anonymous": 0})
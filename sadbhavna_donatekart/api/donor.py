import frappe

# @frappe.whitelist(allow_guest=True)
# def get_recent_donation(name):
#     return frappe.db.get_value("Donation", filters={"campaign": name, "anonymous": 0})

@frappe.whitelist(allow_guest=True)
def download_80g(donor, donation, date):
    donor = frappe.db.get_value("Donor", filters={"email": donor}, fieldname=["name"])
    doc = frappe.get_doc({"doctype": "Tax Exemption 80G Certificate", "recipient": "Donor", "donor": donor, "date": date, "donation": donation})
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    doc = frappe.get_last_doc("Tax Exemption 80G Certificate")
    return doc.name
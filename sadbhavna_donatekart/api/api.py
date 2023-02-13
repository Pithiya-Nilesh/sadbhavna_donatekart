import frappe
from frappe.utils import today


@frappe.whitelist(allow_guest=True)
def get_recent_donation(name):
    return frappe.db.get_list("Donation", filters={"campaign": name}, fields=["name","donor_name", "amount", "creation", "anonymous", "donor_image"])
    # return frappe.db.sql(f"select donor.image, donor.donor_name, donation.name, donation.amount, donation.creation, donation.anonymous from `tabDonation` as donation inner join `tabDonor` as donor on donation.donor = donor.name where donation.name='{name}'")


@frappe.whitelist(allow_guest=True)
def register(first_name, last_name, email, password, phone_number, pan_number):
    # doc = frappe.new_doc('User')
    # doc.email = email,
    # doc.first_name = first_name,
    # doc.last_name = last_name,
    # doc.new_password = password,
    # doc.phone = phone_number
    # doc.insert(ignore_permissions=True)   

    user = frappe.get_doc({"doctype": "User", "email": f"{email}", "first_name": f"{first_name}", "last_name": f"{last_name}", "phone": f"{phone_number}", "new_password": f"{password}" })
    user.insert(ignore_permissions=True)
    frappe.db.commit()
    donor = frappe.get_doc({"doctype": "Donor", "email": f"{email}", "donor_name": f"{first_name} {last_name}", "mobile": f"{phone_number}", "donor_type": "Defult", "pan_number": f"{pan_number}"}) 
    donor.insert(ignore_permissions=True)
    frappe.db.commit() 

@frappe.whitelist(allow_guest=True)
def set_details_in_doctype_after_donation(user_id, campaign, item, price):
    donor = frappe.db.get_value("Donor", filters={"email": f"{user_id}"}, fieldname=["name"], pluck="name")
    donation = frappe.get_doc({"doctype": "Donation", "donor": donor, "campaign": f"{campaign}", "date": today(), "amount": price, "donation_item": [{"item": item, "qty": 1, "rate": price, "amount": price}]}) 
    donation.insert(ignore_permissions=True)
    frappe.db.commit()

    # raised_amount = frappe.db.get_value("Donation Campaign", filters={"name": campaign}, fieldname=["raised_amount"], pluck="name")
    raised_amount, donation_amount = frappe.db.get_value("Donation Campaign", filters={"name": campaign}, fieldname=["raised_amount", "donation_amount"])
    total = int(price) + int(raised_amount)
    if total >= int(donation_amount):
        frappe.db.set_value("Donation Campaign", campaign, "raised_amount", total)
        frappe.db.set_value("Donation Campaign", campaign, "published", 0)
    else:
        frappe.db.set_value("Donation Campaign", campaign, "raised_amount", total)

from frappe.auth import LoginManager
from sadbhavna_donatekart.api.autologin import login_via_oauth2, login_via_oauth2_id_token
import frappe
from frappe.utils import today

import base64
import json
from typing import TYPE_CHECKING, Callable

import jwt
import frappe.utils
from frappe import _
from frappe.utils.password import get_decrypted_password
# from frappe.utils.oauth import login_via_oauth2, login_via_oauth2_id_token


if TYPE_CHECKING:
    from frappe.core.doctype.user.user import User


class SignupDisabledError(frappe.PermissionError):
    ...


@frappe.whitelist(allow_guest=True)
def get_recent_donation(name):
    return frappe.db.get_list("Donation", filters={"campaign": name}, fields=["name", "donor_name", "amount", "creation", "anonymous", "donor_image"])
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

    user = frappe.get_doc({"doctype": "User", "email": f"{email}", "first_name": f"{first_name}",
                          "last_name": f"{last_name}", "phone": f"{phone_number}", "new_password": f"{password}"})
    user.insert(ignore_permissions=True)
    frappe.db.commit()
    donor = frappe.get_doc({"doctype": "Donor", "email": f"{email}", "donor_name": f"{first_name} {last_name}",
                           "mobile": f"{phone_number}", "donor_type": "Defult", "pan_number": f"{pan_number}"})
    donor.insert(ignore_permissions=True)
    frappe.db.commit()

# @frappe.whitelist(allow_guest=True)
# def set_details_in_doctype_after_donation(user_id, campaign, item, price):
#     donor = frappe.db.get_value("Donor", filters={"email": f"{user_id}"}, fieldname=["name"], pluck="name")
#     donation = frappe.get_doc({"doctype": "Donation", "donor": donor, "campaign": f"{campaign}", "date": today(), "amount": price, "donation_item": [{"item": item, "qty": 1, "rate": price, "amount": price}]})
#     donation.insert(ignore_permissions=True)
#     frappe.db.commit()

#     # raised_amount = frappe.db.get_value("Donation Campaign", filters={"name": campaign}, fieldname=["raised_amount"], pluck="name")
#     raised_amount, donation_amount = frappe.db.get_value("Donation Campaign", filters={"name": campaign}, fieldname=["raised_amount", "donation_amount"])
#     total = int(price) + int(raised_amount)
#     if total >= int(donation_amount):
#         frappe.db.set_value("Donation Campaign", campaign, "raised_amount", total)
#         frappe.db.set_value("Donation Campaign", campaign, "published", 0)
#     else:
#         frappe.db.set_value("Donation Campaign", campaign, "raised_amount", total)


@frappe.whitelist(allow_guest=True)
def set_details_in_doctype_after_donation(user_id, campaign, item, amount, payment_id):
    donor = frappe.db.get_value(
        "Donor", filters={"email": f"{user_id}"}, fieldname=["name"], pluck="name")
    donation = frappe.get_doc({"doctype": "Donation", "donor": donor, "campaign": f"{campaign}",
                              "date": today(), "amount": amount, "donation_item": item, "payment_id": payment_id})
    donation.insert(ignore_permissions=True)
    frappe.db.commit()

    # raised_amount = frappe.db.get_value("Donation Campaign", filters={"name": campaign}, fieldname=["raised_amount"], pluck="name")
    raised_amount, donation_amount = frappe.db.get_value("Donation Campaign", filters={
                                                         "name": campaign}, fieldname=["raised_amount", "donation_amount"])
    total = int(amount) + int(raised_amount)
    if total >= int(donation_amount):
        frappe.db.set_value("Donation Campaign", campaign,
                            "raised_amount", total)
        frappe.db.set_value("Donation Campaign", campaign, "published", 0)
    else:
        frappe.db.set_value("Donation Campaign", campaign,
                            "raised_amount", total)


@frappe.whitelist(allow_guest=True)
def login_with_google(email, last_name='', first_name='', image_url=''):
    user_exists = frappe.db.get_value("User", filters={'email': email})

    if not user_exists:
        user = frappe.get_doc({"doctype": "User", "email": email, "last_name": last_name,
                              "first_name": first_name, "user_image": image_url, "new_password": frappe.generate_hash()})
        user.insert(ignore_permissions=True)
        frappe.db.commit()
        donor = frappe.get_doc({"doctype": "Donor", "email": f"{email}", "donor_name": f"{first_name} {last_name}",
                                "donor_type": "Defult", "image": f"{image_url}"})
        donor.insert(ignore_permissions=True)
        frappe.db.commit()
    else:
        doc = frappe.get_doc("User", email)
        doc.update(
            {
                "enabled": 1,
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "user_image": image_url,
                "new_password": frappe.generate_hash()
            }
        )
        doc.save(ignore_permissions=True)
        donor = frappe.db.get_value(
        "Donor", filters={"email": f"{email}"}, fieldname=["name"], pluck="name")
        doc = frappe.get_doc("Donor", donor)
        doc.update(
            {
                "email": f"{email}",
                "donor_name": f"{first_name} {last_name}",
                "donor_type": "Defult",
                "image": f"{image_url}"
            }
        )
        doc.save(ignore_permissions=True)

    return login_user(email)


def login_user(user):
    frappe.local.login_manager.user = user
    frappe.local.login_manager.post_login()
    frappe.db.commit()

    login_token = frappe.generate_hash(length=32)
    frappe.cache().set_value(
        f"login_token:{login_token}", frappe.local.session.sid, expires_in_sec=120
    )
    print("\n\n login token", login_token, "\n\n")
    # return login_token
    return login_via_token(login_token)


@frappe.whitelist(allow_guest=True)
def login_via_token(login_token: str):
    print("\n\n called",  login_token, "\n\n")
    sid = frappe.cache().get_value(f"login_token:{login_token}", expires=True)
    if not sid:
        frappe.respond_as_web_page(_("Invalid Request"), _(
            "Invalid Login Token"), http_status_code=417)
        return

    frappe.local.form_dict.sid = sid
    frappe.local.login_manager = LoginManager()
    return True

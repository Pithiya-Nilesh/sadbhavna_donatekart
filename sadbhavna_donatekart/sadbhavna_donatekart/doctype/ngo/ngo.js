// Copyright (c) 2023, Sanskar and contributors
// For license information, please see license.txt

let prev_page_route = ['','','']
let is_form_new = false
frappe.ui.form.on('NGO', {
	refresh: function(frm) {
		prev_page_route = frappe.get_prev_route()
	},
	before_save: function(frm) {
		is_form_new = frm.doc.name.includes('new')
	},
	after_save:function(frm){
		if( prev_page_route[1]==='Donation Campaign request' && is_form_new ){
			frappe.call({
				method: "sadbhavna_donatekart.sadbhavna_donatekart.doctype.donation_campaign_request.donation_campaign_request.update_campaign_request",
				args: {'campaign_request': prev_page_route[2] ,'ngo': frm.doc.name,'campaign':'','update_status_to':'Verified'},
				freeze: true,
				callback: function(r) {
					frappe.set_route("Form", "Donation Campaign request", prev_page_route[2]);
					is_form_new = false
				}
			});
		}
	}
});

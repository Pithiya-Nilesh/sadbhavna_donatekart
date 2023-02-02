// Copyright (c) 2023, Sanskar and contributors
// For license information, please see license.txt
let prev_page_route = ['','','']
let is_form_new = false
frappe.ui.form.on('Donation Campaign', {
	refresh: function(frm) {
		prev_page_route = frappe.get_prev_route()
		if(frm.doc.ngo){
			frm.events.show_go_to_ngo_campaign_form(frm,"NGO",frm.doc.ngo);
		}
		if(frm.doc.campaign_request){
			frm.events.show_go_to_ngo_campaign_form(frm,"Donation Campaign Request",frm.doc.campaign_request);
		}
				
	},
	before_save: function(frm) {
		is_form_new = frm.doc.name.includes('new')
	},
	after_save:function(frm){
		if(prev_page_route[1]==='Donation Campaign request' && is_form_new ){
			frappe.call({
				method: "sadbhavna_donatekart.sadbhavna_donatekart.doctype.donation_campaign_request.donation_campaign_request.update_campaign_request",
				args: {'campaign_request': prev_page_route[2] ,'ngo': frm.doc.ngo,'campaign':frm.doc.name,'update_status_to':'Pending Campaign'},
				freeze: true,
				callback: function(r) {
					is_form_new = false
				}
			});
		}
	},
	show_go_to_ngo_campaign_form: function(frm,type,name) {
		// open NGO page
		frm.add_custom_button(__(`${type}`), function() {
			frappe.set_route("Form",type,name);
		});
	}
});




// Copyright (c) 2023, Sanskar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Donation Campaign request', {
	refresh: function(frm) {
		if(!frm.doc.name.includes('new')){
			if(frm.doc.status==='New Request'){
				frm.events.show_add_to_ngo_form(frm);
			}else if(frm.doc.ngo){
				frm.events.show_go_to_doctype(frm,frm.doc.requester_type,frm.doc.ngo);
				switch(frm.doc.status){
					case "Verified":
						frm.events.show_add_campaign_form(frm);
						break;
					case "Pending Campaign":
						frm.events.show_go_to_doctype(frm,"Donation Campaign",frm.doc.campaign);
						break;
					default:
						break;
				}
			}
		}
	},
	show_add_to_ngo_form: function(frm) {
		// check if ngo exist with requester email
		var default_ngo=''
		frappe.call({
			args: {
				"ngo": frm.doc.email,
			},
			method: "sadbhavna_donatekart.sadbhavna_donatekart.doctype.donation_campaign_request.donation_campaign_request.check_ngo_exists",
			callback: function(r) {
				default_ngo = r.message
			}
		})
		// Add request to NGO button on click open dialog
		frm.add_custom_button(__(`Add request to ${frm.doc.requester_type}`), function() {
			let dialog = new frappe.ui.Dialog({
				title: __(`Add request to ${frm.doc.requester_type}`),
				fields: [
					{
						"label" : __(`Select ${frm.doc.requester_type}`),
						"fieldname": "ngo",
						"fieldtype": "Link",
						"options": "NGO",
						"reqd": 1,
						"default": default_ngo,
					},
				],
				primary_action_label: `Add to ${frm.doc.requester_type}`,
				primary_action: function() {
					const data = dialog.get_values();
					frappe.call({
						method: "sadbhavna_donatekart.sadbhavna_donatekart.doctype.donation_campaign_request.donation_campaign_request.update_campaign_request",
						args: {'campaign_request':frm.doc.name,'ngo':data.ngo,'campaign':'','update_status_to':'Verified'},
						freeze: true,
						callback: function(r) {
							dialog.hide();
						}
					});
					dialog.hide();
				},
			});
			dialog.show();

			// on create a new NGO click open new doc and fetch data from campaign request
			frappe.ui.form.ControlLink.prototype.new_doc = function(e) {
				if(this.df.fieldname==='ngo'){
					frappe.model.with_doctype("NGO", function() {
						var doc = frappe.model.get_new_doc("NGO");
						doc.organisation_name = frm.doc.organisation_name;
						doc.organisation_website = frm.doc.organisation_website;
						doc.email = frm.doc.email
						doc.phone = frm.doc.phone
						doc.full_name = frm.doc.full_name
						doc.requester_type = frm.doc.requester_type
						frappe.set_route("Form", "NGO", doc.name);                                                                        
					})
				}
				return false;
			}
		});
	},
	show_go_to_doctype: function(frm,type,name) {
		// open NGO page
		frm.add_custom_button(__(`${type}`), function() {
			if(type==='Indivisual/Group'){
				type='NGO'
			}
			frappe.set_route("Form",type,name);
		});
	},
	show_add_campaign_form:function(frm){
		frm.add_custom_button(__(`Add Campaign`), function() {
			frappe.model.with_doctype("NGO", function() {
				var doc = frappe.model.get_new_doc("Donation Campaign");
				doc.ngo = frm.doc.ngo
				doc.campaign_request = frm.doc.name
				doc.status = 'Pending'
				frappe.set_route("Form", "Donation Campaign", doc.name);
			})
		});
	}
});

frappe.ui.form.on('Timesheet Detail', {
    is_billable: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        console.log(locals[cdt][cdn])
        
        if (d.is_billable) {
            // Retrieve the rate from employee if it exists; assume the rates from the activity type has already been retrieve
            frappe.call({
                method: "legal_project.legal_project_management.overrides.bill_cost_rates.get_employee_rates",
                args: {
                    employee: frm.doc.employee
                },
                callback: function(r) {
                    if (!r.exc) {
                        let exchange_rate = flt(frm.doc.exchange_rate);
                        frappe.model.set_value(cdt, cdn, "base_billing_rate", flt(r.message.billing_rate));
                        frappe.model.set_value(cdt, cdn, "billing_rate", flt(r.message.billing_rate) * exchange_rate);
                        frappe.model.set_value(cdt, cdn, "base_costing_rate", flt(r.message.costing_rate));
                        frappe.model.set_value(cdt, cdn, "costing_rate", flt(r.message.costing_rate) * exchange_rate);
                    }
                }
            });
        }
    },
});
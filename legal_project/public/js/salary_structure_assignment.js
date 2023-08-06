frappe.ui.form.on('Salary Structure Assignment', {
    refresh: function(frm) {
        if (frm.doc.docstatus == 1) {
            frm.add_custom_button(__("Override Employee Rates"), function() {
                frappe.confirm(__("Are you sure you want to override the employee rates?"),
                () => {
                    frm.trigger("override_employee_rates")
                })
            })
        }
    },

    on_submit: function(frm) {
        // If the Override checkbox is set then trigger the override_employee_rates function
        if (frm.doc.override_employee_default_billing_and_costing_rate) {
            frappe.confirm(__("Are you sure you want to override the employee rates?"),
            () => {
                frm.trigger("override_employee_rates")
            })
        }
    },
    
    override_employee_rates: function(frm) {
        frappe.call({
            method: "legal_project.legal_project_management.overrides.bill_cost_rates.override_employee_rates",
            args: {
                "employee": frm.doc.employee,
                "salary_structure": frm.doc.salary_structure
            },
            callback: function(r) {
                if (r.exc) {
                    frappe.msgprint(r.message);
                }
            }
        });
    }
});

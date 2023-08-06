import frappe
from frappe import _

@frappe.whitelist()
def override_employee_rates(employee, salary_structure):
    salary_structure_doc = frappe.get_doc("Salary Structure", salary_structure)
    employee_doc = frappe.get_doc("Employee", employee)
    print("Salary Structure: " + salary_structure_doc.name)

    # Override the rates in the salary structure with the rates in the employee record
    employee_doc.default_billing_rate = salary_structure_doc.default_billing_rate
    employee_doc.ctc = salary_structure_doc.default_costing_rate
    employee_doc.billing_uom = salary_structure_doc.default_unit_of_measure
    employee_doc.save()

    return "success"


@frappe.whitelist()
def get_employee_rates(employee):
    employee_doc = frappe.get_doc("Employee", employee)

    # If default_billing_rate is not set, retrieve from salary structure
    if employee_doc.default_billing_rate:
        rates = {"billing_rate": employee_doc.default_billing_rate, "costing_rate": employee_doc.ctc, "uom": employee_doc.billing_uom}
    else:
        sql = '''SELECT
                    default_billing_rate as billing_rate, 
                    default_costing_rate as costing_rate,
                    default_unit_of_measure as uom
                 FROM
                    `tabSalary Structure` 
                 WHERE name = (SELECT salary_structure FROM `tabSalary Structure Assignment`
                    ORDER BY from_date DESC LIMIT 1
                    WHERE employee = "%{employee}s")'''
        rates = frappe.db.sql(sql, {"employee": employee}, as_dict=True)[0]

    print(rates)

    if rates["uom"] == "Hour":
        divisor = 1
    elif rates["uom"] == "Daily":
        divisor = 8
    elif rates["uom"] == "Weekly":
        divisor = 40
    elif rates["uom"] == "Monthly":
        divisor = 160
    
    rates["billing_rate"] = rates["billing_rate"] / divisor
    rates["costing_rate"] = rates["costing_rate"] / divisor

    return rates    
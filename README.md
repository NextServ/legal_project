## Legal Project Management

Extends existing Project Management module to accommodate requirements of a law firm

### License

MIT

### To Do

#### Salary Structure
- Add fields:
    - Default bill rate under the Currency field - DONE
    - Unit selection: Hour, Day, Week, Month - DONE

#### Salary Structure Assignment
- Add Override Employee Billing and Costing Rate checkbox - DONE
- If the above is checked, the values in the corresponding fields in the Employee doctype should be overridden - DONE

#### Employee
- Add fields:
    - Default bill rate under the Salary tab - this defaults to Default bill rate in Salary Structure if it exists - DONE
    - Unit selection: Hour, Day, Week, Month - this defaults to Unit in Salary Structure if it exists - DONE
- Use Cost-to-Company (CTC) as the default cost in Activity Cost - DONE

#### Activity Cost
- Default value in Billing Rate should be the one based on the bill rate field on the Employee doctype - DONE
- Default value in Costing Rate should be the one based on the CTC field of - DONE

#### Timesheet
- Calculate Total Billable Amount and Total Costing Amount based on the applicable rates from the Activity Cost - DONE

### Change Log

#### 0.0.1
1. Default Billing Rate, Costing Rate and UoM selection fields addedd to Salary Structure doctype
1. Added Override Employee Billing and Costing Rates checkbox in Salary Structure Assignment doctype
1. Default Billing Rate, UoM selection and Costing Rate to Employee doctype
1. When creating a new timesheet entry, the system retrieve default billing and costing rate from the Employee doctype if it exists, otherwise it'll use the default values from the applicable Activity Type
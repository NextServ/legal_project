## Legal Project Management

Extends existing Project Management module to accommodate requirements of a law firm

### License

MIT

### To Do

#### Salary Structure
- Add fields:
    - Default bill rate under the Currency field
    - Unit selection: Hour, Day, Week, Month

#### Employee
- Add fields:
    - Default bill rate under the Salary tab - this defaults to Default bill rate in Salary Structure if it exists
    - Unit selection: Hour, Day, Week, Month - this defaults to Unit in Salary Structure if it exists
- Use Cost-to-Company (CTC) as the default cost in Activity Cost

#### Activity Cost
- Default value in Billing Rate should be the one based on the bill rate field on the Employee doctype
- Default value in Costing Rate should be the one based on the CTC field of 
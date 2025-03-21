# Copyright 2017 Comunitea Servicios Tecnológicos S.L.
# Copyright 2018-19 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "HR Attendance RFID",
    "version": "14.0.1.1.2",
    "category": "Human Resources",
    "website": "https://github.com/OCA/hr-attendance",
    "author": "Comunitea, ForgeFlow, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["hr_attendance"],
    "data": [
        "security/hr_attendance_rfid.xml",
        "security/ir.model.access.csv",
        "data/ir_rule.xml",
        "views/hr_employee_view.xml",
    ],
}

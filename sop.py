from odoo import api, fields, models

class Sop(models.Model):
    _name = "management.sop"
    
    name = fields.Text("SOP Name", size=100)
    no = fields.Char("No", require=True, size=10)
    code = fields.Text("Code", require=True, size=100)
    date_issued = fields.Date("Date Issued", require=True, size=100)
    date_review = fields.Date("Date Review", size=50)
    date_revised = fields.Date("Date Revised", size=100)
from odoo import api, fields, models

class Bcp(models.Model):
    _name = "management.bcp"
    
    name = fields.Text("BCP Name", size=100)
    no = fields.Char("No", require=True, size=10)
    code = fields.Text("Code", require=True, size=100)
    date_issued = fields.Date("Date Issued", require=True, size=100)
    date_review = fields.Date("Date Review", size=50)
    date_revised = fields.Date("Date Revised", size=100)
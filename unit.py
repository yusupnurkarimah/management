from odoo import api, fields, models

class Unit(models.Model):
    _name = "management.unit"
    
    name = fields.Text("Nama Unit", size=100)
    no = fields.Char("No", require=True, size=10)
    no_unit = fields.Text("No Unit", size=100)
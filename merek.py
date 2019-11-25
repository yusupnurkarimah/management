from odoo import api, fields, models

class Merek(models.Model):
    _name = "management.merek"
    
    name = fields.Text("Merk", size=100)
    no = fields.Char("No", require=True, size=10)
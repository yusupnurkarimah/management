from odoo import api, fields, models

class Capacity(models.Model):
    _name = "management.capacity"
    
    name = fields.Text("Rack", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    used = fields.Text("Used", size=100)
    available = fields.Char("Available", require=True, size=100)
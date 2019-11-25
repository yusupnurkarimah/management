from odoo import api, fields, models

class Kode(models.Model):
    _name = "management.kode"
    
    name = fields.Text("Golongan Perangkat", size=100)
    no = fields.Char("No", require=True, size=10)
    no_perangkat = fields.Char("No Perangkat", require=True, size=10)
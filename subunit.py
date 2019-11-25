from odoo import api, fields, models

class Subunit(models.Model):
    _name = "management.subunit"
    
    name = fields.Text("Nama Sub Unit", size=100)
    no = fields.Char("No", require=True, size=10)
    kode = fields.Char("Kode/Golongan Perangkat", require=True, size=10)
    no_subunit = fields.Text("No Sub Unit", size=100)
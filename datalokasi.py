from odoo import api, fields, models

class Datalokasi(models.Model):
    _name = "management.datalokasi"
    
    name = fields.Text("Lokasi", size=100)
    no = fields.Char("No", require=True, size=10)
    no_lokasi = fields.Text("No Lokasi", require=True, size=100)
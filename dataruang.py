from odoo import api, fields, models

class Dataruang(models.Model):
    _name = "management.dataruang"
    
    name = fields.Text("Lokasi", size=100)
    no = fields.Char("No", require=True, size=10)
    no_ruang = fields.Text("No Ruang", require=True, size=100)
    nama_ruang = fields.Text("Nama Ruang", require=True, size=100)
from odoo import api, fields, models

class Kelompok(models.Model):
    _name = "management.kelompok"
    
    name = fields.Char("Kode", require=True, size=10)
    no = fields.Char("No", require=True, size=10)
    no_kelompok_perangkat = fields.Char("No Kelompok Perangkat", require=True, size=10)
    nama_kelompok_perangkat = fields.Text("Nama Kelompok Perangkat", size=100)
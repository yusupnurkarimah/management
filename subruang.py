from odoo import api, fields, models

class Dataruang(models.Model):
    _name = "management.subruang"
    
    name = fields.Text("Ruang", size=100)
    no = fields.Char("No", require=True, size=10)
    no_subruang = fields.Text("No Sub Ruang", require=True, size=100)
    nama_subruang = fields.Text("Nama Sub Ruang", require=True, size=100)
from odoo import api, fields, models

class Layout(models.Model):
    _name = "management.layout"
    
    name = fields.Text("SKPD/UKPD/Pemilik", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    ruang = fields.Text("Ruang/Posisi", size=100)
    no_reg = fields.Char("No.Reg/SN/IP", require=True, size=100)
    model = fields.Text("Merk/Model/Tipe", size=50)
    spesifikasi = fields.Text("Spesifikasi", size=100)
    fungsi = fields.Text("Fungsi", size=50)
    visit = fields.Char("Visit", size=10)
    note = fields.Text("Note", size=100)
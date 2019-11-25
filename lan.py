from odoo import api, fields, models

class Lan(models.Model):
    _name = "management.lan"
    
    name = fields.Many2one(comodel_name="management.dataruang", string="Ruang", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    posisi = fields.Text("Posisi", size=100)
    no_reg = fields.Char("No.Reg/SN/IP", require=True, size=100)
    model = fields.Many2one(comodel_name="management.dataruang", string="Merk/Model/Tipe", size=50)
    fungsi = fields.Text("Fungsi", size=100)
    koneksi_list = fields.Text("Koneksi List", size=50)
    distribution = fields.Char("Distribution", size=50)
    visit = fields.Char("Visit", size=10)
    note = fields.Text("Note", size=100)
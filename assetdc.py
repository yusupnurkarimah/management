from odoo import api, fields, models

class Asset(models.Model):
    _name = "management.assetdc"
    
    name = fields.Char("Name", require=True, size=10)
    pemilik = fields.Many2one(comodel_name="hr.employee", string="SKPD/UKPD/Pemilik", require=True, size=100)
    ruang = fields.Many2one(comodel_name="management.dataruang", string="Ruang/Posisi", size=100)
    no_reg = fields.Char("No.Reg/SN/IP", require=True, size=100)
    model = fields.Many2one(comodel_name="management.merek", string="Merk/Model/Tipe", size=50)
    spesifikasi = fields.Text("Spesifikasi", size=100)
    fungsi = fields.Text("Fungsi", size=50)
    visit = fields.Char("Visit", size=10)
    note = fields.Text("Note", size=100)
    maintenance_id = fields.One2many(comodel_name="management.maintenance",
    	inverse_name="assetdc_id",
    	string="Maintenance", required=False)
    image_small = fields.Binary(string="Image Small",)
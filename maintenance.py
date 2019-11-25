from odoo import api, fields, models

class Maintenance(models.Model):
    _name = "management.maintenance"
    
    name = fields.Char("Tiket", size=100)
    no = fields.Char("No", require=True, size=10)
    tgl_berkunjung = fields.Date("Tgl.Berkunjung", require=True, size=100)
    tujuan = fields.Char("Tujuan", require=True, size=100)
    keterangan = fields.Text("Keterangan", size=50)
    status = fields.Text("Status", size=100)
    assetdc_id = fields.Many2one(comodel_name="management.assetdc",	string="assetdc")
    assetnondc_id = fields.Many2one(comodel_name="management.assetnondc",	string="assetnondc")
from odoo import api, fields, models

class Berita(models.Model):
    _name = "management.berita"
    
    name = fields.Text("Judul", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    tgl_posting = fields.Date("Tgl.Posting", size=100)
    publish = fields.Char("Publish", require=True, size=10)
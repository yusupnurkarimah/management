from odoo import api, fields, models

class SDM(models.Model):
    _name = "management.sdm"
    
    name = fields.Text("Nama", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    kode = fields.Text("Kode", size=100)
    kelamin = fields.Char("Kelamin", require=True, size=100)
    usia = fields.Text("Usia", size=50)
    pendidikan = fields.Text("Pendidikan", size=100)
    telp = fields.Text("Telp/HP", size=50)
    email = fields.Char("Email", size=10)
    file = fields.Text("File", size=100)
    pengalaman = fields.Char("Pengalaman", size=10)
    catatan = fields.Text("Catatan", size=100)
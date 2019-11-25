from odoo import api, fields, models

class Datauser(models.Model):
    _name = "management.datauser"
    
    name = fields.Text("Username", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    identitas = fields.Text("Identitas", size=100)
    nama_lengkap = fields.Char("Nama Lengkap", require=True, size=100)
    level = fields.Text("Level", size=50)
    blokir = fields.Text("Blokir", size=100)
    pemandu = fields.Text("Pemandu", size=50)
    pengelola = fields.Char("Pengelola", size=50)
    temp_admin = fields.Char("Temp Admin", size=10)
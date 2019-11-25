from odoo import api, fields, models

class Agenda(models.Model):
    _name = "management.agenda"
    
    name = fields.Text("Tema", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    tgl_mulai = fields.Date("Tgl.Mulai", size=100)
    tgl_selesai = fields.Date("Tgl.Selesai", require=True, size=100)
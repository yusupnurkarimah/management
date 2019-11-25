from odoo import api, fields, models

class Perangkat(models.Model):
    _name = "management.perangkat"
    
    name = fields.Char("OS/Merk", require=True, size=100)
    no = fields.Char("No", require=True, size=10)
    cpu = fields.Char("CPU", size=100)
    ram = fields.Char("RAM", require=True, size=100)
    disk = fields.Text("DISK", size=50)
    traffic_in_out = fields.Text("Traffic In/Out ", size=100)
    fungsi = fields.Text("Fungsi/Note", size=50)
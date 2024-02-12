from odoo import fields, models

class InternMentorProfile(models.Model):
    _name = 'intern.mentor.profile'
    _description = "Mentor's Profile"

    name = fields.Char(required=True)
    email = fields.Char()
    phone_number = fields.Char()
    department = fields.Char(required=True) #TODO: we can directly fetch the department from the name and vice versa
    
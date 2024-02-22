from odoo import fields, models, api

class InternMentorProfile(models.Model):
    _name = 'intern.mentor.profile'
    _description = "Mentor's Profile"

    # Fields
    name = fields.Char(required=True)
    email = fields.Char()
    phone_number = fields.Char()

    # Relations
    department_id = fields.Many2one('intern.department', string="Department") #TODO: we can directly fetch the department from the name and vice versa
    intern_ids = fields.One2many('intern.profile', 'mentor_id', string="Interns")

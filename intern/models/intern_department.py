from odoo import fields, models

class InternDepartment(models.Model):
    _name = 'intern.department'
    _description = 'Intern Department'

    # Fields
    name = fields.Char(required=True)
    description = fields.Text()

    # Relations
    mentor_ids = fields.One2many('intern.mentor.profile', 'department_id', string="Mentors")

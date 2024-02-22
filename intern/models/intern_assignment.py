from odoo import fields, models

class InternAssignment(models.Model):
    _name = 'intern.assignment'
    _description = 'Intern Assignment'

    # Fields
    name = fields.Char('Title', required=True)
    description = fields.Text()
    start_date = fields.Date(default=fields.Date.today(), required=True)
    end_date = fields.Date()
    maximum_marks = fields.Float(default=100, required=True)

    # Relations
    project_id = fields.Many2one('intern.project', string='Project')
    assignment_status_ids = fields.One2many('intern.assignment.status', 'assignment_id', string="Assignment Status")

from odoo import fields, models

class InternAssignment(models.Model):
    _name = 'intern.assignment'
    _description = 'Intern Assignment'

    title = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Date(default=fields.Date.today(), required=True)
    end_date = fields.Date()
    status = fields.Selection([('unassigned', 'Unassigned'), ('assigned', 'Assigned'), ('ongoing', 'Ongoing'), ('completed', 'Completed')], default='unassigned', required=True)
    feedback = fields.Text()
    # intern_id = fields.Many2one('intern.profile', string='Intern')  TODO associate intern and project
    # project_id = fields.Many2one('intern.project', string='Project')
    
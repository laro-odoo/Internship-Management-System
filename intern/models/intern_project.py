from odoo import fields, models

class InternProject(models.Model):
    _name = 'intern.project'
    _description = 'Intern Project'

    title = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Date(default=fields.Date.today(), required=True)
    end_date = fields.Date()
    status = fields.Selection([('ongoing', 'Ongoing'), ('completed', 'Completed')], default='ongoing', required=True)
    # intern_id = fields.Many2one('intern.profile', string='Intern')
    # mentor_id = fields.Many2one('intern.mentor.profile', string='Mentor')
    
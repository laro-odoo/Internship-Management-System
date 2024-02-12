from odoo import fields, models

class InternReport(models.Model):
    _name = 'intern.report'
    _description = 'Intern Report'

    title = fields.Char(required=True)
    report_date = fields.Date(default=fields.Date.today(), required=True)
    report_details = fields.Text()
    # intern_id = fields.Many2one('intern.profile', string='Intern') # TODO
    # project_id = fields.Many2one('intern.project', string='Project')
    
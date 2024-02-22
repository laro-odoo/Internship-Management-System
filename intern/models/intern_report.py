from odoo import fields, models, api
import base64

class InternReport(models.Model):
    _name = 'intern.report'
    _description = 'Intern Report'

    # Fields
    name = fields.Char('Title', required=True)
    report_date = fields.Date(default=fields.Date.today(), required=True)
    report_details = fields.Text()
    status = fields.Selection([
        ('created', 'Created'),
        ('submitted', 'Submitted'),
        ('unsubmit', 'Unsubmitted')
    ], default='created')
    file = fields.Binary('File')
    filename = fields.Char(string='Filename')


    # Relations
    intern_id = fields.Many2one('intern.profile', string='Intern', required=True) # TODO
    project_id = fields.Many2one('intern.project', string='Project', required=True)

    @api.model
    def create(self, vals):
        file = vals.get('file')
        if file:
            vals['file'] = base64.b64encode(file.read())
            vals['filename'] = file.filename
        return super(self).create(vals)

    def action_submit(self):
        self.status = 'submitted'
    
    def action_unsubmit(self):
        self.status = 'unsubmit'

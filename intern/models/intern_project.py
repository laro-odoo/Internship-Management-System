from odoo import fields, models, api

class InternProject(models.Model):
    _name = 'intern.project'
    _description = 'Intern Project'
    
    # Fields
    name = fields.Char('Title', required=True)
    description = fields.Text()

    # Relations
    mentor_id = fields.Many2one('intern.mentor.profile', string='Mentor')
    project_status_ids = fields.One2many('intern.project.status', 'project_id', string="Project Status")
    assignment_ids = fields.One2many('intern.assignment', 'project_id', string="Assignments")
    report_ids = fields.One2many('intern.report', 'project_id', string="Reports")
    submitted_reports = fields.One2many('intern.report', 'project_id', string="Submitted Reports", compute='_compute_submitted_reports')

    @api.depends('report_ids')
    def _compute_submitted_reports(self):
        self.submitted_reports = self.report_ids.search([('status', '=', 'submitted')])

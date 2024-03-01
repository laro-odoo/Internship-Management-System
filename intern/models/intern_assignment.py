from odoo import fields, models, api

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

    @api.model
    def create(self, vals):
        assign = super().create(vals)
        project_status = self.env['intern.project.status'].search([('project_id', '=', assign.project_id.id), ('status', '!=', 'completed')])
        for status in project_status:
            self.env['intern.assignment.status'].create({
                'assignment_id': assign.id,
                'intern_id': status.intern_id.id,
            })
        return assign

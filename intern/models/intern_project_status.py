from odoo import fields, models, api

class InternProjectStatus(models.Model):
    _name = 'intern.project.status'
    _description = 'Status of the project according to the intern'

    # Fields
    start_date = fields.Date(default=fields.Date.today(), required=True)
    end_date = fields.Date()
    status = fields.Selection([
        ('assigned','Assigned'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
    ],
    default='assigned')
    completion_percentage = fields.Float(string='Progress', compute='_compute_completion_percentage')

    # Relations
    intern_id = fields.Many2one('intern.profile', string='Intern')
    project_id = fields.Many2one('intern.project', string="Related Project")

    @api.model
    def create(self, vals):
        assignments = self.env['intern.project'].browse(vals['project_id']).assignment_ids
        for assign in assignments:
            self.env['intern.assignment.status'].create({
                'assignment_id': assign.id,
                'intern_id': vals.get('intern_id'),
            })
        return super().create(vals)
    
    @api.depends()
    def _compute_completion_percentage(self):
        for proj in self:
            assignments = set(self.env['intern.project'].browse(proj.project_id.id).assignment_ids.ids)
            completed_assignments = []
            print(proj.intern_id)
            for assign in self.env['intern.assignment.status'].search([('intern_id', '=', proj.intern_id.id), ('status', '=', 'completed')]):
                if assign.assignment_id.id in assignments:
                    completed_assignments.append(assign.assignment_id)
            total_assignments = len(assignments)
            proj.completion_percentage = 100 * len(completed_assignments) / total_assignments if total_assignments > 0 else 0

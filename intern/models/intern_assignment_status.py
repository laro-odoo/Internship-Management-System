from odoo import fields, models

class InternAssignmentStatus(models.Model):
    _name = 'intern.assignment.status'
    _description = 'Intern Assignment Status'
    
    # Fields
    name = fields.Char('Title', related='assignment_id.name', required=True)
    status = fields.Selection([
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='assigned')
    start_date = fields.Date(default=lambda self: self.assignment_id.start_date if self.assignment_id else fields.Date.today(), required=True)
    end_date = fields.Date(default=lambda self: self.assignment_id.start_date if self.assignment_id else False)
    feedback = fields.Text()
    project_name = fields.Char(related='assignment_id.project_id.name')
    marks_obtained = fields.Float(default=0, required=True)
    maximum_marks = fields.Float(related='assignment_id.maximum_marks')

    _sql_constraints = [
        ('start_date_check', 'CHECK(start_date <= end_date)', 'Start date must be before end date'),
        ('marks_check', 'CHECK(marks_obtained <= maximum_marks)', 'Marks obtained must be less than or equal to maximum marks'),
    ]

    # Relations
    assignment_id = fields.Many2one('intern.assignment', string='Assignments', required=True)
    intern_id = fields.Many2one('intern.profile', string='Intern')

    def action_description(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Description',
            'res_model': 'intern.assignment',
            'view_mode': 'form',
            'res_id': self.assignment_id.id
        }

from odoo import fields, models, api

class InternProfile(models.Model):
    _name = 'intern.profile'
    _description = 'Intern Profile'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Fields
    name = fields.Char(required=True, tracking=True)
    email = fields.Char(tracking=True)
    phone_number = fields.Char(tracking=True)
    start_date = fields.Date(default=fields.Date.today(), required=True, tracking=True)
    end_date = fields.Date(tracking=True)
    performance_evaluation = fields.Text(tracking=True)
    internship_status = fields.Selection([
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('declined', 'Declined')
    ],tracking=True)

    # Relations
    mentor_id = fields.Many2one('intern.mentor.profile', string='Mentor', tracking=True)  #TODO conenct mentor and project to the profile
    department_id = fields.Many2one('intern.department', string="Department", tracking=True)
    skill_ids = fields.Many2many('intern.skill', tracking=True) #TODO add a tags like feature for the skills and also we can make a seperate module for the skills where we can get the ratings and all
    skill_rating_ids = fields.One2many('intern.skill.rating', 'intern_id', string="Skills", tracking=True)
    project_status_ids = fields.One2many('intern.project.status', 'intern_id', string="Project Status", tracking=True)
    assignment_status_ids = fields.One2many('intern.assignment.status', 'intern_id', string="Assignments", tracking=True)
    report_ids = fields.One2many('intern.report', 'intern_id', string="Reports", tracking=True)

    @api.depends('mentor_id')
    def remove_mentor(self):
        self.mentor_id = False

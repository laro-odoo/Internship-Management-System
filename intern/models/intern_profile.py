from odoo import fields, models, api

class InternProfile(models.Model):
    _name = 'intern.profile'
    _description = 'Intern Profile'

    # Fields
    name = fields.Char(required=True)
    email = fields.Char()
    phone_number = fields.Char()
    start_date = fields.Date(default=fields.Date.today(), required=True)
    end_date = fields.Date()
    performance_evaluation = fields.Text()
    internship_status = fields.Selection([
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('declined', 'Declined')
    ],)

    # Relations
    mentor_id = fields.Many2one('intern.mentor.profile', string='Mentor')  #TODO conenct mentor and project to the profile
    department_id = fields.Many2one('intern.department', string="Department")
    skill_ids = fields.Many2many('intern.skill') #TODO add a tags like feature for the skills and also we can make a seperate module for the skills where we can get the ratings and all
    skill_rating_ids = fields.One2many('intern.skill.rating', 'intern_id', string="Skills")
    project_status_ids = fields.One2many('intern.project.status', 'intern_id', string="Project Status")
    assignment_status_ids = fields.One2many('intern.assignment.status', 'intern_id', string="Assignments")
    report_ids = fields.One2many('intern.report', 'intern_id', string="Reports")

    @api.depends('mentor_id')
    def remove_mentor(self):
        self.mentor_id = False

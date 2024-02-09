from odoo import fields, models

class InternProfile(models.Model):
    _name = 'intern.profile'
    _description = 'Intern Profile'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    email = fields.Char(required=True)
    phone_number = fields.Char(required=True)
    skills = fields.Text() #TODO add a tags like feature for the skills and also we can make a seperate module for the skills where we can get the ratings and all
    start_date = fields.Date(default=fields.Date.today(), required=True)
    end_date = fields.Date()
    performance_evaluation = fields.Text()
    # mentor_id = fields.Many2one('intern.mentor', string='Mentor')  #TODO conenct mentor and project to the profile
    # project_id = fields.Many2one('intern.project', string='Project')
    
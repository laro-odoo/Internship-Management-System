from odoo import fields, models, api

class InternSkill(models.Model):
    _name = 'intern.skill'
    _description = 'Intern Skills'

    # Fields
    name = fields.Char(required=True)
    description = fields.Text()

    # Relations
    skill_rating_ids = fields.One2many('intern.skill.rating', 'skill_id', string="Ratings")

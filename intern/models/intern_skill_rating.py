from odoo import fields, models, api

class InternSkillRating(models.Model):
    _name = 'intern.skill.rating'
    _description = 'Intern Skill Rating'

    # Fields
    name = fields.Char(related='skill_id.name', string='Skill Name')
    rating_star = fields.Selection([('0', '✩'), ('1', '★'), ('2', '★★'), ('3', '★★★'), ('4', '★★★★'), ('5', '★★★★★')], string='Rating (Display)', default=0)

    # Relations
    intern_id = fields.Many2one('intern.profile', string='Intern')
    skill_id = fields.Many2one('intern.skill', string='Skill')

    @api.model
    def create(self, vals):
        rating_record = super(InternSkillRating, self).create(vals)

        # Update intern.profile.skill_ids with skill_id if intern_id is present
        if rating_record.intern_id:
            rating_record.intern_id.skill_ids |= rating_record.skill_id

        return rating_record

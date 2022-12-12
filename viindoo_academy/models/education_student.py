from odoo import models, fields, api


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = ' Education Student'
    
    name = fields.Char(
        string='Name',
        required=True)
    class_id = fields.Many2one(
        comodel_name='education.class',
        string='Class', help="The Class of student")
    
    
    class_ids = fields.Many2many(
        comodel_name='education.class',
        relation='class_education_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes')

    country_ids = fields.Many2many('res.country',string="Country")
    country_ids_2=fields.Char(related='ethnic_ids.name', store=True)
    
    ethnic_ids = fields.Many2many('education.student.ethnic','ethnic_ids')
    user_id = fields.Many2one(comodel_name = 'res.users', string = 'User') 
    
    @api.onchange('ethnic_ids')
    def _onchange_country(self):
        if self.ethnic_ids:
            self.country_ids = self.ethnic_ids.country_ids
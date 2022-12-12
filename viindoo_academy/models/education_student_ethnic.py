from odoo import models,fields
    
class EducationStudentEthnic(models.Model):
    _name = 'education.student.ethnic'
    _description= 'Student Ethnic'
    
    name = fields.Char(string='Name')
    country_ids = fields.Many2many('res.country',string="Country")
    description = fields.Html()
    student_ids = fields.Many2many('education.student','ethnic_ids')
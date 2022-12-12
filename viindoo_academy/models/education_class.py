from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'
    
    name = fields.Char(
        string='Name',
        help="The name of the class for identification",
        required=True)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
            ],
        string='Status',
        default='draft',
        help="Status of the class",
        )
    description = fields.Text(
        string='Description',
        help="The description for identification.")
    active = fields.Boolean(default=True)
    
    start_date = fields.Date(
        string='Start Date',
        help="The date from of class",
                            )

    end_date = fields.Date(
        string='End Date',
        help="The date of class",
                            )    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_id',
        string='Students',
        help="The students that belong to the class.")
    
    historical_student_ids = fields.Many2many(
        comodel_name='education.student',
        relation='class_education_rel',
        column1='class_id',
        column2='student_id',
        string="Historical Students")

    student_count = fields.Integer(string='Number of students', compute='_compute_student_count')
    
    historical_student_count = fields.Integer(string='Number of historical students', onchange='_onchange_historical_student_count')
    
    responsible_id = fields.Many2one(comodel_name='education.student', string='Responsible user', default = lambda self: self.env.user)
    
    @api.onchange('historical_student_ids')
    def _onchange_historical_student_count(self):
        for i in self:
            i.historical_student_count = len(i.historical_student_ids)

    @api.depends('student_ids')
    def _compute_student_count(self):
        for r in self:
            r.student_count = len(r.student_ids)
            
    @api.constrains('start_date','end_date')
    def _check_date(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("The start date of the class must be earlier than or equal to the end date.")
        
    _sql_constraints = [('class_name_unique', 'unique(name)', "The class name must be unique in the company!")]
 

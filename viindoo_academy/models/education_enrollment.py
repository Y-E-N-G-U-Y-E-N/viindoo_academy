from odoo import models, fields, api, _
from odoo.exceptions import UserError


class EducationEnrollment(models.Model):
    _name = 'education.enrollment'
    _description = 'Education Enrollment'
    # _order = 'id DESC'
    
    name = fields.Char(
        string='Ref.',
        required=True
        )

    class_id = fields.Many2one('education.class', string='Class')
    student_id = fields.Many2one('education.student', string='Student')
    date = fields.Date(help="The date on which the student enrolls")

    @api.constrains('class_id', 'student_id')
    def _check_class_vs_student(self):
        for r in self:
            if r.class_id.state != 'confirmed':
                raise UserError(
                    _("You may not be able to enroll a student into the class %s whose status is not Confirmed.")
                     % r.class_id.name
                     )

            if r.student_id and r.class_id and r.class_id.state != 'cancelled': 
                overlap = self.search(
                    domain=[
                        ('id', '!=', r.id),
                        ('student_id', '=', r.student_id.id),
                        ('class_id', '=', r.class_id.id),
                        ('class_id.state', '!=', 'cancelled'),
                        ],
                    limit=1,
                    )
                if overlap:
                    raise UserError(
                        _("You may not be able to enroll the student %s into the class %s twice.")
                        % (r.student_id.name, r.class_id.name)
                        )

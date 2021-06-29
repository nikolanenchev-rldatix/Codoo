from odoo import fields, models, _, api


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student Table"

    name = fields.Char(string="Name")
    surname = fields.Char(string="Surname")
    email = fields.Char(string="Email")
    enrolledYear = fields.Char(string="Enrolled Year")
    birthdate = fields.Char(string="BirthDate")
    grade = fields.Char(string="Grade of the student", default="5")
    field = fields.Char(string="Field of study")
    index = fields.Char(string='Index of student', required=True, copy=False,
                        readonly=True, index=True, default=lambda self: _('New'))
    courses_ids = fields.Many2many('school.course', 'student_course_rel',
                                   'student_ids', 'courses_ids', string='Courses')

    def student_report(self):
        return self.env.ref('om_school.report_students').report_action(self)

    @api.model
    def create(self, vals):
        if vals.get('index', _('New')) == _('New'):
            vals['index'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        result = super(SchoolStudent, self).create(vals)
        return result

from odoo import fields, models


class SchoolStudent(models.Model):
    _name = "school.teacher"
    _description = "Teacher Table"

    name = fields.Char(string="Name")
    surname = fields.Char(string="Surname")
    email = fields.Char(string="Email")
    course_ids = fields.Many2many('school.course', 'teacher_course_rel',
                            'teacher_ids', 'course_ids', string='Courses')
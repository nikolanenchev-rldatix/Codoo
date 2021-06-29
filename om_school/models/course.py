from odoo import fields, models, api


class SchoolCourse(models.Model):
    _name = "school.course"
    _description = "Course Table"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    Cname = fields.Char(string="Course Name", readonly=True, tracking=True,
                        states={
                            'draft': [('readonly', False)]})
    field = fields.Char(string="Field of study for course", readonly=True,
                        states={
                            'draft': [('readonly', False)]
                        })
    semester = fields.Selection([('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth'),
                                 ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eight', 'Eight')],
                                default='First', readonly=True, tracking=True,
                                states={
                                    'draft': [('readonly', False)]
                                })
    description = fields.Char(string="Description of course", readonly=True, tracking=True,
                              states={
                                  'draft': [('readonly', False)]
                              })
    bdate = fields.Char(string="Beginning date", readonly=True, tracking=True,
                        states={
                            'draft': [('readonly', False)]
                        })
    edate = fields.Char(string="Ending date", readonly=True, tracking=True,
                        states={
                            'draft': [('readonly', False)]
                        })
    documents = fields.Binary(string="Documents", help="This is documents upload option")
    document_name = fields.Char(string="File Name")
    student_ids = fields.Many2many('school.student', 'student_course_rel',
                                   'courses_ids', 'student_ids', string='Students', readonly=False,
                                   copy=False)
    teacher_ids = fields.Many2many('school.teacher', 'teacher_course_rel',
                                   'course_ids', 'teacher_ids', string='Teachers')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('finished', 'Finished')], string='Status', readonly=True, default='draft')

    def action_open(self):
        for rec in self:
            rec.state = 'open'

    def action_finished(self):
        for rec in self:
            rec.state = 'finished'

    def print_report(self):
        return self.env.ref('om_school.report_courses').report_action(self)

    @api.returns('self', lambda value: value, id)
    def copy(self, default=False):
        rtn = super(SchoolCourse, self).copy(default=default)
        return rtn

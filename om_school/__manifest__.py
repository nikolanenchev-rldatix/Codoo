{
    'name': 'School Management',
    'version': '13.0.1.0.0',
    'summary': 'School Management Software',
    'description': '***Module to Manage School***',
    'category': 'Extra Tools',
    'author': 'Nikola',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/courses.xml',
        'views/teacher.xml',
        'data/sequence.xml',
        'views/student.xml',
        'reports/report.xml',
        'reports/course_card.xml',
        'reports/student_card.xml'
    ],
    'demo': [''],
    'installable': True,
    'auto_install': False,
    'application' : True

}
{
    'name': "Camp Scheduler",
    'summary': "Manage camps and attendance",
    'author': "Preston Duffield, Sam Reed - Assemble Inc",
    'website': "https://www.assembleinc.com/",
    'category': 'Uncategorized',
    'version': '14.0.11',
    'depends': ['base', 'stock', 'sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/location.xml',
        'views/camp.xml',
        'views/attendee.xml'
    ],
    'demo': ['demo.xml'],
}

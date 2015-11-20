"""
Configuration for a project.
"""


rails = {

    'models': {
        'engine': 'sqlalchemy',
        'db': {
            'type': 'postgres',
            'user': 'rails',
            'password': 'rails',
        }
    },

    'views.engine': 'jinja',

}

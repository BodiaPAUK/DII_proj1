input_lvs = [
    {
        'X': (0, 26, 1),
        'name': 'Java skills',
        'terms': {
            'Beginner': ('trapmf', 0, 0, 15, 18),
            'Intermediate': ('trapmf', 17, 20, 22, 24),
            'Advanced': ('trapmf', 20, 23, 25, 26),
        }
    },

    {
        'X': (0, 61, 1),
        'name': 'English level',
        'terms': {
            'Beginner': ('trapmf', 0, 0, 25, 30),
            'Intermediate': ('trapmf', 27, 35, 45, 53),
            'Advanced': ('trapmf', 51, 55, 61, 61),
        }
    },

    {
        'X': (0, 51, 1),
        'name': 'Soft skills',
        'terms': {
            'Beginner': ('trapmf', 0, 0, 20, 30),
            'Intermediate': ('trapmf', 25, 33, 40, 45),
            'Advanced': ('trapmf', 37, 43, 51, 51),
        }
    },
]

output_lv = {
    'X': (0, 1, 0.01),
    'name': 'Junior Java skill level',
    'terms': {
        'none to very little': ('trapmf', 0, 0, 0.05, 0.1),
        'very low': ('trimf', 0, 0.2, 0.3),
        'low': ('trapmf', 0.2, 0.3, 0.4, 0.5),
        'medium': ('trimf', 0.4, 0.5, 0.6),
        'above medium': ('trimf', 0.5, 0.6, 0.7),
        'high': ('trapmf', 0.6, 0.7, 0.8, 0.9),
        'extremely high': ('trapmf', 0.7, 0.9, 1, 1),
    }
}


rule_base = [
    (('Beginner', 'Beginner', 'Beginner'), 'none to very little'),
    (('Beginner', 'Beginner', 'Intermediate'), 'very low'),
    (('Beginner', 'Beginner', 'Advanced'), 'very low'),
    (('Beginner', 'Intermediate', 'Beginner'), 'very low'),
    (('Beginner', 'Intermediate', 'Intermediate'), 'low'),
    (('Beginner', 'Intermediate', 'Advanced'), 'medium'),
    (('Beginner', 'Advanced', 'Beginner'), 'very low'),
    (('Beginner', 'Advanced', 'Intermediate'), 'low'),
    (('Beginner', 'Advanced', 'Advanced'), 'above medium'),
    (('Intermediate', 'Beginner', 'Beginner'), 'very low'),
    (('Intermediate', 'Beginner', 'Intermediate'), 'low'),
    (('Intermediate', 'Beginner', 'Advanced'), 'medium'),
    (('Intermediate', 'Intermediate', 'Beginner'), 'medium'),
    (('Intermediate', 'Intermediate', 'Intermediate'), 'medium'),
    (('Intermediate', 'Intermediate', 'Advanced'), 'above medium'),
    (('Intermediate', 'Advanced', 'Beginner'), 'medium'),
    (('Intermediate', 'Advanced', 'Intermediate'), 'above medium'),
    (('Intermediate', 'Advanced', 'Advanced'), 'high'),
    (('Advanced', 'Beginner', 'Beginner'), 'very low'),
    (('Advanced', 'Beginner', 'Intermediate'), 'medium'),
    (('Advanced', 'Beginner', 'Advanced'), 'above medium'),
    (('Advanced', 'Intermediate', 'Beginner'), 'medium'),
    (('Advanced', 'Intermediate', 'Intermediate'), 'above medium'),
    (('Advanced', 'Intermediate', 'Advanced'), 'high'),
    (('Advanced', 'Advanced', 'Beginner'), 'above medium'),
    (('Advanced', 'Advanced', 'Intermediate'), 'high'),
    (('Advanced', 'Advanced', 'Advanced'), 'extremely high'),
]
import stringdist
import random
from random import randint
from datetime import datetime

# Mockup of a CRM database
contacts = [
    {
        'surname': 'Smith',
        'company': 'iLegal',
        'pastCases': [
            'Sharman Networks Ltd v Universal Music Australia Pty Ltd [2006] FCA 1 (5 January 2006)',
            'Handberg, in the matter of Greight Pty Ltd (in liq) [2006] FCA 17 (25 January 2006)'
        ],
        'interests': [
            'Golf', 'Cars'
        ],
        'leeds': [

        ],
        'remarks': [
            'Married in 2011',
            'Child in 2016',
            'Co-Founder of InCe'
        ]
    },
    {
        'surname': 'Doe',
        'company': 'we.cool',
        'pastCases': [
            'NBAN v Minister for Immigration and Multicultural Affairs [2006] FCA 57 (8 February 2006)'
        ],
        'interests': [
        ],
        'leeds': [
        ],
        'remarks': [
            'Chairman of ACM SenSys',
            'Prefers Italian Food'
        ]
    },
]

def getContactDetails(name):
    random.seed(datetime.now())
    File = open('./firstnames.txt')
    firstnames = File.read()
    namesDistance = [];
    for firstname in firstnames.splitlines():
        namesDistance.append((stringdist.levenshtein(firstname, name), firstname ))

    contact = contacts[randint(0,42000) % len(contacts)]

    contact['firstname'] = sorted(namesDistance)[0][1]

    return contact

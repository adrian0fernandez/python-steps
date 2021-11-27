from typing import Dict, List, Tuple

def tipado_estricto():
    positives: List[int] = [1,2,3,4,5]

    users: Dict[str, int] = {
        'argentina': 1,
        'mexico': 34,
        'colombia':45,
    }

    countries: List[Dict[str, str]] = [
        {
            'name': 'Argentina',
            'people': '4500000'
        },
        {
            'name': 'México',
            'people': '9000000'
        },
        {
            'name': 'Colombia',
            'people': '999999999',
        },
    ]
tipado_estricto()

def tipado_tuplas():
    numbers: Tuple[int, float, int] = (1, 0.5, 1)
tipado_tuplas()

def tipado_coordenas():
    coordinatesType = List[Dict[str, Tuple[int, int]]]

    coordinates: coordinatesType = [
        {
            'coord1': (1,2),
            'coord2': (3,5)
        },
        {
            'coord1': (0,1),
            'coord2': (2,5)
        },
    ]
tipado_coordenas()
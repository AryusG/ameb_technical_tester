class CelloGrade3Generator:
    def __init__(self) -> None:
        self.name = "Cello Grade 3 Generator"
        self.scales = self.get_scales()
        self.arpeggios = self.get_arpeggios()
        self.chromatic_scales = self.get_chromatic_scales()
        self.technical_exercises = self.get_technical_exercises()


    def get_scales(self) -> dict:
        return {
            'scales': [
                "C Harmonic Minor",
                "C Melodic Minor",
                "Eb Major",
                "F Major",
            ],
            'bowing_patterns': [
                'Spiccato',
                'Hook Stroke',
                'Two Crotchets Slurred Followed By Two Seperate Crotchets'
            ],
            'range': "2 Octaves"
        }


    def get_arpeggios(self) -> dict:
        return {
            'arpeggios': [
                "C Minor",
                "Eb Major",
                "F Major"
            ],
            'bowing_patterns': [
                'Detache with Cresc. and Desc.',
                'Three Note Slurred'
            ],
            'range': "2 Octaves"
        }


    def get_chromatic_scales(self) -> dict:
        return {
            'chromatics': [
                'C Chromatic',
                'Eb Chromatic'
            ],
            'range': '2 Octaves'
        }


    def get_technical_exercises(self) -> list:
        return [
            'Exercise 3.1: Swinging',
            'Exercise 3.2: Rope Ladder',
            'Exercise 3.3: Moving Up to Tenor Clef',
            'Exercise 3.4: Courtly Dance'
        ]
    


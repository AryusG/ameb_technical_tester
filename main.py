import random
from resources.cello.grade_3.CelloGrade3Generator import CelloGrade3Generator

generator = CelloGrade3Generator()

# Scale - Range - Bowing Pattern
# Technical Exercises []
print('\n')
print("-----------------------------------------------")
print(f"You are now using the {generator.name}")
print("-----------------------------------------------")
print()
print("\nPress Enter For Next or ('q' then Enter to quit)\n")

while True:
    probability = random.choice(range(1, 10))    

    if probability > 5:
        scale = random.choice(generator.scales['scales'])
        s_range = generator.scales['range']
        bowing_pattern = random.choice(generator.scales['bowing_patterns'])

        print(f"     -> {scale} ({s_range}) [{bowing_pattern}]")

    elif probability > 3:
        arpeggio = random.choice(generator.arpeggios['arpeggios'])
        a_range = generator.arpeggios['range']
        bowing_pattern = random.choice(generator.arpeggios['bowing_patterns'])

        print(f"     -> {arpeggio} Arpeggio ({a_range}) [{bowing_pattern}]")

    elif probability > 1:
        chromatic_s = random.choice(generator.chromatic_scales['chromatics'])
        chromatic_range = generator.chromatic_scales['range']

        print(f'     -> {chromatic_s} ({chromatic_range})')

    else:
        exercise = random.choice(generator.technical_exercises)
        print(f'     -> {exercise}')

    user_i = input()

    if user_i == 'q':
        break

    print()
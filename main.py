import file_operations
from faker import Faker
import random
import os


RUNE_DICT = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}




def main():   
    all_skills = [
        "стремительный прыжок", 
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд"
    ]

    
    
    runic_skill = []
    for i in all_skills:
        runic_version = i
        for letter, rune in RUNE_DICT.items():
            runic_version = runic_version.replace(letter, rune)
            runic_version = runic_version.replace(letter.upper(),rune)
        runic_skill.append(runic_version)
        
    all_skills = runic_skill

    for l in range(10):
        random_skills=random.sample(all_skills, 3)

        
        skill_first = random_skills[0]
        skill_second = random_skills[1]
        skill_third = random_skills[2]

        
        strength=random.randint(3, 18)
        agility=random.randint(3, 18)
        endurance=random.randint(3, 18)
        intelligence=random.randint(3, 18)
        luck=random.randint(3, 18)


        fake_first_name=Faker("ru_RU")
        fake_last_name=Faker("ru_RU")
        fake_job=Faker("ru_RU")
        fake_city=Faker("ru_RU")

        
        context = {
            "first_name": fake_first_name.first_name(),
            "last_name": fake_last_name.last_name(),
            "job": fake_job.job(),
            "town": fake_city.city(),
            "strength": strength,
            "agility": agility,
            "endurance": endurance,
            "intelligence": intelligence,
            "luck": luck,
            "skill_1": skill_first,
            "skill_2": skill_second,
            "skill_3": skill_third
        }


        
        output_filename = f"character_{l+1}.svg"
        output_path = "Character Cards/" + output_filename
        file_operations.render_template("charsheet.svg", output_path, context)


if __name__ == '__main__':
    main()









    
    
    

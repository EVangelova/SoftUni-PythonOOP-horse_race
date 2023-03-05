from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def find_horse(self, horse_type_):
        found_horse = next(
            filter(lambda x: (type(x).__name__ == horse_type_ and not x.is_taken), reversed(self.horses)),
            None
        )
        if not found_horse:
            raise Exception(f"Horse breed {horse_type_} could not be found!")
        return found_horse

    def find_jockey(self, jockey_name_):
        found_jockey = next(filter(lambda x: x.name == jockey_name_, self.jockeys), None)
        if not found_jockey:
            raise Exception(f"Jockey {jockey_name_} could not be found!")
        return found_jockey

    def find_horse_race(self, race_type_):
        found_race = next(filter(lambda x: x.race_type == race_type_, self.horse_races), None)
        if not found_race:
            raise Exception(f"Race {race_type_} could not be found!")
        return found_race

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        new_jockey = Jockey(jockey_name, age)
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        new_race_type = HorseRace(race_type)
        for race in self.horse_races:
            if race.type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(new_race_type)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        jockey = self.find_jockey(jockey_name)
        horse = self.find_horse(horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            jockey.horse = horse
            horse.is_taken = True
            return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        race = self.find_horse_race(race_type)
        jockey = self.find_jockey(jockey_name)
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'
        else:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):

        race = self.find_horse_race(race_type)
        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        the_fastest_jockey = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return f'The winner of the {race_type} race, with a speed of {the_fastest_jockey.horse.speed}km/h ' \
               f'is {the_fastest_jockey.name}! Winner\'s horse: {the_fastest_jockey.horse.name}.'


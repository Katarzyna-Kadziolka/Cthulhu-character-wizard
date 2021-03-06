from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.firearms import Firearm
from Enums.language import Language
from Enums.occupation import Occupation
from Enums.pilot import Pilot
from Enums.science import Science
from Enums.skill import Skill
from Enums.survival import Survival
from Enums.uncommon_skill import UncommonSkill


class Translator:
    skills = {
        Skill.ACCOUNTING: "Księgowość",
        Skill.ANTHROPOLOGY: "Antropologia",
        Skill.APPRAISE: "Wycena",
        Skill.ARCHAEOLOGY: "Archeologia",
        Skill.ART_CRAFT: "Sztuka/Rzemiosło",
        Skill.CHARM: "Urok Osobisty",
        Skill.CLIMB: "Wspinaczka",
        Skill.CREDIT_RATING: "Majętność",
        Skill.CTHULHU_MYTHOS: "Mity Cthulhu",
        Skill.DISGUISE: "Charakteryacja",
        Skill.DODGE: "Unik",
        Skill.DRIVE_AUTO: "Prowadzenie Samochodu",
        Skill.ELECTRICAL_REPAIR: "Elektryka",
        Skill.FAST_TALK: "Gadanina",
        Skill.FIGHTING: "Walka Wręcz",
        Skill.FIREARMS: "Broń Palna",
        Skill.FIRST_AID: "Pierwsza Pomoc",
        Skill.HISTORY: "Historia",
        Skill.INTIMIDATE: "Zastraszanie",
        Skill.JUMP: "Skakanie",
        Skill.OTHER_LANGUAGE: "Język Obcy",
        Skill.OWN_LANGUAGE: "Język Ojczysty",
        Skill.LAW: "Prawo",
        Skill.LIBRARY_USE: "Korzystanie z Bibliotek",
        Skill.LISTEN: "Nasłuchiwanie",
        Skill.LOCKSMITH: "Ślusarstwo",
        Skill.MECHANICAL_REPAIR: "Mechanika",
        Skill.MEDICINE: "Medycyna",
        Skill.NATURAL_WORLD: "Wiedza o Naturze",
        Skill.NAVIGATE: "Nawigacja",
        Skill.OCCULT: "Okultyzm",
        Skill.OPERATE_HEAVY_MACHINERY: "Obsługa Ciężkiego Sprzętu",
        Skill.PERSUADE: "Perswazja",
        Skill.PILOT: "Pilotowanie",
        Skill.PSYCHOLOGY: "Psychologia",
        Skill.PSYCHOANALYSIS: "Psychoanaliza",
        Skill.RIDE: "Jeździectwo",
        Skill.SCIENCE: "Nauka",
        Skill.SLEIGHT_OF_HAND: "Zręczne Palce",
        Skill.SPOT_HIDDEN: "Spostrzegawczość",
        Skill.STEALTH: "Ukrywanie",
        Skill.SURVIVAL: "Sztuka Przetrwania",
        Skill.SWIM: "Pływanie",
        Skill.THROW: "Rzucanie",
        Skill.TRACK: "Tropienie",
        Skill.DIVING: "Nurkowanie",
        Skill.UNCOMMON_SKILL: "Specjalna umiejętność"
    }

    languages = {
        Language.LATIN: "Język: Łacina",
        Language.SPANISH: "Język: Hiszpański",
        Language.GERMAN: "Język: Niemiecki",
        Language.FRENCH: "Język: Francuski",
        Language.ITALIAN: "Język: Włoski",
        Language.POLISH: "Język: Polski",
        Language.RUSSIAN: "Język: Rosyjski",
        Language.CHINESE: "Język: Chiński",
        Language.JAPANESE: "Język: Japoński",
        Language.TURKISH: "Język: Turecki"
    }

    arts_crafts = {
        ArtCraft.ACTING: "Sztuka/Rzemiosło: Aktorstwo",
        ArtCraft.BARBER: "Sztuka/Rzemiosło: Fryzjerstwo",
        ArtCraft.CARPENTRY: "Sztuka/Rzemiosło: Cieślarstwo",
        ArtCraft.COBBLER: "Sztuka/Rzemiosło: Szewctwo",
        ArtCraft.COOK: "Sztuka/Rzemiosło: Gotowanie",
        ArtCraft.DANCER: "Sztuka/Rzemiosło: Taniec",
        ArtCraft.FINE_ART: "Sztuka/Rzemiosło: Plastyka",
        ArtCraft.FORGERY: "Sztuka/Rzemiosło: Fałszerstwo",
        ArtCraft.PHOTOGRAPHY: "Sztuka/Rzemiosło: Fotografia",
        ArtCraft.OPERA_SINGER: "Sztuka/Rzemiosło: Śpiew operowy",
        ArtCraft.PAINTER: "Sztuka/Rzemiosło: Malarstwo",
        ArtCraft.POTTER: "Sztuka/Rzemiosło: Garncarstwo",
        ArtCraft.SCULPTOR: "Sztuka/Rzemiosło: Rzeźbiarstwo",
        ArtCraft.WOODWORK: "Sztuka/Rzemiosło: Stolarstwo",
        ArtCraft.TECHNICAL_DRAWING: "Sztuka/Rzemiosło: Rysunek techniczny",
        ArtCraft.FARMING: "Sztuka/Rzemiosło: Rolnictwo",
        ArtCraft.ART: "Sztuka/Rzemiosło: Sztuka",
        ArtCraft.WELDING: "Sztuka/Rzemiosło: Spawanie",
        ArtCraft.PLUMBING: "Sztuka/Rzemiosło: Hydraulika",
        ArtCraft.INSTRUMENT: "Sztuka/Rzemiosło: Gra na instrumencie",
        ArtCraft.TYPING: "Sztuka/Rzemiosło: Maszynopisanie",
        ArtCraft.SHORT_HAND: "Sztuka/Rzemiosło: Stenografia",
        ArtCraft.LITERATURE: "Sztuka/Rzemiosło: Literatura",
        ArtCraft.WRITER: "Sztuka/Rzemiosło: Pisarstwo"
    }

    fighting = {
        Fighting.AXE: "Walka: Siekiera",
        Fighting.BRAWL: "Walka: Walka na Pięści",
        Fighting.CHAINSAW: "Walka: Piła Łańcuchowa",
        Fighting.FLAIL: "Walka: Nunchako",
        Fighting.GARROTE: "Walka: Garota",
        Fighting.SPEAR: "Walka: Włócznia",
        Fighting.SWORD: "Walka: Miecz",
        Fighting.WHIP: "Walka: Bicz"
    }

    firearms = {
        Firearm.BOW: "Broń: Łuk",
        Firearm.FLAMETHROWER: "Broń: Miotacz ognia",
        Firearm.HANDGUN: "Broń: Pistolet",
        Firearm.RIFLE_SHOTGUN: "Broń: Karabin",
    }

    science = {
        Science.ASTRONOMY: "Nauka: Astronomia",
        Science.BIOLOGY: "Nauka: Biologia",
        Science.BOTANY: "Nauka: Botanika",
        Science.CHEMISTRY: "Nauka: Chemia",
        Science.CRYPTOGRAPHY: "Nauka: Kryptografia",
        Science.ENGINEERING: "Nauka: Inżynieria",
        Science.FORENSICS: "Nauka: Kryminalistyka",
        Science.GEOLOGY: "Nauka: Geologia",
        Science.MATHEMATICS: "Nauka: Matematyka",
        Science.METEOROLOGY: "Nauka: Meteorologia",
        Science.PHARMACY: "Nauka: Farmacja",
        Science.PHYSICS: "Nauka: Fizyka",
        Science.ZOOLOGY: "Nauka: Zoologia"
    }

    uncommon_skills = {
        UncommonSkill.ANIMAL_HANDLING: "Tresura Zwierząt",
        UncommonSkill.ARTILLERY: "Artyleria",
        UncommonSkill.DEMOLITIONS: "Wyburzenia",
        UncommonSkill.HYPNOSIS: "Hipnoza",
        UncommonSkill.READ_LIPS: "Czytanie z Ruchu Warg"
    }

    occupations = {
        Occupation.ACCOUNTANT: "Księgowy",
        Occupation.ACROBAT: "Akrobata",
        Occupation.STAGE_ACTOR: "Aktor scenowy",
        Occupation.FILM_STAR: "Gwiazda filmowa",
        Occupation.AGENCY_DETECTIVE: "Detektyw z agencji",
        Occupation.ALIENIST: "Alienista",
        Occupation.ANIMAL_TRAINER: "Trener zwierząt",
        Occupation.ANTIQUARIAN: "Antykwariusz",
        Occupation.ANTIQUE_DEALER: "Sprzedawca antyków",
        Occupation.ARCHAEOLOGIST: "Archeolog ",
        Occupation.ARCHITECT: "Architekt",
        Occupation.ARTIST: "Artysta",
        Occupation.ASSASSIN: "Zabójca ",
        Occupation.ASYLUM_ATTENDANT: "Pacjent szpitala psychiatrycznego",
        Occupation.ATHLETE: "Atleta",
        Occupation.AUTHOR: "Pisarz",
        Occupation.AVIATOR: "Lotnik",
        Occupation.BANK_ROBBER: "Kasiarz",
        Occupation.BARTENDER: "Barman",
        Occupation.BIG_GAME_HUNTER: "Myśliwy",
        Occupation.BOOK_DEALER: "Księgarz",
        Occupation.BOOTLEGGER: "Przemytnik",
        Occupation.BOUNTY_HUNTER: "Łowca nagród",
        Occupation.BOXER: "Bokser",
        Occupation.BURGLAR: "Włamywacz ",
        Occupation.BUTLER_MAID: "Lokaj/Pokojówka",
        Occupation.CHAUFFEUR: "Szofer",
        Occupation.CLERGY: "Kleryk",
        Occupation.CONMAN: "Oszust",
        Occupation.COWBOY: "Kowboj",
        Occupation.CRAFTSPERSON: "Rzemieślnik",
        Occupation.CRIMINAL: "Przestępca ",
        Occupation.CULT_LEADER: "Przywódca kultu",
        Occupation.DESIGNER: "Projektant",
        Occupation.DILETTANTE: "Dziedzic",
        Occupation.DIVER: "Nurek",
        Occupation. DOCTOR_OF_MEDICINE: "Doktor medycyny",
        Occupation.DRIFTER: "Włóczykij",
        Occupation.DRIVER: "Kierowca",
        Occupation.EDITOR: "Redaktor",
        Occupation.ELECTED_OFFICIAL: "Urzędnik",
        Occupation.ENGINEER: "Inżynier",
        Occupation.ENTERTAINER: "Artysta sceniczny",
        Occupation.EXPLORER: "Odkrywca",
        Occupation.FARMER: "Rolnik",
        Occupation.FEDERAL_AGENT: "Agent federalny",
        Occupation.FENCE: "Paser",
        Occupation.FIREFIGHTER: "Strażak",
        Occupation.FOREIGN_CORESPONDENT: "Korespondent zagraniczny",
        Occupation.FORENSIC_SURGEON: "Patolog sądowy",
        Occupation.FORGER: "Fałszerz",
        Occupation.GAMBLER: "Hazardzista",
        Occupation.GANGSTER_BOSS: "Mafiozo",
        Occupation.GANGSTER_UNDERLING: "Członek mafii",
        Occupation.GENTLEMAN_LADY: "Dżentelmen/Dama",
        Occupation.GUN_MOLL: "Dziewczyna gangstera",
        Occupation.HOBO: "Bezdomny",
        Occupation.HOSPITAL_ORDERLY: "Pracownik szpitala",
        Occupation.INVESTIGATIVE_JOURNALIST: "Dziennikarz śledczy",
        Occupation.JUDGE: "Sędzia",
        Occupation.LABORATORY_ASSISTANT: "Laborant",
        Occupation.LABORER: "Robotnik",
        Occupation.LAWYER: "Prawnik",
        Occupation.LIBRARIAN: "Bibliotekarz ",
        Occupation.LUMBERJACK: "Drwal",
        Occupation.MECHANIC:"Mechanik ",
        Occupation.MILITARY_OFFICER: "Oficer Wojskowy",
        Occupation.MINER: "Górnik ",
        Occupation.MISSIONARY: "Misjonarz",
        Occupation.MOUNTAIN_CLIMBER: "Wspinacz górski",
        Occupation.MUSEUM_CURATOR: "Kurator Muzeum",
        Occupation.MUSICIAN: "Muzyk",
        Occupation.NURSE: "Pielęgniarka",
        Occupation.OCCULTIST: "Okultysta",
        Occupation.OUTDOORSMAN: "Traper",
        Occupation.PARAPSYCHOLOGIST: "Parapsycholog",
        Occupation.PHARMACIST: "Farmaceuta",
        Occupation.PHOTOGRAPHER: "Fotograf",
        Occupation.PHOTOJOURNALIST: "Fotoreporter ",
        Occupation.PILOT: "Pilot ",
        Occupation.POLICE_DETECTIVE_OFFICER: "Detektyw policyjny/oficer",
        Occupation.UNIFORMED_POLICE_OFFICER: "Policjant",
        Occupation.PRIVATE_INVESTIGATOR: "Prywatny detektyw",
        Occupation.PROFESSOR: "Profesor ",
        Occupation.PROSPECTOR: "Poszukiwacz złota",
        Occupation.PROSTITUTE: "Prostytutka",
        Occupation.PSYCHIATRIST: "Psychiatra",
        Occupation.PSYCHOLOGIST_PSYCHOANALYST: "Psycholog/psychoanalityk",
        Occupation.REPORTER: "Reporter ",
        Occupation.RESEARCHER: "Badacz",
        Occupation.SAILOR_NAVAL: "Marynarz wojskowy",
        Occupation.SAILOR_COMMERCIAL: "Marynarz",
        Occupation.SALESPERSON: "Sprzedawca",
        Occupation.SCIENTIST: "Naukowiec",
        Occupation.SECRETARY: "Sekretarka",
        Occupation.SHOPKEEPER: "Właściciel sklepu",
        Occupation.SMUGGLER: "Szmugler ",
        Occupation.SOLDIER: "Żołnierz",
        Occupation.SPY: "Szpieg",
        Occupation.STREET_PUNK: "Drab",
        Occupation.STUDENT_INTERN: "Student/Stażysta",
        Occupation.STUNTMAN: "Kaskader",
        Occupation.TAXI_DRIVER: "Kierowca taksówki ",
        Occupation.TRIBE_MEMBER: "Członek Plemienia",
        Occupation.UNDERTAKER: "Grabarz",
        Occupation.UNION_ACTIVIST: "Aktywista",
        Occupation.WAITER: "Kelner",
        Occupation.WHITE_COLLAR_WORKER: "Pracownik biurowy",
        Occupation.MANAGER: "Manager",
        Occupation.ZEALOT: "Fanatyk",
        Occupation.ZOOKEEPER: "Pracownik zoo"
    }

    pilot = {
        Pilot.AIRCRAFT: "Pilotowanie: Samolot",
        Pilot.BOAT: "Pilotowanie: Łódź"
    }

    survival = {
        Survival.ALPINE: "Sztuka Przetrwania: Góry",
        Survival.DESERT: "Sztuka Przetrwania: Pustynie",
        Survival.FOREST: "Sztuka Przetrwania: Lasy",
        Survival.JUNGLE: "Sztuka Przetrwania: Dżungla",
        Survival.SEA: "Sztuka Przetrwania: Morze",
        Survival.ARCTIC: "Sztuka Przetrwania: Arktyka"
    }

    def get_translation_for_skill(self, enum):
        skill = "error"
        if type(enum) == Skill:
            skill = Translator.skills[enum]
        elif type(enum) == Language:
            skill = Translator.languages[enum]
        elif type(enum) == ArtCraft:
            skill = Translator.arts_crafts[enum]
        elif type(enum) == Fighting:
            skill = Translator.fighting[enum]
        elif type(enum) == Firearm:
            skill = Translator.firearms[enum]
        elif type(enum) == Science:
            skill = Translator.science[enum]
        elif type(enum) == UncommonSkill:
            skill = Translator.uncommon_skills[enum]
        elif type(enum) == Pilot:
            skill = Translator.pilot[enum]
        elif type(enum) == Survival:
            skill = Translator.survival[enum]
        elif type(enum) == Occupation:
            skill = Translator.occupations[enum]

        return skill

    def get_skill_for_translation(self, translation):

        for key, value in Translator.skills.items():
            if value == translation:
                return key

        for key, value in Translator.languages.items():
            if value == translation:
                return key

        for key, value in Translator.arts_crafts.items():
            if value == translation:
                return key

        for key, value in Translator.fighting.items():
            if value == translation:
                return key

        for key, value in Translator.firearms.items():
            if value == translation:
                return key

        for key, value in Translator.science.items():
            if value == translation:
                return key

        for key, value in Translator.uncommon_skills.items():
            if value == translation:
                return key

        for key, value in Translator.pilot.items():
            if value == translation:
                return key

        for key, value in Translator.survival.items():
            if value == translation:
                return key

        raise ValueError(f"{translation} not supported")




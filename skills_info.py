import random_calculator
from Enums.ability import Ability
from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.firearms import Firearm
from Enums.language import Language
from Enums.pilot import Pilot
from Enums.science import Science
from Enums.skill import Skill
from Enums.survival import Survival
from Enums.uncommon_skill import UncommonSkill
from data import Data


class SkillsInfo():
    skills_base_points = {
        Skill.ACCOUNTING: 5,
        Skill.ANTHROPOLOGY: 1,
        Skill.APPRAISE: 5,
        Skill.ARCHAEOLOGY: 1,
        Skill.ART_CRAFT: 5,
        Skill.CHARM: 15,
        Skill.CLIMB: 20,
        Skill.CREDIT_RATING: 0,
        Skill.CTHULHU_MYTHOS: 0,
        Skill.DISGUISE: 5,
        Skill.DODGE: "0.5 DEX",
        Skill.DRIVE_AUTO: 20,
        Skill.ELECTRICAL_REPAIR: 10,
        Skill.FAST_TALK: 5,
        Skill.FIGHTING: 25,
        Skill.FIREARMS: 20,
        Skill.FIRST_AID: 30,
        Skill.HISTORY: 5,
        Skill.INTIMIDATE: 15,
        Skill.JUMP: 20,
        Skill.OTHER_LANGUAGE: 1,
        Skill.OWN_LANGUAGE: "EDU",
        Skill.LAW: 5,
        Skill.LIBRARY_USE: 20,
        Skill.LISTEN: 20,
        Skill.LOCKSMITH: 1,
        Skill.MECHANICAL_REPAIR: 10,
        Skill.MEDICINE: 1,
        Skill.NATURAL_WORLD: 10,
        Skill.NAVIGATE: 10,
        Skill.OCCULT: 5,
        Skill.OPERATE_HEAVY_MACHINERY: 1,
        Skill.PERSUADE: 10,
        Skill.PILOT: 1,
        Skill.PSYCHOLOGY: 10,
        Skill.PSYCHOANALYSIS: 1,
        Skill.RIDE: 5,
        Skill.SCIENCE: 1,
        Skill.SLEIGHT_OF_HAND: 10,
        Skill.SPOT_HIDDEN: 25,
        Skill.STEALTH: 20,
        Skill.SURVIVAL: 10,
        Skill.SWIM: 20,
        Skill.THROW: 20,
        Skill.TRACK: 10,
        Skill.DIVING: 1,
        UncommonSkill.ANIMAL_HANDLING: 5,
        UncommonSkill.ARTILLERY: 1,
        UncommonSkill.DEMOLITIONS: 1,
        UncommonSkill.HYPNOSIS: 1,
        UncommonSkill.READ_LIPS: 1,
        Language.LATIN: 1,
        Language.SPANISH: 1,
        Language.GERMAN: 1,
        Language.FRENCH: 1,
        Language.ITALIAN: 1,
        Language.POLISH: 1,
        Language.RUSSIAN: 1,
        Language.CHINESE: 1,
        Language.JAPANESE: 1,
        Language.TURKISH: 1,
        ArtCraft.ACTING: 5,
        ArtCraft.BARBER: 5,
        ArtCraft.CARPENTRY: 5,
        ArtCraft.COBBLER: 5,
        ArtCraft.COOK: 5,
        ArtCraft.DANCER: 5,
        ArtCraft.FINE_ART: 5,
        ArtCraft.FORGERY: 5,
        ArtCraft.PHOTOGRAPHY: 5,
        ArtCraft.OPERA_SINGER: 5,
        ArtCraft.PAINTER: 5,
        ArtCraft.POTTER: 5,
        ArtCraft.SCULPTOR: 5,
        ArtCraft.WOODWORK: 5,
        ArtCraft.TECHNICAL_DRAWING: 5,
        ArtCraft.FARMING: 5,
        ArtCraft.ART: 5,
        ArtCraft.WELDING: 5,
        ArtCraft.PLUMBING: 5,
        ArtCraft.INSTRUMENT: 5,
        ArtCraft.TYPING: 5,
        ArtCraft.SHORT_HAND: 5,
        ArtCraft.LITERATURE: 5,
        ArtCraft.WRITER: 5,
        Fighting.AXE: 15,
        Fighting.BRAWL: 25,
        Fighting.CHAINSAW: 10,
        Fighting.FLAIL: 10,
        Fighting.GARROTE: 15,
        Fighting.SPEAR: 20,
        Fighting.SWORD: 20,
        Fighting.WHIP: 5,
        Firearm.BOW: 15,
        Firearm.FLAMETHROWER: 10,
        Firearm.HANDGUN: 20,
        Firearm.RIFLE_SHOTGUN: 25,
        Science.ASTRONOMY: 1,
        Science.BIOLOGY: 1,
        Science.BOTANY: 1,
        Science.CHEMISTRY: 1,
        Science.CRYPTOGRAPHY: 1,
        Science.ENGINEERING: 1,
        Science.FORENSICS: 1,
        Science.GEOLOGY: 1,
        Science.MATHEMATICS: 10,
        Science.METEOROLOGY: 1,
        Science.PHARMACY: 1,
        Science.PHYSICS: 1,
        Science.ZOOLOGY: 1,
        Pilot.AIRCRAFT: 1,
        Pilot.BOAT: 1,
        Survival.ALPINE: 10,
        Survival.DESERT: 10,
        Survival.FOREST: 10,
        Survival.JUNGLE: 10,
        Survival.SEA: 10,
        Survival.ARCTIC: 10
    }

    enums_dict = {
        "Uncommon Skill": UncommonSkill,
        "Other Language": Language,
        "Art/Craft": ArtCraft,
        "Fighting": Fighting,
        "Firearms": Firearm,
        "Science": Science,
        "Pilot": Pilot,
        "Survival": Survival
    }

    @staticmethod
    def get_all_skills_list():
        all_skills_list = [key for key, value in SkillsInfo.skills_base_points.items()]
        all_skills_list.remove(Skill.OTHER_LANGUAGE)
        all_skills_list.remove(Skill.ART_CRAFT)
        all_skills_list.remove(Skill.FIGHTING)
        all_skills_list.remove(Skill.FIREARMS)
        all_skills_list.remove(Skill.SCIENCE)
        all_skills_list.remove(Skill.PILOT)
        all_skills_list.remove(Skill.SURVIVAL)

        return all_skills_list

    @staticmethod
    def get_minimal_skill_points(skill) ->int:
        calculator = random_calculator.RandomCalculator()
        minimal_value = SkillsInfo.skills_base_points[skill]
        if minimal_value == "EDU":
            minimal_value = int(Data.data[Ability.EDUCATION])
        elif minimal_value == "0.5 DEX":
            minimal_value = calculator.half_value(Data.data[Ability.DEXTERITY])
        return minimal_value

    @staticmethod
    def extend_skill_list(big_skill_list):
        new_skill_list = []
        for skill_list in big_skill_list:
            if skill_list == []:
                continue
            skill_list_to_add = skill_list
            for skill in skill_list.copy():
                if skill == Skill.ART_CRAFT:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, ArtCraft, Skill.ART_CRAFT)
                elif skill == Skill.OTHER_LANGUAGE:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, Language, Skill.OTHER_LANGUAGE)
                elif skill == Skill.FIGHTING:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, Fighting, Skill.FIGHTING)
                elif skill == Skill.FIREARMS:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, Firearm, Skill.FIREARMS)
                elif skill == Skill.SCIENCE:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, Science, Skill.SCIENCE)
                elif skill == Skill.PILOT:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, Pilot, Skill.PILOT)
                elif skill == Skill.SURVIVAL:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, Survival, Skill.SURVIVAL)
                elif skill == Skill.UNCOMMON_SKILL:
                    skill_list_to_add = SkillsInfo.add_custom_skill(skill_list_to_add, UncommonSkill, Skill.UNCOMMON_SKILL)

            new_skill_list.append(skill_list_to_add)

        return new_skill_list

    @staticmethod
    def add_custom_skill(skill_list_to_add, enum_type, skill_type_enum):
        skill_list_to_add.extend([enum for skill, enum in enum_type.__members__.items()])
        skill_list_to_add.remove(skill_type_enum)
        return skill_list_to_add







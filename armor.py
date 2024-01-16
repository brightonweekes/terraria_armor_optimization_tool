class Armor:
    def __init__(self, name, defense, damage, crit, movement, melee_damage, melee_crit, melee_speed, ranged_damage, ranged_crit, 
                 magic_damage, magic_crit, mana, summon_damage, minion_slots, ability):
        self.name = name
        self.defense = defense
        self.damage = damage
        self.crit = crit
        self.movement = movement
        self.melee_damage = melee_damage
        self.melee_crit = melee_crit
        self.melee_speed = melee_speed
        self.ranged_damage = ranged_damage
        self.ranged_crit = ranged_crit
        self.magic_damage = magic_damage
        self.magic_crit = magic_crit
        self.mana = mana
        self.summon_damage = summon_damage
        self.minion_slots = minion_slots
        self.ability = ability     # As a string
        

# Game stages in order: Pre-Boss, Pre-Brain of Cthulhu/Eater of Worlds, Pre-Perforators/Hive Mind, Pre-Skeletron, Pre-Wall of Flesh
        
class CopperSet:
    helmet = Armor('Copper Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor('Copper Chainmail', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor('Copper Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor('', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'


class PlatinumSet:
    helmet = Armor('Platinum Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor('Platinum Chestplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor('Platinum Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor('', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'


class MoltenSet:
    helmet = Armor('Molten Helmet', 8, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor('Molten Breastplate', 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor('Molten Greaves', 8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor('', 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be set on fire')
    stage = 'Pre-Skeletron'


copper = CopperSet()
platinum = PlatinumSet()
molten = MoltenSet()

armor_sets = {copper, platinum, molten}

helmets = []
chestplates = []
leggings = []

for set in armor_sets:
    helmets.append(set.helmet)
    chestplates.append(set.chestplate)
    leggings.append(set.leggings)

# Better UI needed
# Calamity armor
# Rogue class
# Fix full set bonus output needed
# Code cleanup and better comments needed
# Full text based version with inputs needed

import tkinter

calamity = False

def toggle_calamity():
    global calamity
    calamity = not calamity


m=tkinter.Tk(className='Armor Optimization Tool')
w=tkinter.Button(m, option=toggle_calamity())
m.mainloop()

# Import necessary armor pieces, depending on whether Calamity mod is enabled or disabled

if calamity:
    from calamity_armor import armor_sets
else:
    from armor import armor_sets

# Set the target class and stats to maximize
target_stat = 'balance'
target_class = 'summoner' # input('Input target class [melee, ranged, magic, summoner]: ')

# Assign weight values to each stat based on target stat and target class
if target_stat == 'balance':
    defense_weight, damage_weight, crit_weight, movement_weight = 1, 1, 1, .1
    if target_class == 'melee':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 1, 1, 1, 0, 0, 0, 0, 0, 0, 0
    elif target_class == 'ranged':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 0, 0, 0, 1, 1, 0, 0, 0, 0, 0
    elif target_class == 'magic':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 0, 0, 0, 0, 0, 1, 1, .05, 0, 0
    elif target_class == 'summoner':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 0, 0, 0, 0, 0, 0, 0, 0, 1, 10

# Create the list which will contain all combinations of armor and their weighted score
combo_scores = []

# Loop through every combination and append to combo_scores along with weighted score
print('\nCalculating... Please wait\n')
for set in armor_sets:
    for set2 in armor_sets:
        for set3 in armor_sets:
            if hasattr(set, 'helmets') and hasattr(set2, 'chestplates') and hasattr(set3, 'leggings'):
                for helm in set.helmets:
                    for chest in set2.chestplates:
                        helmet_score, chestplate_score, leggings_score, set_bonus_score = 0, 0, 0, 0
                        if hasattr(set, 'helmets'):
                            helmet_score = (helm.defense*defense_weight + helm.damage*damage_weight + helm.crit*crit_weight + helm.movement*movement_weight + helm.melee_damage*melee_damage_weight + 
                                helm.melee_crit*melee_crit_weight + helm.melee_speed*melee_speed_weight + helm.ranged_damage*ranged_damage_weight + helm.ranged_crit*ranged_crit_weight + 
                                helm.magic_damage*magic_damage_weight + helm.magic_crit*magic_crit_weight + helm.mana*mana_weight + helm.summon_damage*summon_damage_weight + 
                                helm.minion_slots*minion_slots_weight)
                        if hasattr(set2, 'chestplates'):
                            chestplate_score = (chest.defense*defense_weight + chest.damage*damage_weight + chest.crit*crit_weight + chest.movement*movement_weight + chest.melee_damage*melee_damage_weight + 
                                chest.melee_crit*melee_crit_weight + chest.melee_speed*melee_speed_weight + chest.ranged_damage*ranged_damage_weight + chest.ranged_crit*ranged_crit_weight + 
                                chest.magic_damage*magic_damage_weight + chest.magic_crit*magic_crit_weight + chest.mana*mana_weight + chest.summon_damage*summon_damage_weight + 
                                chest.minion_slots*minion_slots_weight)
                        if hasattr(set3, 'leggings'):
                            leggings_score = (set3.leggings.defense*defense_weight + set3.leggings.damage*damage_weight + set3.leggings.crit*crit_weight + set3.leggings.movement*movement_weight + set3.leggings.melee_damage*melee_damage_weight + 
                                set3.leggings.melee_crit*melee_crit_weight + set3.leggings.melee_speed*melee_speed_weight + set3.leggings.ranged_damage*ranged_damage_weight + set3.leggings.ranged_crit*ranged_crit_weight + 
                                set3.leggings.magic_damage*magic_damage_weight + set3.leggings.magic_crit*magic_crit_weight + set3.leggings.mana*mana_weight + set3.leggings.summon_damage*summon_damage_weight + 
                                set3.leggings.minion_slots*minion_slots_weight)
                        if hasattr(set, 'helmets') and hasattr(set2, 'chestplates') and hasattr(set3, 'leggings'):
                            if helm.set_identifier == chest.set_identifier == set3.leggings.set_identifier or helm.set_identifier == chest.set_identifier == 87:   # if combo is a full set, calculate the set_bonus score
                                if set.set_bonus != None:
                                    set_bonus_score += (set.set_bonus.defense*defense_weight +
                                        set.set_bonus.damage*damage_weight + set.set_bonus.crit*crit_weight + set.set_bonus.movement*movement_weight + 
                                        set.set_bonus.melee_damage*melee_damage_weight + set.set_bonus.melee_crit*melee_crit_weight + set.set_bonus.melee_speed*melee_speed_weight + 
                                        set.set_bonus.ranged_damage*ranged_damage_weight + set.set_bonus.ranged_crit*ranged_crit_weight + 
                                        set.set_bonus.magic_damage*magic_damage_weight + set.set_bonus.magic_crit*magic_crit_weight + set.set_bonus.mana*mana_weight + 
                                        set.set_bonus.summon_damage*summon_damage_weight + set.set_bonus.minion_slots*minion_slots_weight)
                                if helm.set_bonus != None:
                                    set_bonus_score += (helm.set_bonus.defense*defense_weight +
                                        helm.set_bonus.damage*damage_weight + helm.set_bonus.crit*crit_weight + helm.set_bonus.movement*movement_weight + 
                                        helm.set_bonus.melee_damage*melee_damage_weight + helm.set_bonus.melee_crit*melee_crit_weight + helm.set_bonus.melee_speed*melee_speed_weight + 
                                        helm.set_bonus.ranged_damage*ranged_damage_weight + helm.set_bonus.ranged_crit*ranged_crit_weight + 
                                        helm.set_bonus.magic_damage*magic_damage_weight + helm.set_bonus.magic_crit*magic_crit_weight + helm.set_bonus.mana*mana_weight + 
                                        helm.set_bonus.summon_damage*summon_damage_weight + helm.set_bonus.minion_slots*minion_slots_weight)
                                if chest.set_bonus != None:
                                    set_bonus_score += (chest.set_bonus.defense*defense_weight +
                                        chest.set_bonus.damage*damage_weight + chest.set_bonus.crit*crit_weight + chest.set_bonus.movement*movement_weight + 
                                        chest.set_bonus.melee_damage*melee_damage_weight + chest.set_bonus.melee_crit*melee_crit_weight + chest.set_bonus.melee_speed*melee_speed_weight + 
                                        chest.set_bonus.ranged_damage*ranged_damage_weight + chest.set_bonus.ranged_crit*ranged_crit_weight + 
                                        chest.set_bonus.magic_damage*magic_damage_weight + chest.set_bonus.magic_crit*magic_crit_weight + chest.set_bonus.mana*mana_weight + 
                                        chest.set_bonus.summon_damage*summon_damage_weight + chest.set_bonus.minion_slots*minion_slots_weight)      
                        
                        total_score = helmet_score + chestplate_score + leggings_score + set_bonus_score
                        combo_scores.append((total_score, (helm, chest, set3.leggings), set_bonus_score))
                

# Sort the combo_scores list based on descending scores
combo_scores.sort(key=lambda x: x[0])

# Output message
print(f'\n{combo_scores[-1][1][0].name}, {combo_scores[-1][1][1].name}, and {combo_scores[-1][1][2].name} give the highest score of {combo_scores[-1][0]}, given class is set to {target_class} and target stat is set to {target_stat}. This combination gives the following stats: \n')

for piece in combo_scores[-1][1]:
    print('\n', piece.name)
    for attr in dir(piece):
        if type(getattr(piece, attr)) == int and getattr(piece, attr) != 0 and attr != 'set_identifier':
            print(getattr(piece, attr), attr)
    if len(piece.ability) > 0:
        print(piece.ability)


if type(combo_scores[-1][2]) == float:
    print('\n Set Bonus')
    for piece in combo_scores[-1][1]:
        for attr in dir(piece.set_bonus):
            if type(getattr(piece.set_bonus, attr)) == int and getattr(piece.set_bonus, attr) != 0 and attr != 'set_identifier':
                print(getattr(piece.set_bonus, attr), attr)

    # Add full set bonus, not just armor set bonus
                

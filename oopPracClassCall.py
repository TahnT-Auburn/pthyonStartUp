### OBJECT-ORIENTED PROGRAMMING PRACTICE (CLASS CALL) ###

#%%
import os
import numpy as np
import array as arr

os.system('cls')

#%%
# --- call shinobi class ---
from objectOrientedProgPrac import Shinobi

# define instances of Shinobi class
Naruto = Shinobi('Naruto',17,'Hidden Leaf Village','Jinchuriki',9.6)
Sasuke = Shinobi('Sasuke',18,'Hidden Leaf Village','Sharingan',9.6)
Sakura = Shinobi('Sakura',17,'Hidden Leaf Village','Strength',7.1)
Kakashi = Shinobi('Kakashi',31,'Hidden Leaf Village','Sharingan',9.5)

# show output
shinobiOutput = 0

# display
if shinobiOutput == 1:

    print(Naruto)
    print(Sasuke)
    print(Sakura)
    print(Kakashi)

    print('\n')

    # define battle contenders
    contenders = [Naruto, Kakashi]
    print('Contenders:', contenders[0].name, ',', contenders[1].name)

    # battle outcome
    powDiff = contenders[0].powerLevel() - contenders[1].powerLevel()
    if powDiff > 0:
        print('Victor:', contenders[0].name,'\n','Power Difference:',abs(powDiff))
    elif powDiff < 0:
        print('Victor:', contenders[1].name,'\n','Power Difference:',abs(powDiff))
    elif powDiff == 0:
        print('Draw')

    print('\n')

    #print(Shinobi.__dict__) # shows all attributes for Class level
    #print(Naruto.__dict__) # shows all attributes for instance level

elif shinobiOutput == 0:
    pass

#%%
# --- call MajikShop class ---
from objectOrientedProgPrac import MajikShop
from objectOrientedProgPrac import Boots
from objectOrientedProgPrac import Swords


# define items in shop
swift_foot_boots = Boots('Swift Foot Boots', 20, 20, 1)
lightning_greaves = Boots('Lightning Greaves', 25, 25, 2)
sword_of_vengence = Swords('Sword of Vengence', 40, 15)
black_blade_reforged = Swords('Black Blade Reforged', 45, 10)
sword_of_fire_and_ice = Swords('Sword of Fire and Ice', 85, 5)

# define shop output
shopOutput = 1

# display
if shopOutput == 1:

    '''
    print(swift_foot_boots)
    swift_foot_boots.applyDiscount()
    print(swift_foot_boots.calculateTotalPrice())

    print('\n')

    for instance in MajikShop.all:
        print(instance.name)
    '''

    #MajikShop.instantiateFromCsv()
    print('All items:','\n', MajikShop.all)
    print('\n')
    print('All boots:','\n',Boots.all_boots)
    print('\n')
    print('All swords:','\n',Swords.all_swords)

    print('\n')

    print('Call Boots items and price:')
    print(Boots.all_boots,'\n', Boots.all_boots_price)
    print('\n')
    print('Call Swords items and price:')
    print(Swords.all_swords,'\n', Swords.all_swords_price)
    
    '''
    for boots in np.all_boots:
        print(np.all_boots[boots], ':', np.all_boots_price[boots])
    ''' 

elif shopOutput == 0:
    pass


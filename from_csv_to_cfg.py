import csv

# Open csv file
data_list = list()
with open('Updated_item_defaults.csv', 'r') as f:
    reader = csv.reader(f, skipinitialspace=True, delimiter=',')
    for row in reader:
        data_list.append(row)

# From list to str
def get_str_line(line_list:list) -> str:
    name = line_list[0] if ':' in line_list[0] else f'{line_list[0]}:'
    return f'{name} Stack = {line_list[1]} Price = {line_list[2]} SellPrice = {line_list[3]} Tradeable = {line_list[4]} IgnoreWaitForDiscovery = {line_list[5]} Sellable = {line_list[6]}'

# Completed data text
data_text = '\n'.join([get_str_line(l) for l in data_list])

# Default text
text_before_data = '''#################################################################################################################################################################################################
###->IF YOU'VE RUN THE GAME EVEN ONCE SINCE INSTALLING BETTER TRADER, EDITING THIS FILE WON'T DO ANYTHING UNLESS YOU DELETE THE BepInEx/config/Menthus.bepinex.plugins.BetterTrader.cfg FILE<-###
#############->UNLESS YOU WANT TO ADD MORE ITEMS TO BETTER TRADER, YOU SHOULD USE THE BepInEx/config/Menthus.bepinex.plugins.BetterTrader.cfg FILE TO MAKE ANY ADDITIONAL CHANGES<-##############
#################################################################################################################################################################################################

#################################EXAMPLES##################################
Example1 AncientSeed
Example2 AncientSeed: Stack = 1
Example3 AncientSeed: Stack = 1 Price = 30 SellPrice = 30 Tradeable = true IgnoreWaitForDiscovery = false
Example4 AncientSeed: Price = 20
Example5 AncientSeed: IgnoreWaitForDiscovery = true

Note: Settings are not case sensitive(e.g., stack or Stack will both work).
###########################################################################

#################################EpicLoot##################################
EpicLoot items will only load if you have EpicLoot installed. Scroll down
until you find #EpicLoot# and add any items you want Better Trader to handle
below that line. A few are set by default, which you can add/remove/modify
to your liking. Modifying EpicLoot items works the same as any other(see EXAMPLES
above).
###########################################################################

If you enable WaitForDiscovery in BepInEx/config/Menthus.bepinex.plugins.BetterTrader.cfg, tradeable = true means the item will be sold by the trader after you've discovered the item.
If tradeable = false, then even after you've discovered the item it still won't be sold.
IF THE WaitForDiscovery OPTION ISN'T SHOWING UP, BE SURE TO RUN THE GAME AT LEAST ONCE WITH BetterTrader INSTALLED! THE OPTION WILL BE GENERATED ON STARTUP!

#Better Trader#
'''
text_after_data = '''

#EpicLoot#
##RunestoneMagic: stack = 1 price = 100 sellprice = 100 tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##RunestoneRare: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##RunestoneEpic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##RunestoneLegendary: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ShardMagic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ShardRare: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ShardEpic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ShardLegendary: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##DustMagic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##DustRare: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##DustEpic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##DustLegendary: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ReagentMagic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ReagentRare: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ReagentEpic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##ReagentLegendary: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##EssenceMagic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##EssenceRare: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##EssenceEpic: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
##EssenceLegendary: Stack = 1 Price = 100 SellPrice = 100 Tradeable = true IgnoreWaitForDiscovery = false Sellable = true
'''

# Create a config file
with open('CREATED_item_defaults.cfg', 'w') as file:
    file.write(f'{text_before_data}{data_text}{text_after_data}')

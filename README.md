# ![GitHub Logo](/.github/atechtree.png) TechTree reborn release 

### Table of contents
 - 

## TechTree 0.5.3
<details>
  <summary>Changelog</summary>
  
  ### 0.5.3
  - automatical layout database update
  - layout selection in-game  
  
</details>

## getTanks 0.5.0

### About
This mod generates list of tanks available for techtree in-game
- scan game for all available vehicles currently in game
- creates report in form of CSV file in ''' mods/<current_version>_tankList.csv '''

### Available informations
<details>
 <summary>List</summary>
  
 - nation code
 - long tank name for XML
 - ingame name
 - in-nation ID
 - compactDescriptionID (used by all game mechanics)
 - vehicle level
 - vehicle class (LT, MT, HT, AT, SPG)
 - premium status
 - premiumIGR - vehicles for gameshow accouts
 - hidden - not yet released and/or removed tanks
 - fallout game mode vehicles
 - bob - team clash rental BB tanks
 - collector vehicle status
 - isOnlyForEventBattles - special event vehicle
 - isOnlyForEpicBattles - FL battles vehicles 
 - isOnlyForBattleRoyaleBattles - SH steel hunter vehicles
 - *any remaing unresolved tag
</details>
### Settings
- <details>
   <summary>Ignore vehicles specified in ignoreList</summary>
   When allowed mod will ignore tanks specified in ignore list when generating new report.
   
   ''' mods\configs\techtree\ignoreList.txt '''
</details>
- <details>
   <summary>List of currently ignored vehicles</summary>
   Displays tank names specified in ignoreList.
   Only for information.
   
   Formating: each line in ignoreList.txt represents one tank.
   You have to specify nation and tank name separated by ':'. IE:
   ''' <nation>:<long_name> '''
   ie:
   ''' ussr:observer
    germany:G25_PzII_Luchs '''
	
   
</details>
 
  
  ### 0.5.3
  - automatical layout database update
  - layout selection in-game  
  


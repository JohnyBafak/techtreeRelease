# ![GitHub Logo](/.github/atechtree.png) TechTree
### version 0.5.3

- [About](#About)
- [Custom Layouts](#custom-layouts)
- [Settings](#Settings)
- [Issues](#Issues)
- [To-Do](#TO-DO)
- [getTanks](#getTanks-050)


<details>
  <summary>Changelog</summary>
  
  #### 0.5.3
  - automatical layout database update
  - layout selection in-game  
  
</details>

## About [top](#-TechTree)
aTechTree mod bring back most of the old features:
- 2 basic horizontal layouts
- custom layout support
- show collector's vehicles in TT
- show hidden premium tanks
- show special/reward tanks
- show hidden&secret vehicles
- in-game settings
- unlock comparison for all tanks in game
- preview all tanks in game (works well with missing tank mod)
- automaticaly update layout data

#### Requirements:
For optimal user-experience following mods are recomended:
- [izebreg's ModsSettingsAPI](https://bitbucket.org/IzeBerg/modssettingsapi/downloads/)
- [P0LIR0ID's modsListAPI](https://bitbucket.org/P0LIR0ID/wot-modslist/downloads/)

## Custom layouts
Don't like predefined layouts? Create your own, here is how:

1. Create new folder in 
```
mods\configs\techtree\xml\
```

2. Add all *nation-tree* and *nation-premium* .XML files into that folder

3. Edit XML files

4. Select your layout from ingame settings


## Settings
comming soon

## Issues
no feedback yet

## TO-DO






# getTanks 0.5.0 
######[top](#)

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
 *any remaing unresolved tag
</details>

### Settings
- <details>
   <summary>Ignore vehicles specified in ignoreList</summary>
   When allowed mod will ignore tanks specified in ignore list when generating new report.
   
   ``` 
   mods\configs\techtree\ignoreList.txt 
   ```
</details>

- <details>
   <summary>List of currently ignored vehicles</summary>
   Displays tank names specified in ignoreList.
   Only for information.
   
   Formating: each line in ignoreList.txt represents one tank.
   You have to specify nation and tank name separated by colon:
   ```
   <nation>:<long_name> 
   ```
   For example:
   ```
   ussr:observer
   germany:G25_PzII_Luchs 
   ```
</details>

- <details>
   <summary>Generate new list on start-up</summary>
   Mod will try to create a new vehicle list every time game is lauched. Not recomended.
   
</details>

- <details>
   <summary>Generate vehicle list</summary>
   Forcing tankList to be generated from game.
   
</details>

### TO-DO
- add tank price into available informations

  
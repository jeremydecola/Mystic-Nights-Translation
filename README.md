# Mystic Nights (PS2) English Translation 

Mystic Nights (미스틱 나이츠) is an obscure Korean-Exclusive survival horror Playstation 2 title.
It was developed by N-Log Corporation and published by Sony Computer Entertainment of Korea in 2005.
Although a North-American release was planned, Sony mysteriously pulled the plug.

Little is known about this game and it is extremely difficult to track down, even in Korea.
As a big fan of the survival horror genre, I took it upon myself to translate the title in hopes that it reaches a wider audience.

I hope you enjoy!

The gentlemen at cdromance have gone through the trouble of uploading a pre-patched copy of the game.
Download: https://cdromance.com/ps2-iso/mystic-nights-english-patched/

If you like my work, feel free to show your support: https://ko-fi.com/jeremydecola

<p align="center">
  <img src="GRAPHICS/COVERART.png" width=50%>  
</p>

Art commission by u/thienpnguyen.

## Acknowledgements 

Reverse engineering this game was quite a challenge and I learned quite a bit thanks to the folks on Reverse Engineering StackExchange. 

As for the translation, none of this would have been possible without the help of my girlfriend who so graciously helped me translate the entire game. 

Finally, I would like to extend a big thank you to u/thienpnguyen who did a fantastic job with the art I commissioned from him. 

Mystic Nights is property of N-Log Soft and SCE Korea. 

I did not develop the xpert tool. Info on xpert can be found at http://xpert2.blogspot.com/2006/.

## Tips

* This game requires a lot of grinding for ammunition. Skipping enemies and rushing to the next objective may leave you unprepared for the boss fights and is not recommended, even on Easy mode. 
* Each enemy type is weak to a specific weapon type. Exploiting enemy weaknesses is key to ensuring your survival. 
* There are two items (Data Stick H and Data Stick B) which affect the endings you can get. It seems there is some kind of function that computes which item can be obtained. Reloading a save just before acquiring the item allowed me to obtain the other one. 

1. ENDING A (SPOILERS)
<details>
  <summary>SHOW</summary>

  ```
  Allen - Good Ending : 
  * Obtain all notes.
  * Receive Data Stick B.
  * Side with Allen in the fight between Allen and Jennifer. 
  ```
</details>

2. ENDING B (SPOILERS)
<details>
  <summary>SHOW</summary>

  ```
  Jennifer - Good Ending : 
  * Picking up all notes does not affect this specific situation.
  * Receive Data Stick H.
  * Side with Jennifer in the fight between Allen and Jennifer. 
  ```
</details>

3. ENDING C (SPOILERS)
<details>
  <summary>SHOW</summary>

  ```
  Allen - Bad Ending : 
  * OPTION 1: Do not obtain all notes and Recieve Data Stick B.
  * OPTION 2: Receive Data Stick H.
  * Side with Allen in the fight between Allen and Jennifer. 
  ```
</details>

4. ENDING D (SPOILERS)
<details>
  <summary>SHOW</summary>

  ```
  Jennifer - Bad Ending : 
  * Picking up all notes does not affect this specific situation.
  * Receive Data Stick B.
  * Side with Jennifer in the fight between Allen and Jennifer. 
  ```
</details>

## Prerequisites

* A copy of the Mystic Nights disc image (.iso) 
* xpert (PS2/PSP .iso extraction/rebuilding tool)
* SCKA_200.55 (mapping, menu and system messages)
* RES/SUBSYS.RES (dialogue, item names, item descriptions)
* RES/UI/COMPANY.RES (warning screen)
* RES/UI/DOCUMENT.RES and RES/UI/ITEM.RES (item and document text)
* RES/SCENE/ST01-03/ and RES/SCENE/ST04-07/ (level-specific item mapping)

## Instructions

1) Launch "xpert.exe".
2) Select the PS2 CdDvD5 plugin.
3) Click on "Open an Image File" > Select your .iso file.
4) Click on "Extract LBA".
5) Click on "Extract File".
6) Navigate to the folder it extracted the .iso to 
7) In the root folder, replace "SCKA_200.55" with mine.
8) Copy all files in my "RES" folder into "/RES/" 
9) Click on "Rebuild File".
10) Click on "Rebuild LBA".

Congratulations. xpert should have generated a new .iso image complete with my English translation!

## Bug Reporting
Please report any bugs or issues (such as off-screen text or typos) to jeremydecola@gmail.com. 
Screenshots would be appreciated. 

## *PROGRESS*
### v1.1.0
Big thanks to Reed Armstrong for pointing out a vast majority of the mistakes in my translation. 
* A: Spelling mistakes fixed
* B: Grammatical errors fixed
* C: Offscreen text and awkward line breaking fixed. 

### v1.0.1
Typographical Errors Fixed. 
Credit to Reed Armstrong and Daniel Rain (YouTube). 

### v1.0.0
Initial Public Release! 

### 0.9.12-beta
MAJOR AESTHETIC UPDATE PART 2: Removed the remaining trailing spaces (20) in cutscenes and replaced them with null bytes (00) after discovering that cutscenes become interactable (skipable) after first playthrough. 

### 0.9.11-beta
* Multiple Endings discovered
* Various typographical errors fixed
* TOMCAT item aesthetic renaming
* Fixed visual artifacts for 'Data Stick H'

### 0.9.10-beta
* Various typographical errors fixed

### 0.9.9-beta
* Various typographical errors fixed

### 0.9.8-beta
MAJOR AESTHETIC UPDATE: Removed all trailing spaces (20) in dialogue and replaced them with null bytes (00). 

### 0.9.7-beta
'DOCUMENT.RES' contains the text displayed ONLY on pickup of a document. 'ITEM.RES' contains the text displayed in documents when accessing them through the 'NOTES' section of the menu. 
* Fixed a bug which caused 'Secrets' to be unobtainable.
* Fixed visual artifacts for 'Data Stick (5,7,8,9,11,12,S,S1,S2,B,X)', 'Decree', 'KP's Diary' and 'Friendly Advice'
* Fixed off-screen text for 'Bloody Schedule', 'Power Guide', 'Secrets', 'Data Stick (3 [pickup only],6,S3,S4)' and 'Letter for Greg'
* Power Cylinder A -> Cylinder A
* Power Cylinder B -> Cylinder B
* Power Cylinder C -> Cylinder C
* Power Cylinder D -> Cylinder D

### 0.9.6-beta
Various fixes for off-screen text and removal of unecessary spacing. 
* Military Strategy Letter -> Letter for Greg
* Fixed visual artifacts for 'Monica's Note', 'Data Stick 3', 'Letter for Greg', 'Data Stick 4', 'Larva Report' and 'D's Journal'
* Fixed '%s acquired' spacing aesthetic in SCKA_200.55
* Fixed a bug which caused 'Experiment Report' and 'W's Diary' to dissapear after pickup. (Introduced in 0.9.5-beta)

### 0.9.5-beta
* MASSIVE OVERHAUL OF ITEM NAMES AND REMOVAL OF SPACE CHARACTERS. BUG REPORT SPREADSHEET HAS BEEN CLEARED. WILL RESTART PLAYTHROUGH. 
If the null byte (00) is added in SCKA_200.55 for item names, the item name displays off-center and goes off the screen if too long. 
As such, the space character (20) should be used for these specific items (mainly weapons). Some weapons were renamed to fit the screen:
* Vampire Blade -> Butcher
* Ancient Blade -> Slayer
* Kaiser Blade -> Reaper
* Vampire Pistol -> Cobra
* Ancient Pistol -> Viper
* Kaiser Pistol -> Venom
* Vampire Rifle -> Silent Star
* Ancient Rifle -> Red Rum
* Kaiser Rifle -> Black Widow
* Vampire Shot -> Avarice
* Ancient Shot -> Malice
* Kaiser Shot -> Envy
* Light Vest -> Normal Vest
* Heavy Vest -> Sturdy Vest

### 0.9.4-beta
Adding the null byte (00) instead of the space character (20) removes the trailing white space after an item name. 
* Fixed 'Memo for Walter' bug by adding an extra page. (Previous fix did not work).
* Created a bug_report excel table for tracking of ITEMS or DOCUMENTS with problems.
* Corrected all references to the 'Blade' weapon as 'Knife'. 
* Fixed various off-screen text issues. 
* Fixed 'Guidelines', 'Operations', 'Genetics Report' and 'Data Stick 1' which all had visual artifacts due to overflow.
* Fixed various typos
* Shortened 'B1 Control Room Key' to 'B1 Control Key' to avoid having letters go off-screen in the ITEMS menu. 

### 0.9.3-beta
* Discovered omission where Jennifer's groaning noises were left untranslated.
* Discovered omission where Room Names appear in Korean when entering rooms. 
* Fixed bug which caused 'Strong Vest' and 'Medkit (L)' not to be added to inventory in some scenes.
* Fixed off-screen text : [TIP] Section : PRESS THE *BUTTON* BUTTON -> PRESS *BUTTON* 
* Fixed Jennifer's lines to better reflect in-game scenario.
* Fixed 'Memo for Walter' content to better reflect in-game scenario. 
* Fixed bug which caused 'Memo for Walter' page 1 to display with visual artifacts.

### 0.9.2-beta 
Fixed references for item names that were changed in 0.5.0 in scene file maps.

* 유충 관찰 보고서 (Larvae Report -> Larva Report)
4 MATCHES FOUND.
SUBSYS.RES, ST0302_3.RES, DOCUMENT.RES, ITEM.RES

* 동력실 근무 명령서 (Power Room Order -> Bloody Schedule)
4 MATCHES FOUND.
SUBSYS.RES, ST0501_2.RES, DOCUMENT.RES, ITEM.RES

* 근무지 이탈 주의 메모 (Deserter's Memo -> Friendly Advice)
4 MATCHES FOUND.
SUBSYS.RES, ST0501_2.RES, DOCUMENT.RES, ITEM.RES

* 감사 지침문 (User Manual -> Decree)
4 MATCHES FOUND.
SUBSYS.RES, ST0403_2.RES, DOCUMENT.RES, ITEM.RES

### 0.9.1-beta
Fixed Dialogue to reflect changes:
Project Vampyre -> Project Ancient
Vampyre -> Vampire

### 0.9.0-beta
TRANSLATION COMPLETE! 

### 0.5.0
DOCUMENT RESOURCE FILE TRANSLATION COMPLETE!
CHANGES MUST BE REPLICATED IN THE ITEM RESOURCE FILE.
Change of Item Names: 
Larvae Report -> Larva Report
Power Room Order -> Bloody Schedule 
Deserter’s Memo > Friendly Advice
User Manual > Decree
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 100% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE
* DOCUMENTS: 100% COMPLETE 
* NETWORK features partially translated.

### 0.4.2
DOCUMENTS PROGRESSING WELL. PLOT ELEMENTS VALIDATED WITH NATIVE SPEAKER AND AESTHETIC CHANGES TO CERTAIN WORDS. (Vampyre -> Vampire / Project Vampyre -> Project Ancient / Palmata -> Palmate Leaves / Ancient Vampyres -> Ancients)  
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 100% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE
* DOCUMENTS: 50% COMPLETE 
* NETWORK features partially translated.

### 0.4.1
DOCUMENTS UNDERWAY. DISCOVERED DOCUMENT MAPPING. 
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 100% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE
* DOCUMENTS: 5% COMPLETE (A's Letter)
* NETWORK features partially translated.

### 0.4.0
COMPLETED SYSTEM/MENUS WITH THE EXCEPTION OF NETWORK FEATURES.
DOCUMENTS UNDERWAY.  
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 100% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE
* DOCUMENTS: 0% COMPLETE
* NETWORK features partially translated

### 0.3.3
TRANSLATED SETTINGS SCREEN (OPTIONS > MORE). 
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 99% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE

### 0.3.2
TRANSLATED CONTROLS SCREEN. 
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 95% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE

### 0.3.1
MAJORITY OF SYSTEM/MENUS COMPLETE. 
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 90% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE

### 0.3.0
COMPLETED LEVEL MAPPING. SYSTEM/MENUS TRANSLATION UNDERWAY. 
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 5% COMPLETE 
* SCENE FILE MAPPING : 100% COMPLETE

### 0.2.2
COMPLETED ITEM TRANSLATION. LEVEL MAPPING UNDERWAY. 
* TEXT: 100% COMPLETE 
* ITEMS: 100% COMPLETE
* SYSTEM/MENUS: 5% COMPLETE 
* SCENE FILE MAPPING COMPLETE FOR: Medkit, Vest, Serum, Blade, Pistol, Rifle, Shot, Mag, MEL Key, 2F Map, Central Key Card.

### 0.2.1
REORGANIZED REPOSITORY. BEGAN LEVEL MAPPING.
* TEXT: 100% COMPLETE 
* ITEMS: 50% COMPLETE
* SYSTEM/MENUS: 5% COMPLETE 
* SCENE FILE MAPPING COMPLETE FOR: Medkit, Vest, Serum, Blade, Pistol, Rifle, Shot, Mag, MEL Key, 2F Map, Central Key Card.

### 0.2.0
FINAL COVER ART FOR GAME COMPLETE.
* TEXT: 100% COMPLETE 
* ITEMS: 50% COMPLETE
* SYSTEM/MENUS: 5% COMPLETE 
* FIXED MAJOR MAPPING PROBLEM FOR ITEMS THAT CAUSED ITEMS TO NOT BE ADDED TO INVENTORY. 
* DISCOVERED MAPPING MECHANISM WITH SCENE RESOURCE FILES. 

### 0.1.3
BROKEN. 
* TEXT: 100% COMPLETE 
* ITEMS: 50% COMPLETE
* SYSTEM/MENUS: 1% COMPLETE
* ITEM MAPPING BROKEN!

### 0.1.2
DIALOGUE TRANSLATION COMPLETE.
* TEXT: 100% COMPLETE 
* ITEMS: 0% COMPLETE
* SYSTEM/MENUS: 1% COMPLETE

### 0.1.1
* TEXT: 99% COMPLETE ~ Translation revised. Missing words and punctuation. Genetics Lab > GH Storage Room.
* ITEMS: 0% COMPLETE
* SYSTEM/MENUS: 0% COMPLETE

### 0.1.0
* TEXT: 95% COMPLETE ~ UNTRANSLATED PORTIONS ARE BEING INTERPRETED BY A NATIVE SPEAKER.
* ITEMS: 0% COMPLETE
* SYSTEM/MENUS: 0% COMPLETE

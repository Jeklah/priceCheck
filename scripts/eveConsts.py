# This is the constants file for the ship cost calculator.
# It may grow to contain more general eve constants so will keep the name 'eveConsts'
#
# Author: Jeklah
# Date: 10/05/2020

ptIndex = 1     # Index for the indicator value of partindex in shipPartCounts
countIndex = 1  # Index for the indicator value of countindex in shipPartCounts
shipIndex = 0   # Index for the name of the ship in shipPartCounts
partIndex = 2   # This acts as an index for when the partindex list needs to be referenced
shipList = []   # Initalising shipList.

oreList = [
            'Tritanium',
            'Pyerite',
            'Isogen',
            'Megacyte',
            'Mexallon',
            'Nocxium',
            'Zydrine'
           ]

marketList = [
                'jita',
                'hek',
                'amarr',
                'rens',
                'dodixie'
              ]

capitalPartsList = [
                'Capital Armor Plates',
                'Capital Capacitor Battery',
                'Capital Cargo Bay',
                'Capital Computer System',
                'Capital Construction Parts',
                'Capital Corporate Hangar Bay',
                'Capital Sensor Cluster',
                'Capital Ship Maintenance Bay',
                'Capital Propulsion Engine',
                'Capital Clone Vat Bay',
                'Capital Drone Bay',
                'Capital Jump Drive',
                'Capital Power Generator',
                'Capital Shield Emitter'
            ]

shipPartCounts = [
    (('Orca'), ('partIndex', '1', '2', '3', '4', '5', '6', '7'), ('count', '9', '35', '7', '15', '4', '4', '7')),
    (('Obelisk'), ('partIndex', '0', '2', '4', '8'), ('count', '15', '81', '51', '16')),
    (('Venture'), ('oreIndex', '2', '4', '5', '1', '0', '6'), ('count', '400', '670', '45', '6700', '22401', '20')),
    (('Providence'), ('partIndex', '0', '2', '4', '8'), ('count', '16', '75', '48', '20')),
    (('Caracal'), ('oreIndex', '2', '3', '4', '5', '1', '0', '6'), ('count', '9400', '501', '33001', '3000', '110000', '490000', '1260')),
    (('Gila'), ('oreIndex', '2', '3', '4', '5', '1', '0', '6'), ('count', '8719', '321', '35917', '2149', '138810', '552921', '1082')),
    (('Tristan'), ('oreIndex', '2', '3', '4', '5', '1', '0', '6'), ('count', '300', '2', '2700', '71', '5700', '21000', '20')),
    (('Rattlesnake'), ('oreIndex', '2', '3', '4', '5', '1', '0', '6'), ('count', '148876', '5745', '602482', '37478', '2471520', '10150680', '18185')),
    (('Rorqual'), ('partIndex', '0', '1', '2', '9', '3', '4', '5', '10', '11', '12', '8', '6', '13', '7'), ('count', '7', '10', '20', '30', '30', '40', '16', '6', '10', '10', '9', '9', '9', '30')),
]

for ship in shipPartCounts:
    shipList.append(ship[shipIndex])

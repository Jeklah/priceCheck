# This is the constants file for the ship cost calculator.
# It may grow to contain more general eve constants so will keep the name 'eveConsts'
#
# Author: Jeklah
# Date: 10/05/2020

ptIndex = 1     # Index for the indicator value of partindex list of ships
countIndex = 1  # Index for the indicator value of countindex list of ships
partIndex = 2   # This acts as an index for when the partindex list needs to be referenced
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

shipList = [
                'Orca',
                'Obelisk',
                'Venture',
                'Providence',
                'Caracal',
                'Gila',
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
            ]

shipPartCounts = [
    (('Orca'), ('partIndex', '1', '2', '3', '4', '5', '6', '7'), ('count', '9', '35', '7', '15', '4', '4', '7')),
    (('Obelisk'), ('partIndex', '0', '2', '4', '8'), ('count', '15', '81', '51', '16')),
    (('Venture'), ('oreIndex', '2', '4', '5', '1', '0', '6'), ('count', '400', '670', '45', '6700', '22401', '20')),
    (('Providence'), ('partIndex', '0', '2', '4', '8'), ('count', '16', '75', '48', '20')),
    (('Caracal'), ('oreIndex', '2', '3', '4', '5', '1', '0', '6'), ('count', '9400', '501', '33001', '3000', '110000', '490000', '1260')),
    (('Gila'), ('oreIndex', '2', '3', '4', '5', '1', '0', '6'), ('count', '8719', '321', '35917', '2149', '138810', '552921', '1082')),
]

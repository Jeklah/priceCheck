pcIndex = 1     # This acts as an index for parts and a starting point for count
partIndex = 2   # This acts as an index for parts when it is referenced to with an index of 2
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
]

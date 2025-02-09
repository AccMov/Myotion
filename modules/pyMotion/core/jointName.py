class jointName:
    short = [
        "UT-L",
        "UT-R",
        "MT-L",
        "MT-R",
        "LT-L",
        "LT-R",
        "AD-L",
        "AD-R",
        "MD-L",
        "MD-R",
        "PD-L",
        "PD-R",
        "PM-L",
        "PM-R",
        "LD-L",
        "LD-R",
        "BB-L",
        "BB-R",
        "TB-L",
        "TB-R",
        "BRD-L",
        "BRD-R",
        "ECRL-L",
        "ECRL-R",
        "ECRB-L",
        "ECRB-R",
        "ECU-L",
        "ECU-R",
        "ED-L",
        "ED-R",
        "EDM-L",
        "EDM-R",
        "EI-L",
        "EI-R",
        "FCR-L",
        "FCR-R",
        "PL-L",
        "PL-R",
        "FCU-L",
        "FCU-R",
        "FDS-L",
        "FDS-R",
        "FDP-L",
        "FDP-R",
        "FPL-L",
        "FPL-R",
        "SSP-L",
        "SSP-R",
        "ISP-L",
        "ISP-R",
        "SSC-L",
        "SSC-R",
        "TM-L",
        "TM-R",
        "RA-L",
        "RA-R",
        "EO-L",
        "EO-R",
        "IO-L",
        "IO-R",
        "TA-L",
        "TA-R",
        "ES-L",
        "ES-R",
        "GM-L",
        "GM-R",
        "Gme-L",
        "Gme-R",
        "BF-L",
        "BF-R",
        "ST-L",
        "ST-R",
        "SM-L",
        "SM-R",
        "VL-L",
        "VL-R",
        "VM-L",
        "VM-R",
        "VI-L",
        "VI-R",
        "RF-L",
        "RF-R",
        "TIBA-L",
        "TIBA-R",
        "GCM-L",
        "GCM-R",
        "GCL-L",
        "GCL-R",
        "SOL-L",
        "SOL-R",
    ]
    long = [
        "Trapezius (upper)-L",
        "Trapezius (upper)-R",
        "Trapezius (middle)-L",
        "Trapezius (middle)-R",
        "Trapezius (lower)-L",
        "Trapezius (lower)-R",
        "Deltoid (anterior)-L",
        "Deltoid (anterior)-R",
        "Deltoid (middle)-L",
        "Deltoid (middle)-R",
        "Deltoid (posterior)-L",
        "Deltoid (posterior)-R",
        "Pectoralis Major-L",
        "Pectoralis Major-R",
        "Latissimus Dorsi-L",
        "Latissimus Dorsi-R",
        "Biceps Brachii-L",
        "Biceps Brachii-R",
        "Triceps Brachii-L",
        "Triceps Brachii-R",
        "Brachioradialis-L",
        "Brachioradialis-R",
        "Extensor Carpi Radialis Longus-L",
        "Extensor Carpi Radialis Longus-R",
        "Extensor Carpi Radialis Brevis-L",
        "Extensor Carpi Radialis Brevis-R",
        "Extensor Carpi Ulnaris-L",
        "Extensor Carpi Ulnaris-R",
        "Extensor Digitorum-L",
        "Extensor Digitorum-R",
        "Extensor Digiti Minimi-L",
        "Extensor Digiti Minimi-R",
        "Extensor Indicis-L",
        "Extensor Indicis-R",
        "Flexor Carpi Radialis-L",
        "Flexor Carpi Radialis-R",
        "Palmaris Longus-L",
        "Palmaris Longus-R",
        "Flexor Carpi Ulnaris-L",
        "Flexor Carpi Ulnaris-R",
        "Flexor Digitorum Superficialis-L",
        "Flexor Digitorum Superficialis-R",
        "Flexor Digitorum Profundus-L",
        "Flexor Digitorum Profundus-R",
        "Flexor Pollicis Longus-L",
        "Flexor Pollicis Longus-R",
        "Supraspinatus-L",
        "Supraspinatus-R",
        "Infraspinatus-L",
        "Infraspinatus-R",
        "Subscapularis-L",
        "Subscapularis-R",
        "Teres Major-L",
        "Teres Major-R",
        "Rectus Abdominis-L",
        "Rectus Abdominis-R",
        "External Oblique-L",
        "External Oblique-R",
        "Internal Oblique-L",
        "Internal Oblique-R",
        "Transversus Abdominis-L",
        "Transversus Abdominis-R",
        "Erector Spinae-L",
        "Erector Spinae-R",
        "Gluteus Maximus-L",
        "Gluteus Maximus-R",
        "Gluteus Medius-L",
        "Gluteus Medius-R",
        "Biceps Femoris-L",
        "Biceps Femoris-R",
        "Semitendinosus-L",
        "Semitendinosus-R",
        "Semimembranosus-L",
        "Semimembranosus-R",
        "Vastus Lateralis-L",
        "Vastus Lateralis-R",
        "Vastus Medialis-L",
        "Vastus Medialis-R",
        "Vastus Intermedius-L",
        "Vastus Intermedius-R",
        "Rectus Femoris-L",
        "Rectus Femoris-R",
        "Tibialis Anterior-L",
        "Tibialis Anterior-R",
        "Gastrocnemius (medial head)-L",
        "Gastrocnemius (medial head)-R",
        "Gastrocnemius (lateral head)-L",
        "Gastrocnemius (lateral head)-R",
        "Soleus-L",
        "Soleus-R",
    ]

    def __getattr__(self, name):
        if name == "short":
            return self.short
        elif name == "long":
            return self.long

    def __getitem__(self, name):
        if name == "short":
            return self.short
        elif name == "long":
            return self.long

    @staticmethod
    def getLongName(n):
        if n in jointName.short:
            return jointName.long[jointName.short.index(n)]
        elif n in jointName.long:
            return n
        else:
            return ""

    @staticmethod
    def getShortName(n):
        if n in jointName.long:
            return jointName.short[jointName.long.index(n)]
        elif n in jointName.short:
            return n
        else:
            return ""

    @staticmethod
    def getConcatName(n):
        if n in jointName.long:
            return "{} / {}".format(jointName.short[jointName.long.index(n)], n)
        elif n in jointName.short:
            return "{} / {}".format(n, jointName.long[jointName.short.index(n)])
        else:
            return n

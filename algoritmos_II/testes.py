from enum import Enum

class LanguagaID(Enum):
    cobol = 1
    jcl = 2
    flowchart = 3
    spark = 4
    java = 5

print(LanguagaID.cobol.value)

# Model to database

from .account_schema import Account

accounts = [
    Account(id=1, name="Ana"     , document="12301", bornDate="01/04/1983", email="ana@gmail.com"      , phoneNumber="19982013301"),
    Account(id=2, name="Rodrigo" , document="12302", bornDate="02/08/1996", email="rodrigo@hotmail.com", phoneNumber="41982013302"),
    Account(id=3, name="Bianca"  , document="12303", bornDate="03/02/1982", email="bianca@gmail.com"   , phoneNumber="61982013303"),
    Account(id=4, name="Fernanda", document="12304", bornDate="04/11/1999", email="fernanda@yahoo.com" , phoneNumber="19982013304"),
    Account(id=5, name="Murilo"  , document="12305", bornDate="05/09/1989", email="murilo@hotmail.com" , phoneNumber="24982013305"),
    Account(id=6, name="Renato"  , document="12306", bornDate="06/03/1994", email="renato@gmail.com"   , phoneNumber="55982013306"),
    Account(id=7, name="Maria"   , document="12307", bornDate="07/08/1988", email="maria@yahoo.com"    , phoneNumber="32982013307"),
    Account(id=8, name="Bruna"   , document="12308", bornDate="08/09/1991", email="bruna@gmail.com"    , phoneNumber="21982013308")
]
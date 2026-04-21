from model.features_contact import FeaturesContact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/features_contact.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o== "-f":
        f=a

#генератор рандомных строк
def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.punctuation +string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные тестовые данные
testdata=[
    FeaturesContact(firstname=random_string("firstname",4),
                    middlename=random_string("middlename",3),
                    lastname=random_string("lastname",6),
                    nickname=random_string("nick",3),
                    title=random_string("title",5),
                    company=random_string("comp",6),
                    address=random_string("addr",8),
                    home=random_string("+7",11),
                    mobile=random_string("+7",11),
                    work=random_string("+7",11),
                    fax=random_string("+7",11),
                    email=random_string("em1",12),
                    email2=random_string("em2",12),
                    email3=random_string("em3",12))
                    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))
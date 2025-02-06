
def load_dict(filename, source_field, target_field):
   d = {}
   f = open(filename)
   for line in f.readlines():
       line = line.strip()
       # if line[0] != '#' and  len(line) > 0: # crash!
       if len(line) > 0 and line[0] != '#' :
           fields = line.split(";")
           english = fields[source_field].strip()
           swedish = fields[target_field].strip()
           for english_word in english.split(","):
               for swedish_word in swedish.split(","):
                   d.setdefault(english_word.strip(),[]).append(swedish_word.strip())
   return d

english_to_swedish = load_dict("terms.csv", 1 , 0  )
swedish_to_english = load_dict("terms.csv",  0, 1)
print(english_to_swedish["distribution"])
print(swedish_to_english["stilguide"])

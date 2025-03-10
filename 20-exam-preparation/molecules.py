
# load the atom weights

def load_weights():
  weights = {}
  with open("atoms.txt") as f:
      for line in f:
          (atom,weight) = line.split()
          weights[atom] = float(weight)
  return weights

def m_mass(molecule):
    weights = load_weights()
    i = 0
    result = 0
    while i < len(molecule):
        atom = molecule[i]
        assert(not atom.isdigit())
        # print("i=",i,"  atom=",atom," len=",len(molecule),"w=",weights[atom])
        if i < len(molecule)-1 and molecule[i+1].isdigit():
            count = int(molecule[i+1])
            result = result + weights[atom] * count
            i = i+2
        else:
            result = result + weights[atom]
            i = i+1
    return result

def tester(molecule):
    print("The weight of",molecule,"is",m_mass(molecule))

 
tester("H")
tester("H2O")
tester("CH4")
tester("H2SO4")

aminoacid_dict = {"A": "ALA", "R": "ARG", "N": "ASN", "D": "ASP", "C": "CYS", "E": "GLU", "Q": "GLN", "G": "GLY", 
                  "H": "HIS", "I": "ILE", "L": "LEU", "K": "LYS", "M": "MET", "F": "PHE", "P": "PRO", "S": "SER",
                  "T": "THR", "W": "TRP", "Y": "TYR", "V": "VAL"}

# read from file .cif
with open("lab2\\dssp_structure_from_cif.blank", "r") as cif_file:
    cif_data = cif_file.readlines()
cif_data = [line.strip().split() for line in cif_data]
actual_structure = []
for line in cif_data:
    if len(line) > 1:
        actual_structure.append([line[2], line[3], line[4]])

# read from file .ss2
with open("lab2\\4ywo.ss2") as ss2_file:
    ss2_data = ss2_file.readlines()
ss2_data = [line.strip().split() for line in ss2_data]
predicted_structure = []
for line in ss2_data:
    if len(line) > 1:
        if line[0] != '#':
            predicted_structure.append([line[0], line[1], line[2]])

# change nomenclature to be unific between structures
for position in range(0, len(predicted_structure)):
    predicted_structure[position][1] = aminoacid_dict[predicted_structure[position][1]]
    if predicted_structure[position][2] == 'C':
        predicted_structure[position][2] = '.'
    if predicted_structure[position][2] == 'E':
        predicted_structure[position][2] = 'B'
for position in range(0, len(actual_structure)):
    if actual_structure[position][2] in {'H', 'G', 'I', 'P'}:
        actual_structure[position][2] = 'H'
    elif actual_structure[position][2] in {'B', 'E'}:
        actual_structure[position][2] = 'B'
    else:
        actual_structure[position][2] = '.'

# assume correct positioning
as_postioion = 0; compared = 0; matched = 0
for position in range(0, len(predicted_structure)):
    if predicted_structure[position][0] == actual_structure[as_postioion][0]:
        if predicted_structure[position][2] == actual_structure[as_postioion][2]:
            matched += 1
        as_postioion += 1; compared += 1
        if as_postioion >= len(actual_structure):
            break

# print out results
print(f"The SSI between predicted structure and actual structure is {(matched/compared)*100:.2f}%")
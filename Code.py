DNA = "ATCGACTCAGACGATATCATAGCAGAGAACGAATGCAGACAGATAAAGACTACGACAGAAAATACCCAA"
codons =  ""
i = 0
while (i < len(DNA)):
    codons += DNA[i:i+3]
    codons += " "
    i = i+3
print(codons)

newfile = open("Codons.csv","w") 
newfile.write(codons) 

#results can be found in working directory

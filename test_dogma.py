import dogma

print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))
print(dogma.translate('AUGCUACGCAUCGCUACGAUCGACUACGGCGCAUGCGGCGAUCGUACGUACGUACGUACG'))
print(dogma.translate('ATGAACGT'))
s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))
print(dogma.entropy(s))
 
print(dogma.avghydrobit('MRQSFSYAYRKDKKHETSVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIMRQSFSYVYIIIIIIIIIIIII'))

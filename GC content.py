
# coding: utf-8

# In[4]:

# This sequence is the first 100 nucleotides of the Influenza H1N1 Virus segment 8

flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'

# count "G"
G = flu_ns1_seq.count('G')

# count "C"
C = flu_ns1_seq.count('C')

# add GC content
GC_content = G + C

# add G content
G_content = G

# add C content
C_content = C

# get total length of DNA sequence
DNA_length = len(flu_ns1_seq)

# calculate the GC percentage
GC_percentage = GC_content / DNA_length * 100

#calculate the G percentage
G_percentage = G_content / DNA_length * 100

#calculate the C percentage
C_percentage = C_content / DNA_length * 100

# print result
print ('GC percentage:', GC_percentage,'%')

# print result
print ('G percentage:', G_percentage,'%')

# print result
print ('C percentage:', C_percentage,'%')



# In[ ]:




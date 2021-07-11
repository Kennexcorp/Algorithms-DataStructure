# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_v1(dna, P, Q):
    # write your code in Python 3.6
    
    necleotides = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4
    }

    y = x = 0
    dna_segments = []

    while x < len(P) and y < len(Q):

        start = P[x]
        end = Q[y]+1

        # remove duplicate dna sequence
        non_dup_dna = list(set(dna[start:end]))

        # Append non duplicate segment
        dna_segments.append(non_dup_dna)

        x += 1
        y += 1

    minimum_impact_values = []

    for segment in dna_segments:

        minimum = necleotides[segment[0]]

        for neclid in segment:
            
            if necleotides[neclid] < minimum:

                minimum = necleotides[neclid]

            if minimum == 1:

                break
        
        minimum_impact_values.append(minimum)

    return minimum_impact_values



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_v2(dna, P, Q):
    # write your code in Python 3.6
    
    necleotides = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4
    }

    necleotide_impact_values = []
    

    for necleotide in dna:

        value = necleotides[necleotide]

        necleotide_impact_values.append(value)

    x = y = 0
    minimum_impacts = []

    while x < len(P) and y < len(Q):

        start = P[x]
        end = Q[y]+1

        # remove duplicate dna sequence
        minimum = min(necleotide_impact_values[start:end])

        # Append non duplicate segment
        minimum_impacts.append(minimum)

        x += 1
        y += 1

    return minimum_impacts

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_v3(dna, P, Q):
    # write your code in Python 3.6
    necleotides = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4
    }

    x = y = 0
    minimum_impacts = []

    while x < len(P) and y < len(Q):

        start = P[x]
        end = Q[y]+1

        # create a list
        necleotide_impact_values = [necleotides[necleotide] for necleotide in dna[start: end]]
        minimum = min(necleotide_impact_values)

        # Append non duplicate segment
        minimum_impacts.append(minimum)

        x += 1
        y += 1

    return minimum_impacts

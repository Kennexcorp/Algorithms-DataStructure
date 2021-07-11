def numPlayers(k, scores):
    # Write your code here
    ranks = []
    scores.sort()
    scores = scores[::-1]
    newScores = list(set(scores))
    newScores = newScores[::-1]

    rank = 1
    for x in range(len(newScores)):
        occurrance = scores.count(newScores[x])
        for y in range(occurrance):
            ranks.append(rank)
        rank += occurrance
    
    playerCount = 0

    for x in range(len(scores)):
        if ranks[x] <= k and scores[x] != 0:
            playerCount += 1
    
    return playerCount



print(numPlayers(2, [0, 0, 0]))
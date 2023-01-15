import polybius as pb
import ngram_score as ns


def hillclimb(ciphertext, iterations = 100, step = 1, grams = 'english_quadgrams.txt'):
    best = None
    bestfit = -99999999
    for iter in range(iterations):
        parent = pb.polybius()
        fitness = ns.ngram_score(grams)
        parent.randomize()
        pfit = fitness.score(pb.Decode(parent,ciphertext))
        
        noImproveGens = 0
        while(noImproveGens < 3000):
            child = pb.polybius(parent)
            child.smallRnd(step)
            nfit = fitness.score(pb.Decode(child,ciphertext))
            if nfit > pfit:
                parent = child
                pfit = nfit
                noImproveGens = 0
            else:
                noImproveGens += 1
        print(iter, end=" (")
        print(pfit, end="): ")
        print([pb.Decode(parent,ciphertext), parent.alphabet])     
        if pfit > bestfit:
            best = parent
            bestfit = pfit
    if best != None:
        return [pb.Decode(best,ciphertext), best.alphabet]
    else:
        return ["_Invalid_", "_Invalid_"]
        
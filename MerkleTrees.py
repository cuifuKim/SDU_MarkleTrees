import math
import hashlib,json
import random

#1. Generate the MerkleTree
def CreatTree(DATA):
    l0 = len(DATA)
    Depth = math.ceil(math.log(l0, 2))+1
    MerkleTree = [[]]
    MerkleTree[0] = [(hashlib.sha256(i.encode())).hexdigest() for i in DATA]

    for i in range(1, Depth):
        l = math.floor(len(MerkleTree[i-1])/2)
        MerkleTree.append([(hashlib.sha256(MerkleTree[i-1][2*j].encode() + MerkleTree[i-1][2*j+1].encode())).hexdigest() for j in range(0, l)])
        if len(MerkleTree[i-1])%2 == 1:
            MerkleTree[i].append(MerkleTree[i-1][-1])

    return MerkleTree

#2.Generate 100k messages
def GenerateMessages():
    return [''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789',5)) for i in range(0,100000)]

#3.Show the evidence that a leafnode is in the tree
def ShowEvidence(m,Tree):
    h = (hashlib.sha256(m.encode())).hexdigest()
    try:
        n=Tree[0].index(h)
    except:
        print("The leafnode is not in the tree")
    Depth = len(Tree)
    Evidence = []
    for d in range(0,Depth):
        if n%2==0:
            if n == len(Tree[d]) - 1:
                pass
            else:
                Evidence.append([Tree[d][n],Tree[d][n+1]])
        else:
            Evidence.append([Tree[d][n-1], Tree[d][n]])
        n = math.floor(n/2)
    Evidence.append([Tree[-1][0]])
    return Evidence

#4.Verify the proof
def Verify(m,Evidence,Top):
    h = (hashlib.sha256(m.encode())).hexdigest()
    if h != Evidence[0][0] and h != Evidence[0][1]:
        return False
    if Evidence[-1][0] != Top:
        return False
    Depth = len(Evidence)
    for i in range(0,Depth-1):
        node = (hashlib.sha256(Evidence[i][0].encode() + Evidence[i][1].encode())).hexdigest()
        if node != Evidence[i+1][0] and node != Evidence[i+1][1]:
            return False
    if (hashlib.sha256(Evidence[-2][0].encode() + Evidence[-2][1].encode())).hexdigest() != Evidence[-1][0]:
        return False

    return True

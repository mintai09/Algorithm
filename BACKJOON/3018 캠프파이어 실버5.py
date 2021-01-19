N = int(input())
E = int(input())

S = [ []for _ in range(N+1)]
song = 0

for i in range(E):
    P = list(map(int,input().split()))
    P.pop(0)
    if 1 in P:
        for i in P:
            S[i].append(song)
        song += 1
    else:
        songs = []
        for i in P:
            for s in S[i]:
                if s not in songs:
                    songs.append(s)
                    
        for i in P:
            S[i] = songs[:]
            

for i in range(1,len(S)):
    if len(S[i]) == len(S[1]):
        print(i)
    

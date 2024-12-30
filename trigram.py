import torch

words = open('names.txt').read().splitlines()

#print(words[:10])

b = {}
for w in words:
  chs = ['.'] + list(w) + ['.']
  for ch1, ch2, ch3 in zip(chs, chs[1:], chs[2:]):
      #print(ch1, ch2, ch3)
      trigram = (ch1, ch2, ch3)
      b[trigram] = b.get(trigram, 0) + 1

print(sorted(b.items(), key = lambda kv: -kv[1]))

N = torch.zeros((27, 27, 27), dtype=torch.int32)

chars = sorted(list(set(''.join(words))))
stoi = {s:i+1 for i,s in enumerate(chars)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2, ch3 in zip(chs, chs[1:], chs[2:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        ix3 = stoi[ch3]
        N[ix1, ix2, ix3] += 1

print(N.shape)
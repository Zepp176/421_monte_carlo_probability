import numpy as np
import matplotlib.pyplot as plt
    
def play_421(speak=False):
    de = [False, False, False]
    
    for i in range(3):
        nb = 3 - np.sum(de)
        if speak:
            print("essai {}: {} lancer(s)".format(i+1, nb))
        
        for j in range(nb):
            result = np.random.randint(1, 7)
            if speak:
                print("dé 1: {}".format(result))
            
            if result == 1:
                de[0] = True
            if result == 2:
                de[1] = True
            if result == 4:
                de[2] = True
            
            if sum(de) == 3:
                break
    
    if speak:
        if sum(de) == 3:
            print("\n421!")
        else:
            print("perdu...")
    
    if sum(de) == 3:
        return True
    else:
        return False
            

count = 0
n_iter = 100000
result = np.empty(n_iter)

result[0] = play_421()

for i in range(1, n_iter):
    result[i] = result[i-1] + play_421()
for i in range(n_iter):
    result[i] /= (i+1)

print("{} iterations.".format(n_iter))
print("probability to win \"421\": {}%".format(count/n_iter*100))

plt.figure(figsize=(7,5))
plt.grid()
plt.title("probability to win 421 game")
plt.xlabel("iteration")
plt.ylabel("probability of win [%]")
plt.plot(result*100)
plt.show()

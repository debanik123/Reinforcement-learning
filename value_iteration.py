
# coding: utf-8

# In[3]:


reward = [0 for _ in range(101)]
print(reward)


# In[4]:


reward[100] = 1


# In[6]:


print(reward)


# In[30]:


gamma = 1
p = 0.4
num_states = 100

reward  = [0 for i in range(101)]
reward[100] = 1

theta = 0.00000001

value = [0 for i in range(101)]
policy = [0 for i in range(101)]



def reinforcement_learning():
    
    delta = 1
    
    while delta > theta:
        delta = 0
        
        
        for i in range(1, num_states):
            oldvalue = value[i]
            
            bellman_equation(i)
            
            diff = abs(oldvalue - value[i])
            delta = max(delta,diff)
    print(value)
def bellman_equation(num):
    
    optimal_value = 0 #initialize the optimal value 
    
    for bet in range(0,min(num, 100 - num)+1):
        win = num + bet
        loss = num - bet
        
        sum = p*(reward[win] + gamma*value[win]) + (1-p)*(reward[loss] + gamma*value[loss])
        
        if sum>optimal_value:
            
            optimal_value = sum
            value[num] = sum
            policy[num] = bet
reinforcement_learning()  


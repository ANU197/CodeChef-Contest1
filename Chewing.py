"""
Zonal Computing Olympiad 2013, 10 Nov 2012

Hobbes has challenged Calvin to display his chewing skills and chew two different types of Chewing
Magazine's Diabolic Jawlockers chewing gum at the same time. Being a generous sort of tiger, Hobbes allows Calvin to pick the two types of gum he will chew.


Each type of chewing gum has a hardness quotient, given by a non-negative integer.
If Calvin chews two pieces of gum at the same time, the total hardness quotient is the sum of the individual hardness quotients of the two pieces of gum.


Calvin knows that he cannot chew any gum combination whose hardness quotient is K or more.
 He is given a list with the hardness quotient of each type of gum in the Diabolic Jawlockers collection.
 How many different pairs of chewing gum can Calvin choose from so that the total hardness quotient remains strictly below his hardness limit K?


For instance, suppose there are 7 types of chewing gum as follows:
 Chewing gum type 	 1 	 2 	 3 	 4 	 5 	 6 	 7
 Hardness quotient 	 10 	 1 	 3 	 1 	 5 	 5 	 0

If Calvin's hardness limit is 4, there are 4 possible pairs he can choose: type 2 and 7 (1+0 < 4), type 3 and 7 (3+0 < 4), type 2 and 4 (1+1 < 4) and type 4 and 7 (1+0 < 4).


Input format
Line 1 : Two space separated integers N and K, where N is the number of different types of chewing gum and K is Calvin's hardness limit.

Line 2: N space separated non-negative integers, which are the hardness quotients of each of the N types of chewing gum.


Output format
The output consists of a single non-negative integer, the number of pairs of chewing gum with total hardness quotient strictly less than K.


Sample Input
7 4
10 1 3 1 5 5 0

Sample Output
4


"""


x = list(map(int, input().strip().split()))
y = list(map(int, input().strip().split()))
count = 0
y.sort()
n = x[0]
k = x[1]

for i in range(n):
    for j in range(i+1, n):
        if (y[i]+y[j] < k):
            count = count + 1


print(count)

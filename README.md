The project addresses finding the lowest floor from which a ball will break when dropped in a building with n floors, using k available balls. 
The basic assumptions include the fact that a ball breaks if it falls from a certain floor and that subsequent drops do not affect the strength of the glass. 
To solve this problem, we used a Dynamic Programming approach. 
The checking_number function calculates the minimum number of trials required using a two-dimensional table that describes solutions to the problem of ball breakage for different numbers of balls and floors. 
When the exact floor where the ball will break is unknown, the index_floor function enables a binary search to find the first floor where the ball breaks from a list of potential floors. 
Finally, the index_first_floor function provides an optimal solution for the case k=2, using a closed-form mathematical formula to estimate the minimum number of trials required. 
The goal is to simplify finding the solution with minimal trials and to handle optimization problems in cases of a limited number of balls.

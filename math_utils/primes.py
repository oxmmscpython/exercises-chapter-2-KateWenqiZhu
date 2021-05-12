def isprime(n):
  if n==1: return False    
  else:
        for x in range(2, n):
          if n % x == 0:
              return False
              break
        else:
              return True      

    
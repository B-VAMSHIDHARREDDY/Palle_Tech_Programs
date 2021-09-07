"""
assign the parameter values in argument stage
function(a,b):
    return a,b
function(b=20,a=100) # assign values by key based
"""
print("------------------ Example 1 -----------------")
def fun(a,b):
    print(a,b)
fun(b = 200,a = 300)
print("------------------ Example 2 -----------------")
def fun(a,b,c,d):
    print(a,b,c,d)

fun(10,c=30,b=20,d=10)
fun(20,10,30,d=50)
fun(d=10,a=20,c=40,b=70)
print("------------------ Example 3 -----------------")
def wish(name,msg):
    print("Hello",name,msg)
wish(name="Vamshi",msg="Good Morning")
wish(msg="Good Morning",name="Vamshi")
# wish(name="Vamshi","Good Morning") ==>invalid
from cyberpythonevaluator import CyberPythonEvaluator

cpe = CyberPythonEvaluator()

challenge = cpe.get_challenge(5)

print "Description", challenge.description #Create a function which receives a number and returns False if the number is odd, and True if the number is even.
#print "Example Input", challenge.example_input
#print "Example Output", challenge.example_output

def solution(n):
    if n % 2 == 0:
        return True
    else:
        return False







#print challenge.validate(solution, debug=True)
print challenge.validate(solution, debug=True)

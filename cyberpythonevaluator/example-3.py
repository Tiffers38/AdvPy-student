from cyberpythonevaluator import CyberPythonEvaluator

cpe = CyberPythonEvaluator()

challenge = cpe.get_challenge(3)

print "Description", challenge.description #Create a function which receives a number and returns the number of prime factors.
#print "Example Input", challenge.example_input
#print "Example Output", challenge.example_output

def solution(n):

#number is greater than 1
#







#print challenge.validate(solution, debug=True)
print challenge.validate(solution, debug=True)

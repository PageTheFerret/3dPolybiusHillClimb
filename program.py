import hillclimb as hc
import patterns
import polybius as pb


print("Starting...")
result = hc.hillclimb(patterns.Allt, 1000)
print("Result:")
print(result)

print("Done!")
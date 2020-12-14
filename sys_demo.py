import sys

arguments = sys.argv
print(f"we received the following arguments:")

for arg in arguments:
    print(f"- {arg}")

    print(f"We are running on a '{sys.platform}' machine")

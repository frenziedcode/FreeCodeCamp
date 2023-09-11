str = "X-DSPAM-Confidence:0.8475"

position = str.find(':')
partPosition = str[position + 1:]
float(partPosition)

print(partPosition)


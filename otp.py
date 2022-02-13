
import math, random
def generateOTP() :


	string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	OTP = ""
	length = len(string)
	for i in range(6) :
		OTP += string[math.floor(random.random() * length)]

	return OTP

if __name__ == "__main__" :
	
	print("OTP of length 6:", generateOTP())

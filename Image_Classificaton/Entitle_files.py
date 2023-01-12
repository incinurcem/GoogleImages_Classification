import os




#Naming and downloading photos according to the order in the desired name

def main():

	folder = "/images/dataset/snowy"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"snowy{str(count)}.jpg"
		src = f"{folder}/{filename}"
		dst = f"{folder}/{dst}"
		os.rename(src, dst)


if __name__ == '__main__':
	
	main()

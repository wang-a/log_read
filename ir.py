#encoding:utf-8
#python 2.7
import os
import glob
import sys

def main() :
	print	"Hwang YunAh's IR-8 Assignment"
	if len(sys.argv) != 3 : #인자 갯수를 잘못 넣었을 떄 사용법 출력
		print "Usage : python ir.py <PATH> <CODE>";
		print "<PATH> : Log files directory"
		print "<CODE> : 1 > Attack file path / 2 > Attacker IP / 3 > All"
		return

	logPath = sys.argv[1]
	num = sys.argv[2]
	
	logs = []

	for p in glob.iglob(logPath) : # 폴더의 로그데이터를 다 읽어옴
		for (path, dir, files) in os.walk(p):
		    for filename in files:
		        ext = os.path.splitext(filename)[-1]
		        if ext == '.log':
		            logs.append("%s\\%s" % (path, filename))
	text = ""		        

	f = open("POST_METHOD_LOG.txt","w") #POST 메소드를 사용하는 로그 기록들을 뽑아 파일로 저장한다.

	for log in logs :# 해당 로그 기록을 한줄씩 뽑음.
		for line in open(log, "r").readlines() :
			if "POST" in line :
				f.write(line + "\n") #파일로 저장

	f.close()

	f = open("POST_METHOD_LOG.txt","r")
	f2 = open("200OK_LOG.txt", "w")	
	for line in f.readlines() :
		if "200" in line :
			cut = line.split(" ")
			f2.write(cut[5]+" "+cut[9]+" "+cut[11] + "\n") # Stem, 접속자IP, 응답코드를 저장 
	f2.close()
	f.close()

	os.remove("POST_METHOD_LOG.txt")

	arr = []
	f = open("200OK_LOG.txt")
	for line in f.readlines() : #cer 확장자가 들어가는 파일을 추출
		if ".cer" in line : 
			if line not in arr :
				arr.append(line)
	f.close()
	os.remove("200OK_LOG.txt")

	f2 = open("Attacker_info.txt","w")
	for a in arr :
		f2.write(a + "\n")
	f2.close()

	f = open("Attacker_info.txt","r") #두번째 인자 값에 맞게 공격자 정보 출력
	arr = []
	if num == '1' : 
		for line in f.readlines() : 
			try : arr.append(line.split(" ")[0])
			except : pass
	elif num == '2' : 
		for line in f.readlines() : 
			try : arr.append(line.split(" ")[1])
			except : pass
	elif num == '3' : 
		for line in f.readlines() : 
			try : arr.append(line.split(" ")[0] +" "+ line.split(" ")[1])
			except : pass
	f.close()

	arr = list(set(arr))
	for l in arr :
		print l

if __name__ == '__main__':
	main()
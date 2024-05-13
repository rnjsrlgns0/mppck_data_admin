#구동가상환경 = admin
import os
import shutil
import pandas as pd
import zipfile
import time

#group1 법정동
def path_finder_group1():
	# 1. 한곳에 전국데이터 압축해제
	rltv_pth = '../layer_group_1_juso/'
	zip_names = os.listdir(rltv_pth)
	for i in zip_names:
		if i != '.DS_Store':
			zip_file_path = f'{rltv_pth}{i}'
			extracted_folder_path = f'{rltv_pth}전국/'
			with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(extracted_folder_path)
	folder_names = os.listdir(f'{rltv_pth}전국')
	for i in folder_names:
		file_names = os.listdir(f'{rltv_pth}전국/{i}')
		for j in file_names:
			path_before = f'{rltv_pth}전국/{i}/{j}'
			path_after = f'{rltv_pth}전국/{i}_{j}'
			shutil.move(path_before, path_after)
		os.rmdir(f'{rltv_pth}전국/{i}')
		li_table = ['TL_SCCO_EMD','TL_SCCO_LI','TL_SCCO_CTPRVN','TL_SCCO_SIG']
	for i in li_table:
		os.mkdir(f'{rltv_pth}{i}')
	for j in li_table:
		file_names = os.listdir(f'{rltv_pth}전국')
		for i in file_names:
			if j in i:
				path_before = f'{rltv_pth}전국/{i}'
				path_after = f'{rltv_pth}{j}/{i}'
				shutil.move(path_before,path_after)
	shutil.rmtree(f'{rltv_pth}전국')    
	# 3.몰려있는 파일들을 다시 지역 별 폴더로 나누기
	for i in li_table:
		file_names = os.listdir(f'{rltv_pth}{i}') # 폴더 안에 있는 모든 파일 이름
		li_fldr = []
		for j in file_names:
			n = '_'.join([j.split('_')[0]]) # 레이어 종류 + 지역코드
			li_fldr.append(f'{rltv_pth}{i}/{n}') #디렉터리 리스트 생성
		li_fldr = list(set(li_fldr)) #중복값 제거 
		for k in li_fldr:
			path_before = f'{rltv_pth}{i}'
			os.mkdir(k)
			for l in file_names:
				if (k.split('/')[-1].split('_')[-1] in l) &('DS_Store' not in k): #지역코드가 파일명에 들어있으면 
					shutil.move('/'.join([path_before,l]), '/'.join([k, l]))

#group2 연속지적도
def path_finder_group2():
	zip_names = os.listdir('../layer_group_2/')
	for i in zip_names:
		if i != '.DS_Store':
			zip_file_path = f'../layer_group_2/{i}'
			extracted_folder_path = f'../layer_group_2/전국/{i[:-4]}'
			with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(extracted_folder_path)
			contents = os.listdir(extracted_folder_path)
			p = os.path.join(f'../layer_group_2/전국/{i[:-4]}', contents[-1])
			os.remove(zip_file_path) #zip파일 삭제

#group3 지하철, 철도
def path_finder_group3_sttn():
	#상대경로
	rltv_pth = '../layer_group_3_sttn/'
	# 1. 한곳에 전국데이터 압축해제
	zip_names = os.listdir(rltv_pth)
	for i in zip_names:
		if i != '.DS_Store':
			zip_file_path = f'{rltv_pth}{i}'
			extracted_folder_path = f'{rltv_pth}전국/'
			with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(extracted_folder_path)
	li_table = ['TL_SPSB_STATN','TL_SPSB_RLWAY','TL_SPSB_ENTRC', #폴리곤
				'TL_SPRL_STATN','TL_SPRL_RLWAY'] #라인
	for i in li_table:
		os.mkdir(f'{rltv_pth}{i}')

	# 2. 같은종류의 파일끼리 한 곳에 몰아놓기
	file_names = os.listdir(f'{rltv_pth}전국')
	# print(len(file_names))
	# s = pd.Series(data = file_names)
	# s.str.split('.').str[3].unique()
	for i in file_names:
		if (i != '.DS_Store')&(i.split('.')[3] in li_table):
			p = i.split('.')[3]
			path_before = f'{rltv_pth}전국/{i}'
			path_after = f'{rltv_pth}{p}/{i}'
			shutil.move(path_before,path_after)
	shutil.rmtree('../layer_group_3_sttn/전국')
	#--------------------------------여기까지 정상

	# 3.몰려있는 파일들을 다시 지역 별 폴더로 나누기
	for i in li_table:
		file_names = os.listdir(f'{rltv_pth}{i}') # 폴더 안에 있는 모든 파일 이름
		li_fldr = []
		for j in file_names:
			n = '_'.join([j.split('.')[3], j.split('.')[4]]) # 레이어 종류 + 지역코드
			li_fldr.append(f'{rltv_pth}{i}/{n}') #디렉터리 리스트 생성
		li_fldr = list(set(li_fldr)) #중복값 제거 
		for k in li_fldr:
			path_before = f'{rltv_pth}{i}'
			os.mkdir(k)
			for l in file_names:
				if (k.split('/')[-1].split('_')[-1] in l) &('DS_Store' not in k): #지역코드가 파일명에 들어있으면 
					shutil.move('/'.join([path_before,l]), '/'.join([k, l]))
		time.sleep(5)	

#group3 도로
def path_finder_group3_road():
	# 1. 한곳에 전국데이터 압축해제
	rltv_pth = '../layer_group_3_road/'
	zip_names = os.listdir(rltv_pth)
	for i in zip_names:
		if i != '.DS_Store':
			zip_file_path = f'{rltv_pth}{i}'
			extracted_folder_path = f'{rltv_pth}전국/'
			with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(extracted_folder_path)
	fldr_names = os.listdir(extracted_folder_path)
	print(fldr_names)
	for j in fldr_names: #j는 지역코드 폴더
		k = ''.join([extracted_folder_path,j]) #shp들이 들어있는 경로
		# print(k)
		file_names = os.listdir(k)
		for l in file_names:
			n = '/'.join([extracted_folder_path,'.'.join([j,l])])
			# print(n)
			shutil.move('/'.join([k,l]),n)
		shutil.rmtree(k)
	li_table = ['TL_SPRD_INTRVL','TL_SPRD_MANAGE','TL_SPRD_RW']
	for i in li_table:
		os.mkdir(f'{rltv_pth}{i}')

	# 2. 같은종류의 파일끼리 한 곳에 몰아놓기
	file_names = os.listdir(f'{rltv_pth}전국')
	for i in file_names:
		if (i != '.DS_Store')&(i.split('.')[1] in li_table):
			p = i.split('.')[1]
			# print(p)
			path_before = f'{rltv_pth}전국/{i}'
			path_after = f'{rltv_pth}{p}/{i}'
			# print(path_after)
			shutil.move(path_before,path_after)
	shutil.rmtree('../layer_group_3_road/전국')

	# 3.몰려있는 파일들을 다시 지역 별 폴더로 나누기
	for i in li_table:
		file_names = os.listdir(f'{rltv_pth}{i}') # 폴더 안에 있는 모든 파일 이름
		li_fldr = []
		for j in file_names:
			n = '.'.join([j.split('.')[1], j.split('.')[0]]) # 레이어 종류 + 지역코드
			li_fldr.append(f'{rltv_pth}{i}/{n}') #디렉터리 리스트 생성
		li_fldr = list(set(li_fldr)) #중복값 제거 
		for k in li_fldr:
			path_before = f'{rltv_pth}{i}'
			os.mkdir(k)
			for l in file_names:
				if (k.split('/')[-1].split('.')[-1] in l) &('DS_Store' not in k): #지역코드가 파일명에 들어있으면 
					shutil.move('/'.join([path_before,l]), '/'.join([k, l]))

#group4 도로명 주소
def path_finder_group4_road():
	rltv_pth = '../layer_group_4_road/'
	zip_names = os.listdir(rltv_pth)
	for i in zip_names:
		if i != '.DS_Store':
			zip_file_path = f'../layer_group_4_road/{i}'
			extracted_folder_path = f'../layer_group_4_road/전국/'
			with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(extracted_folder_path)
	li_table = ['TL_SGCO_RNADR_MST','TL_SPBD_ENTRC','TL_SPOT_CNTC']
	for i in li_table:
		os.mkdir(f'../layer_group_4_road/{i}')
	file_names = os.listdir('../layer_group_4_road/전국')
	# s = pd.Series(data = file_names)
	# s.str.split('.').str[3].unique()
	for i in file_names:
		if (i != '.DS_Store')&(i.split('.')[3] in li_table):
			p = i.split('.')[3]
			path_before = f'../layer_group_4_road/전국/{i}'
			path_after = f'../layer_group_4_road/{p}/{i}'
			shutil.move(path_before,path_after)
	shutil.rmtree('../layer_group_4_road/전국')
	#--------------------------------여기까지 정상 여기부터 지역별로 나누기
	for i in li_table:
		file_names = os.listdir(f'{rltv_pth}{i}') # 폴더 안에 있는 모든 파일 이름
		li_fldr = []
		for j in file_names:
			n = '_'.join([j.split('.')[3], j.split('.')[4]]) # 레이어 종류 + 지역코드
			li_fldr.append(f'{rltv_pth}{i}/{n}') #디렉터리 리스트 생성
		li_fldr = list(set(li_fldr)) #중복값 제거 
		for k in li_fldr:
			path_before = f'{rltv_pth}{i}'
			os.mkdir(k)
			for l in file_names:
				if (k.split('/')[-1].split('_')[-1] in l) &('DS_Store' not in k): #지역코드가 파일명에 들어있으면 
					shutil.move('/'.join([path_before,l]), '/'.join([k, l]))

#group4 GIS 건통
def path_finder_group4_con():
    # 다운받은 zip파일 해제 및 파일 이동
    zip_names = [f for f in os.listdir('../layer_group_4_con') if f != '.DS_Store']
    os.mkdir('../layer_group_4_con/전국')
    for zip_name in zip_names:
        zip_file_path = f'../layer_group_4_con/{zip_name}'
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall('../layer_group_4_con/전국')

    # 파일명 수정 및 디렉토리 생성
    li_file = os.listdir('../layer_group_4_con/전국')
    unique_files = set(f.split('.')[0] for f in li_file)
    for file_name in unique_files:
        modified_name = file_name.replace('_52_', '_45_').replace('_51_', '_42_')
        os.mkdir(f'../layer_group_4_con/{modified_name}')

    # 파일 이동
    for file in li_file:
        path_before = f'../layer_group_4_con/전국/{file}'
        modified_name = file.split('.')[0].replace('_52_', '_45_').replace('_51_', '_42_')
        path_after = f'../layer_group_4_con/{modified_name}'
        shutil.move(path_before, path_after)

    shutil.rmtree('../layer_group_4_con/전국')

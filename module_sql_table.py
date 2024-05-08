import time
import datetime
date_1 = datetime.datetime.today().date()
time_1 = datetime.datetime.now().strftime("%H:%M:%S")


#layer_group_1_juso
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
dic = {}
dic['tl_scco_ctprvn_new'] = f'''CREATE TABLE gfdata.tl_scco_ctprvn_new (
	gid int4 DEFAULT nextval('gfdata.tl_scco_ctprvn_new'::regclass) NOT NULL,
	ctprvn_cd varchar(2) NULL,
	ctp_eng_nm varchar(40) NULL,
	ctp_kor_nm varchar(40) NULL,
	geom public.geometry(multipolygon, 5179) NULL,
	CONSTRAINT tl_scco_ctprvn_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
)
TABLESPACE gf
;
CREATE INDEX tl_scco_ctprvn_new_geom_idx_{time_1[-2:]} ON gfdata.tl_scco_ctprvn_new USING gist (geom);'''

dic['tl_scco_emd_new'] = f'''CREATE TABLE gfdata.tl_scco_emd_new (
	gid int4 DEFAULT nextval('gfdata.tl_scco_emd_new'::regclass) NOT NULL,
	emd_cd varchar(10) NULL,
	emd_eng_nm varchar(40) NULL,
	emd_kor_nm varchar(40) NULL,
	geom public.geometry(multipolygon, 5179) NULL,
	CONSTRAINT tl_scco_emd_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
)
TABLESPACE gf
;
CREATE INDEX tl_scco_emd_new_geom_idx_{time_1[-2:]} ON gfdata.tl_scco_emd_new USING gist (geom);'''

dic['tl_scco_li_new'] =f'''CREATE TABLE gfdata.tl_scco_li_new (
	gid int4 DEFAULT nextval('gfdata.tl_scco_li_new'::regclass) NOT NULL,
	li_cd varchar(10) NULL,
	li_eng_nm varchar(40) NULL,
	li_kor_nm varchar(40) NULL,
	geom public.geometry(multipolygon, 5179) NULL,
	CONSTRAINT tl_scco_li_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
)
TABLESPACE gf
;
CREATE INDEX tl_scco_li_new_geom_idx_{time_1[-2:]} ON gfdata.tl_scco_li_new USING gist (geom);'''

dic['tl_scco_sig_new'] = f'''CREATE TABLE gfdata.tl_scco_sig_new (
	gid int4 DEFAULT nextval('gfdata.tl_scco_sig_new'::regclass) NOT NULL,
	sig_cd varchar(5) NULL,
	sig_eng_nm varchar(40) NULL,
	sig_kor_nm varchar(40) NULL,
	geom public.geometry(multipolygon, 5179) NULL,
	CONSTRAINT tl_scco_sig_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
)
TABLESPACE gf
;
CREATE INDEX tl_scco_sig_new_geom_idx_{time_1[-2:]} ON gfdata.tl_scco_sig_new USING gist (geom);'''


#layer_group_1_sgis
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
dic['z_sop_bnd_sido_pg_new'] = f'''
CREATE TABLE gfdata.z_sop_bnd_sido_pg_new (
	gid int4 DEFAULT nextval('gfdata.z_sop_bnd_sido_pg_new_{time_1[-2:]}_gid_seq'::regclass) NOT NULL,
	base_date varchar(8) NULL,
	sido_cd varchar(2) NULL,
	sido_nm varchar(50) NULL,
	admint_cd varchar(254) NULL,
	geom public.geometry(multipolygon, 5174) NULL,
	CONSTRAINT z_sop_bnd_sido_pg_new_{time_1[-2:]}_pkey PRIMARY KEY (gid)
);
CREATE INDEX z_sop_bnd_sido_pg_new_{time_1[-2:]}_geom_idx ON gfdata.z_sop_bnd_sido_pg_new USING gist (geom);
'''

dic['z_sop_bnd_adm_dong_pg_new'] = f''' 
CREATE TABLE gfdata.z_sop_bnd_adm_dong_pg_new (
	gid int4 DEFAULT nextval('gfdata.z_sop_bnd_adm_dong_pg_new_{time_1[-2:]}_gid_seq'::regclass) NOT NULL,
	base_date varchar(8) NULL,
	adm_nm varchar(50) NULL,
	adm_cd varchar(8) NULL,
	admint_cd varchar(254) NULL,
	geom public.geometry(multipolygon, 5174) NULL,
	CONSTRAINT z_sop_bnd_adm_dong_pg_new_{time_1[-2:]}_pkey PRIMARY KEY (gid)
);
CREATE INDEX z_sop_bnd_adm_dong_pg_new_{time_1[-2:]}_geom_idx ON gfdata.z_sop_bnd_adm_dong_pg_new USING gist (geom);
'''

dic['z_sop_bnd_sigungu_new'] = f'''
CREATE TABLE gfdata.z_sop_bnd_sido_pg_new (
	gid int4 DEFAULT nextval('gfdata.z_sop_bnd_sido_pg_new_{time_1[-2:]}_gid_seq'::regclass) NOT NULL,
	base_date varchar(8) NULL,
	sido_cd varchar(2) NULL,
	sido_nm varchar(50) NULL,
	admint_cd varchar(254) NULL,
	geom public.geometry(multipolygon, 5174) NULL,
	CONSTRAINT z_sop_bnd_sido_pg_new_{time_1[-2:]}_pkey PRIMARY KEY (gid)
);
CREATE INDEX z_sop_bnd_sido_pg_new_{time_1[-2:]}_geom_idx ON gfdata.z_sop_bnd_sido_pg_new USING gist (geom); 
'''

dic['lsmd_cont_ldreg_new'] = f'''CREATE TABLE gfdata.lsmd_cont_ldreg_new (
	sgg_oid int4 NULL,
	jibun varchar(100) NULL,
	bchk varchar(1) NULL,
	pnu varchar(19) NULL,
	col_adm_se varchar(5) NULL,
	geom public.geometry(multipolygon, 5186) NULL
)partition by range(pnu);'''

#layer_group_3 도로교통 - 지하철
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# 'tl_spsb_entrc_new'------------------------------------------------
dic['tl_spsb_entrc_new'] = f'''CREATE TABLE gfdata.tl_spsb_entrc_new (
	gid int4 DEFAULT nextval('gfdata.tl_spsb_entrc_new'::regclass) NOT NULL,
	sig_cd varchar(5) NULL,
	sub_ent_sn float8 NULL,
	entrc_no int4 NULL,
	opert_de varchar(14) NULL,
	geom public.geometry(point, 5186) NULL,
	CONSTRAINT tl_spsb_entrc_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_spsb_entrc_new_geom_idx_{time_1[-2:]} ON gfdata.tl_spsb_entrc_new USING gist (geom);'''

# 'tl_sprl_statn_new'------------------------------------------------
dic['tl_sprl_statn_new'] = f'''CREATE TABLE gfdata.tl_sprl_statn_new (
    gid int4 DEFAULT nextval('gfdata.tl_sprl_statn_new'::regclass) NOT NULL,
    sig_cd varchar(5) NULL,
    rlr_sta_sn float8 NULL,
    kor_sta_nm varchar(40) NULL,
    opert_de varchar(14) NULL,
    geom public.geometry(multipolygon, 5186) NULL,
    CONSTRAINT tl_sprl_statn_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_sprl_statn_new_geom_idx_{time_1[-2:]} ON gfdata.tl_sprl_statn_new USING gist (geom);'''

# 'tl_sprl_rlway_new'------------------------------------------------
dic['tl_sprl_rlway_new'] = f'''CREATE TABLE gfdata.tl_sprl_rlway_new (
	gid int4 DEFAULT nextval('gfdata.tl_sprl_rlway_new'::regclass) NOT NULL,
	sig_cd varchar(5) NULL,
	rlr_rlw_sn float8 NULL,
	kor_rlr_nm varchar(40) NULL,
	opert_de varchar(14) NULL,
	geom public.geometry(multilinestring, 5186) NULL,
	CONSTRAINT tl_sprl_rlway_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_sprl_rlway_new_geom_idx_{time_1[-2:]} ON gfdata.tl_sprl_rlway_new USING gist (geom);
'''
# 'tl_spsb_statn_new'------------------------------------------------
# 얘는 운영 DB에도 5179로 되어있음. but 맵픽에서 잘 나옴...?
dic['tl_spsb_statn_new'] = f'''CREATE TABLE gfdata.tl_spsb_statn_new (
	gid int4 DEFAULT nextval('gfdata.tl_spsb_statn_new'::regclass) NOT NULL,
	sig_cd varchar(5) NULL,
	sub_sta_sn float8 NULL,
	kor_sub_nm varchar(40) NULL,
	opert_de varchar(14) NULL,
	geom public.geometry(multipolygon, 5179) NULL,
	CONSTRAINT tl_spsb_statn_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_spsb_statn_new_geom_idx_{time_1[-2:]} ON gfdata.tl_spsb_statn_new USING gist (geom); 
'''
# 'tl_spsb_rlway_new'------------------------------------------------
# 얘는 운영 DB에도 5179로 되어있음. but 맵픽에서 잘 나옴...?
dic['tl_spsb_rlway_new'] = f'''CREATE TABLE gfdata.tl_spsb_rlway_new (
	gid int4 DEFAULT nextval('gfdata.tl_spsb_rlway_new'::regclass) NOT NULL,
	sig_cd varchar(5) NULL,
	sub_rlw_sn float8 NULL,
	kor_sbr_nm varchar(40) NULL,
	opert_de varchar(14) NULL,
	geom public.geometry(multilinestring, 5186) NULL,
	CONSTRAINT tl_spsb_rlway_new_2024_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_spsb_rlway_new_geom_idx_{time_1[-2:]} ON gfdata.tl_spsb_rlway_new USING gist (geom);
'''

#layer_group_3 도로교통 - 도로
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# 'tl_sprd_intrvl'------------------------------------------------
dic['tl_sprd_intrvl_new'] = f'''CREATE TABLE gfdata.tl_sprd_intrvl_new (
	gid int4 DEFAULT nextval('gfdata.tl_sprd_intrvl_new'::regclass) NOT NULL,
	bsi_int_sn float8 NULL,
	eve_bsi_mn int4 NULL,
	eve_bsi_sl int4 NULL,
	odd_bsi_mn int4 NULL,
	odd_bsi_sl int4 NULL,
	opert_de varchar(14) NULL,
	rds_man_no float8 NULL,
	sig_cd varchar(5) NULL,
	geom public.geometry(multilinestring, 5186) NULL,
	CONSTRAINT tl_sprd_intrvl_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_sprd_intrvl_new_geom_idx_{time_1[-2:]} ON gfdata.tl_sprd_intrvl_new USING gist (geom);
'''

# 'tl_sprd_intrvl'------------------------------------------------
dic['tl_sprd_manage_new'] = f'''CREATE TABLE gfdata.tl_sprd_manage_new (
	gid serial4 NOT NULL,
	alwnc_de varchar(8) NULL,
	alwnc_resn varchar(254) NULL,
	bsi_int varchar(5) NULL,
	eng_rn varchar(80) NULL,
	mvmn_de varchar(8) NULL,
	mvmn_resn varchar(254) NULL,
	mvm_res_cd varchar(10) NULL,
	ntfc_de varchar(8) NULL,
	opert_de varchar(14) NULL,
	rbp_cn varchar(80) NULL,
	rds_dpn_se varchar(1) NULL,
	rds_man_no float8 NULL,
	rep_cn varchar(80) NULL,
	rn varchar(80) NULL,
	rn_cd varchar(7) NULL,
	road_bt float8 NULL,
	road_lt float8 NULL,
	roa_cls_se varchar(2) NULL,
	sig_cd varchar(5) NULL,
	wdr_rd_cd varchar(10) NULL,
	geom public.geometry(multilinestring, 5186) NULL,
	CONSTRAINT tl_sprd_manage_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_sprd_manage_new_geom_idx_{time_1[-2:]} ON gfdata.tl_sprd_manage_new USING gist (geom);
'''

# 'tl_sprd_rw'------------------------------------------------
dic['tl_sprd_rw_new'] = f'''CREATE TABLE gfdata.tl_sprd_rw_new (
	gid int4 DEFAULT nextval('gfdata.tl_sprd_rw_new'::regclass) NOT NULL,
	opert_de varchar(14) NULL,
	rw_sn float8 NULL,
	sig_cd varchar(5) NULL,
	geom public.geometry(multipolygon, 5186) NULL,
	CONSTRAINT tl_sprd_rw_new_pkey{time_1[-2:]} PRIMARY KEY (gid)
);
CREATE INDEX tl_sprd_rw_new_geom_idx_{time_1[-2:]} ON gfdata.tl_sprd_rw_new USING gist (geom);
'''

#layer_group_4_건물통합정보
dic['al_d010_new'] = f'''
CREATE TABLE gfdata.al_d010_new (
	gid int4 DEFAULT nextval('gfdata.al_d010_new'::regclass) NOT NULL,
	a0 int4 NULL,
	a1 varchar(28) NULL,
	a2 varchar(19) NULL,
	a3 varchar(10) NULL,
	a4 varchar(254) NULL,
	a5 varchar(10) NULL,
	a6 varchar(1) NULL,
	a7 varchar(254) NULL,
	a8 varchar(5) NULL,
	a9 varchar(254) NULL,
	a10 varchar(2) NULL,
	a11 varchar(254) NULL,
	a12 float8 NULL,
	a13 varchar(10) NULL,
	a14 float8 NULL,
	a15 float8 NULL,
	a16 float8 NULL,
	a17 float8 NULL,
	a18 float8 NULL,
	a19 varchar(28) NULL,
	a20 varchar(2) NULL,
	a21 varchar(17) NULL,
	a22 date NULL,
	a23 varchar(5) NULL,
	a24 varchar(254) NULL,
	a25 varchar(254) NULL,
	a26 int4 NULL,
	a27 int4 NULL,
	a28 varchar(10) NULL,
	geom public.geometry(multipolygon, 5186) NULL,
	CONSTRAINT al_d010_new_pkey_{time_1[-2:]} PRIMARY KEY (gid)
)
TABLESPACE gf
;
CREATE INDEX al_d010_geom_idx_{time_1[-2:]} ON gfdata.al_d010_new USING gist (geom);
CREATE INDEX al_d010_geom_idx1_{time_1[-2:]} ON gfdata.al_d010_new USING gist (geom);'''



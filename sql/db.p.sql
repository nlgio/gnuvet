/*
 * sql/db.psql: script to build the gnuvet database in postgres
 *   TAKE CARE THIS IS FOR DEVEL.  PRODUCTION NEEDS DIFFERENT.
 * Copyright (c) 2015 Dipl.Tzt. Enno Deimel <ennodotvetatgmxdotnet>
 *
 * This file is part of gnuvet, published under the GNU General Public License
 * version 3 or later (GPLv3+ in short).  See the file LICENSE for information.
 *
 * After having created the gnuvet db, aptly named `gnuvet'
 * -- for instance with /usr/bin/createdb -- on the db machine, you can roll
 * in this script like so: $ psql gnuvet < db.psql
 * This should be performed as user 'gnuvet'.
 */

-- TODO:
--  solve vacc reminders

\c postgres
drop database if exists gnuvet;
--drop role if exists gvuser;
--drop role if exists gnuvet; -- this won't work being logged in as gnuvet! Put in shell script.  Think of psql serving not only gnuvet...
-- create role gnuvet createdb createrole login encrypted password 'GnuVetPassword' replication;
-- create role gvuser login; -- this for later, the -- well -- gvusers group
-- grant connect temp

-- test 150223:
set client_encoding to 'UTF-8';
create database gnuvet encoding 'UTF-8'; -- test 150223

\c gnuvet


create table boxroles(
 boxr_id serial primary key,
 boxr_name varchar(120) not null);
-- 'master server', 'local server', 'workstation' etc.

create table staffroles(
 staffrole_id serial primary key,
 staffrole_name varchar(20) not null);

create table titles(
 t_id serial primary key,
 t_title varchar(20) not null);

create type sex as enum('m', 'f', 'h', 'n');

-- colour combination: n not, y possible, o obligatory
--create type colcombine as enum('n','y','o');
-- obs this in favour of bit null 0 1, obsoleting this type

create table markups(
 m_id serial primary key,
 m_name varchar(30) not null,
 m_rate numeric(4,3) not null,
 m_obs boolean not null default FALSE);

/* service type: other med serv good food cons hist
create table ptypes(
 pt_id serial primary key,
 pt_name varchar(20) not null,
 pt_markup integer not null references markups default 1);*/

create type ptype as enum('vac','con','hst','med','srv','god','fod','oth');

create table addresses(
 addr_id serial primary key,
 housen varchar(80) not null default '',
 street varchar(80) not null default '',
 village varchar(80) not null default '',
 city varchar(80) not null default '',
 region varchar(80) not null default '',
 postcode varchar(10) not null default '');

create table branches(
 branch_id serial primary key,
 branch_name varchar(120) not null,
 branch_address integer references addresses not null default 1,
 branch_tel varchar(30),
 branch_mobile varchar(30),
 branch_fax varchar(30),
 branch_email varchar(120),
 branch_vatreg varchar(20),
 branch_currency varchar(5),
 branch_currencysymbol varchar(3));

create table boxes( -- computers in gnuvet network
 box_id serial primary key,
 box_name varchar(80) not null, --  'Surgery1', 'Reception2' etc.
 box_ipv4 inet unique not null,
 box_branch integer references branches not null,
 box_role integer references boxroles not null);

create table staff(
 stf_id serial primary key,
 stf_func integer references staffroles not null default 2,
 stf_title integer references titles not null default 3,
 stf_sex sex not null default 'n',
 stf_surname varchar(80) not null,
 stf_mname varchar(25) not null default '',
 stf_forename varchar(80) not null,
 stf_short varchar(10) unique not null,
 stf_logname varchar(10) unique not null,
 stf_tel varchar(30),
 stf_mobile varchar(30),
 stf_email varchar(120));

create table clients(
 c_id serial primary key,
 c_title int references titles not null default 3,
 c_sname varchar(80) not null,
 c_mname varchar(25) not null default '',
 c_fname varchar(80) not null default '',
 c_address integer references addresses not null default 1,
-- c_telhome varchar(30) not null default '',
-- c_telwork varchar(30) not null default '',
-- c_mobile1 varchar(30) not null default '',
-- c_mobile2 varchar(30) not null default '',
 c_email varchar(120) not null default '',
 baddebt boolean not null default False,
 c_reg date not null,
 c_last timestamp not null default current_timestamp,
 c_anno varchar(255) not null default '');

create table phones( -- client phones
-- phone_id serial primary key,
 phone_cid integer not null references clients,
 phone_opt smallint not null default 1, -- 1 best
 phone_num varchar(25) not null default '',
 phone_anno varchar(25) not null default '',
 unique(phone_cid,phone_num));

-- keys presumably overkill for up to medium-sized practice:
--create index c_sname on clients(c_sname);
--create index c_fname on clients(c_fname);
--create index c_last on clients(c_last)

create table locations(
 l_id serial primary key,
 l_name varchar(80) not null,
 l_address integer references addresses not null default 1,
 l_tel varchar(30) default '',
 l_mobile varchar(30) default '',
 l_anno varchar(255) not null default '');

-- keys presumably overkill for up to medium-sized practice

create table species(
 spec_id serial primary key,
 spec_name varchar(80) unique not null,
-- spec_code char(1) unique not null,
-- this to replaced by function 1<<id-1
 spec_fa boolean not null default TRUE); -- potential food animal
-- actually mostly genus/order not species

create table breeds(
 breed_id serial primary key,
 b_spec integer references species not null,
 breed_name varchar(80) unique not null,
 breed_abbr varchar(5) unique not null);

create table basecolours(
 bcol_id serial primary key,
 bcol varchar(25) unique,
-- bc_combine colcombine not null default 'y',
-- this to be bit(1) for null (none), 0 (poss), 1 (must)
 bc_combine bit(1) default '0',
-- bc_speccode varchar(120) not null);
 bc_speccode int not null);

create table colours(
 col_id serial primary key,
-- c_speccode varchar(120) not null,
 c_speccode int not null,
 col1 integer references basecolours not null,
 col2 integer references basecolours not null,
 col3 integer references basecolours not null,
 unique (col1,col2,col3));

create table insurances(
 i_id serial primary key,
 i_name varchar(80) not null,
 i_email varchar(120),
 i_rep varchar(120),
 i_address integer references addresses not null default 1,
 i_tel varchar(30),
 i_anno varchar(255) not null default '');

create table chronics(
 chr_id serial primary key,
 chr_name varchar(80) not null);

create table patients(
 p_id serial primary key,
 p_name varchar(80) not null, -- hierwei
 p_cid integer references clients not null,
 breed integer references breeds,
 xbreed boolean not null default False,
 dob date,
 dobest boolean not null default False,
 colour integer references colours,
 sex sex,
 neutd boolean default False,
 vicious boolean not null default False,
 p_reg date,
 p_anno varchar(255) not null default '',
 loc integer references locations,
 identno varchar(20),
 petpass varchar(20),
 rip boolean not null default False,
 p_last timestamp,
 ins integer references insurances,
 chr integer not null default 0); --> chronic problems, 1<<chr-1 bitmask

create index p_name_idx on patients(p_name);

-- maybe redundance, but i think eases search for patient seen some date:
create table seen(seen_pid integer references patients, seen_date date);

create index seen_pid_idx on seen(seen_pid);

create table neuts(
 neut_id integer references patients not null,
 neut_date date);

create table rips(
 rip_id integer references patients not null,
 rip_date timestamp not null);

create table ownerhistory(
 oh_id serial primary key,
 oh_pid int references patients not null,
 oh_prev int references clients not null,
 oh_date date not null);

create table namehistory(
 nh_id serial primary key,
 nh_pid int references patients not null,
 nh_name varchar(80) not null default '',
 nh_date date not null);

create table vats(
 vat_id serial primary key,
 vat_name varchar(30) not null,
 vat_rate numeric(5,4) not null,
 vat_obs boolean not null default FALSE);

create table units(
 u_id serial primary key,
 u_name varchar(20) not null,
 u_pl varchar(20) not null,
 u_abbr varchar(5) not null,
 u_short varchar(1) unique not null default '');

create table categories(
 cat_id serial primary key,
 category varchar(40) not null unique);

create table ingredients(
 ingr_id serial primary key,
 ingredient varchar(50) not null unique,
 ingr_catid integer references categories); -- not null?

create table suppliers(
 s_id serial primary key,
 s_name varchar(80) not null,
 s_rep varchar(120),
 s_email varchar(80),
 s_address integer references addresses not null default 1,
 s_tel varchar(30),
 s_fax varchar(30),
 s_mobile varchar(30));

/*  collection of building blocks for medication instructions */
create table instructions(
 inst_id serial primary key,
 inst_abbr varchar(5) not null,
 inst_txt varchar(90) not null,
 inst_pos integer not null,
 unique (inst_abbr, inst_pos));

/* collection of printed label texts for re-use */
create table labels(
 lb_id serial primary key,
 lb_abbr varchar(15) unique,
 lb_txt varchar(255) unique);

create table pay_modes(pm_id serial primary key,pm_mode varchar(20) not null,pm_ck bool not null default TRUE);

create table products(
 pr_id serial primary key,
 pr_name varchar(80) not null,
 pr_short varchar(10) not null,
-- pr_type integer references ptypes not null default 1, -- srv, med, good etc.
 pr_type ptype not null default 'med',
 pr_pprice numeric(8,2) not null default 0.00, -- net purchase price
 pr_nprice numeric(8,2) not null, -- net sale price
 pr_from date not null default '2010-01-01',
 pr_vat integer references vats default 1,
 pr_perm boolean not null default FALSE, -- 0 OTC,  1 POM
 pr_u integer references units not null,
-- pr_ingr integer references ingredients, -- bitmask? separate table! if at all
 pr_instr boolean not null default TRUE -- ask for instructions
-- pr_upordu numeric(8,4), -- for assistance in price calc -- whatsthis?
);

create table batchnos(
 chb_id serial primary key,
 chb_prid integer references products,
 chb_val varchar(30) not null);

/* create table barcodes(
 bcode_id serial primary key,
 bcode_prid integer references products;
 bcode_val integer);

create table stocks(
 st_id serial primary key,
 st_prid integer not null references products,
 st_num numeric(9,2) not null);

create table limits(
 l_id serial primary key,
 l_prid integer not null references products,
 l_val numeric(9,2) not null);

create table pr_supplier(
 prid integer not null references products,
 prsup integer references suppliers,
 prordid varchar(100));
****************/

/*create table prodoldprices( -- more efficient than obsoleting old prodprices
 pop_id serial primary key,
 pop_prid integer not null references products,
 pop_npr numeric(8,2) not null,
 pop_vat integer not null references vats,
 pop_fromdate date not null);

create table toorder(o_prid integer not null references products, o_date date);
**************/

/* 'validity' for vaccinations */
create table validities(
 val_id serial primary key,
 val_text varchar(255) not null,
 val_days integer not null);

create table vtypes(
 vt_id serial primary key,
 vt_type varchar(20));

create table vaccinations(
 vac_id serial primary key,
 vac_type integer not null references vtypes,
 vac_prid integer not null references products, -- used product
 vac_sid integer not null references products, -- service
 vac_validity integer references validities, -- not null ifd
 vac_spec integer references species); -- null: all, like rabies

create table vdues(vd_pid integer not null references patients,vd_type integer references vtypes,vd_vdue date not null);

 -- to ease use of the diverse tables, currently unused
-- create or replace view vacs (v_id,v_prod,v_serv,v_short,v_nprice,v_spec) as select vac_id,p.pr_name,s.pr_name,s.pr_short,case when s.pr_nprice=0 then 0.00 else p.pr_nprice + s.pr_nprice end,vac_spec from vaccinations,products p,products s where vac_prid=p.pr_id and vac_sid=s.pr_id;

create table symptoms(
 sy_id serial primary key,
 symptom varchar(80) not null,
 sy_short varchar(5) not null);

create table applications( -- link product to service: a injectable->injection
 app_id serial primary key,
 app_keyword varchar(20) not null);

create table app2prod(
 a2p_prid integer references products primary key,
 a2p_prod integer references applications not null);

/*create table withdrawals( -- wartezeiten #d
 w_id serial primary key,
 w_prid integer references products,
 w_spec integer references species,
 w_app integer references wd_apps,
 w_meat integer not null,
 w_milk integer,
 w_eggs integer,
 w_obs boolean not null default FALSE);

create table wd_apps( -- wd dependent on app type and/or dosage
 wda_id serial primary key,
 wda_app varchar(8),
 wda_dosage varchar(120));*/

create table invoices(inv_id serial primary key,inv_no integer not null unique);
-- cave 0er Jahre: select length(n::text)<10 -> +0

create table appointments(
 app_id serial primary key,
 app_dt timestamp not null,
 app_text varchar(128) not null,
 app_cid integer references clients,
 app_pid integer references patients,
 app_staffid integer references staff,
 app_dur interval not null default '0:00',
 app_status char not null default 'o');

/* tables created by application on demand:
accN:    account client N
	 acc_id acc_pid acc_prid acc_npr acc_vat acc_paid
	 ## invno: int->invoices.invoice_id
	 # pid: patient.p_id
	 # acc_prid int->medN.id
	 # net price, vat
	 # acc_paid: paydate
invN:    invoice for client N
         inv_no price vat amount
weightN: weight entries for patient N
vacN:    registers vacc, date and due -- yes some redundancy
---
eN:	 id: consid to coordinate entries in following tables
chN:   	 actual clinical history i.e. findings
       	 id consid dt text symp staff seq
	 # seq to order ch|med|inst in case of stopped timer:
	 # 1st cons from medN, 2nd history from chN, further from medN again
prodN:	 booked products -- was medN
       	 id consid dt type (serv med good other ...) txt (int->products.pr_id)
	 count symp staff seq
instN: 	 instructions for medication
       	 id text prodid (int->medN.id)
*/

-- create table receipts(recpt_id serial primary key, recpt_date date not null, recpt_cid integer references clients not null, recpt_sum numeric(9,2) not null, recpt_paymode varchar(30));
-- de: 'Bar', 'Kontokarte', 'Kreditkarte', 'Scheck', 'Überweisung', 'Einzug'

-- create type statem_env as enum ('Invoice','Receipt','Letter','Statement');
-- create table statements(stat_id serial primary key, stat_env statem_env not null, statement varchar(80) not null);

-- create type ordermode as enum('fax','email','modem','online','application','phone','letter'); --?
-- create table orders(ord_id serial primary key, ord_date timestamp not null, ord_prid integer references products not null, ord_amount integer not null, ord_supplier integer references suppliers not null, ord_method ordermode not null);

-- delivery?

-- appointments? queues?
-- create table queues(q_id serial primary key, q_name varchar(80) not null);
-- create table apps(app_id serial primary key, a_queue smallint references queus not null, a_staff integer references staff not null, a_datetime timestamp not null, a_duration smallint not null /* minutes */, a_pid integer references patients, a_cid integer references clients not null, a_anno varchar(80) not null default '');


--##################
--# RECONSIDER THESE
--##################
-- waiting(WaitId integer primary key, ArrivedOrder smallint not null, WaitingDateTime timestamp not null, WaitingPId int not null, WaitingBookedTime enum('5','10','15','20','30','45','60','90','120') not null, WaitingForStaff smallint not null, WaitingForServ smallint not null, WaitingComment varchar(50) not null, WaitingStatus enum('w','s','d','p','f')/*waiting served done payment finished*/ not null);

--##################
--### IN THE BINARY:
--##################
-- patient vaccs:
-- create table vacN(
--  v_id serial primary key,
--  vvacid integer references vaccinations not null,
--  vdate timestamp not null,
--  vdue date not null);

-- product action, special price for certain period:
-- create table pactions(pa_id serial primary key, pa_prid integer references products not null, pa_name varchar(80) not null default '', pa_red numeric(3,3) not null, pa_start date not null, pa_end date not null);

-- change of ownership:
-- create table ownerchange(oc_id serial primary key, oc_pid integer references patients not null, oc_fowner integer references clients not null, oc_date date not null);

-- create table orderTIMESTAMP(o_id serial primary key, ono varchar(15) not null, oprid integer references products not null, ogprice numeric(6,2) not null, ogvat integer references vats not null, ogamount numeric(6,3) not null, ogdate date not null, osentdate date not null, ogreceived date/*?*/ not null, ogpaid date not null);

-- journals from present data.
-- archives:older 2a  waiting invoices?  receipts?

-- consider statistics about products/goods/services per time period

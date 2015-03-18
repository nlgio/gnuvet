-- for postgres

alter table clients add toc smallint default 0 ; -- Terms of Credit in Days
alter table clients alter c_reg set default now()::date;



update patients  set neutd ='f' where neutd is null ;
alter table patients add deceased date ; -- makes rips obsolete
alter table patients alter p_reg set default now()::date;
alter table patients  ALTER p_last drop not null;


create table payms  ( paym_id serial primary key, pay_cid integer references clients ,pay_date date not null default now()::date, pay_amount numeric(9,2) default 1 not null, pay_ref varchar not null default '' );
alter table payms add paytyp smallint default 0 ;
insert into paymodes ( pay_id,pay_mode) values (0,'Liab');
insert into paymodes ( pay_mode) values ('Write Off');


alter table invoices  add c_id integer references clients ;
alter table invoices  add stmt_date date ;
alter table invoices  add ref varchar default '';
alter table invoices  add excl_vat numeric(9,2) default 0;
alter table invoices  alter inv_no drop not null; -- invoice number is spent at close time

create table accs ( accs_id serial primary key, acc_cid integer references clients not null, acc_prid integer not null references products, acc_qty smallint not null default 1, acc_npr numeric(9,2) not null, acc_details varchar, acc_inv integer, acc_date timestamp without time zone default now() not null, acc_pid integer references patients );

create table weights ( w_id serial primary key, w_pid integer not null references patients, w_est boolean not null default 'f', w_date timestamp without time zone not null default now(), weight numeric(7,3) not null, w_staff integer references staff not null default 1 );

create table chs( ch_id serial primary key, ch_pid integer not null references patients, ch_date timestamp without time zone not null default now(), ch_descr varchar not null default '', ch_symp integer references symptoms not null default 1, ch_staff varchar not null default current_user );



create view  client_combos  as select c.c_id, lower(c.c_sname||'#'||c.c_fname||'#' ||string_agg(coalesce(p.p_name,''),'#')) as expr from clients c left outer join patients p on ( c.c_id = p.p_cid ) group by c.c_id, c.c_sname||c.c_fname ;


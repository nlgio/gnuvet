
alter table clients add toc smallint default 0 ; -- Terms of Credit in Days
alter table clients alter c_reg set default now()::date;

alter table patients add deceased date ; -- makes rips obsolete
alter table patients alter p_reg set default now()::date;
alter table patients  ALTER p_last drop not null;


alter table payms add paytyp smallint default 0 ;



alter table invoices  add c_id integer references clients ;
alter table invoices  add stmt_date date ;
alter table invoices  add ref varchar default '';
alter table invoices  add excl_vat numeric(9,2) default 0;
alter table invoices  alter inv_no drop not null; -- invoice number is spent at close time

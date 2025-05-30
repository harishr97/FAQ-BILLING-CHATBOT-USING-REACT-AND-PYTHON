----Creating Database

create database chatbot;
----Creating Table
create table public.billing_t (id int, secret_id varchar(50), user_name varchar(50), used_service varchar(50), month varchar(50), amount float, address varchar(100), base_charge float, additional_charge float, taxes float, year varchar(20), next_bill_cycle varchar(20), autopay_date varchar(20));

---Inserting one record into Table
insert into public.billing_t values (3, 'SHAVOX34534','SHARADA','CELLULAR_PREPAID','OCTOBER','749.50','No. 7, Normal theru, Normal road, chennai-28', 500, 180, 69.45, 2024, '2024-11-01', '2024-11-10');


---Querying Table
select * from public.billing_t;



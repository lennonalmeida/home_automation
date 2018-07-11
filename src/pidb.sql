drop database pi;
create database pi
default character set utf8
default collate utf8_general_ci;
use pi;
#table created
create table app2state(
	id tinyint(2) not null auto_increment,
    state enum('ON', 'OFF') default 'ON',
    primary key (id)
)default charset = utf8;

#add a new appliance
insert into app2state
(state)
values
('OFF');
insert into app2state
(state)
values
('ON');

#change state
update app2state
set state='OFF'
where id=2;

SELECT state
FROM app2state
where state
BETWEEN 1 AND 2;
#show table
select * from app2state;

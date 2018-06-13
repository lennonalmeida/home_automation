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
(id, state)
values
('2', 'OFF');
insert into app2state
(id, state)
values
('1', 'ON');

#change state
update app2state
set state='ON'
where id=2;

#show table
select * from app2state;

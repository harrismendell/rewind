drop table if exists claimed_records;
    create table claimed_records (
    id integer primary key,
    band text not null,
    record text not null,
    record_cover text not null,
    price float not null,
);
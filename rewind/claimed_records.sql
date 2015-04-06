drop table if exists claimed_records;
    create table claimed_records (
    id integer primary key autoincrement,
    userid integer not null,
    band text not null,
    record text not null,
    record_cover text not null,
    price float not null
);
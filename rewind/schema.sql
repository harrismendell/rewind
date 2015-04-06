drop table if exists record;
    create table record (
    id integer primary key autoincrement,
    band text not null,
    record text not null,
    record_cover text not null,
    price float not null,
    current_buyers integer not null,
    max_buyers integer not null,
    pitchfork_score float not null,
    pitchfork_link text not null,
    review_snippet text null,
    days_to_go integer not null
);
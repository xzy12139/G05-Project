CREATE TABLE user (
    user_id     varchar(20)     not null,
    user_name   varchar(20)     not null,
    password    varchar(20)     not null,
    PRIMARY KEY (user_id)
);

CREATE TABLE thesis (
    thesis_id           varchar(50)     not null,
    title               varchar(50)     not null,
    author              varchar(30)     not null,
    publication_date    date            default null,
    journal             varchar(30)     not null,
    abstract            varchar(900)    not null,
    link                varchar(100),
    citation_num        int,
    rating              double,
    PRIMARY KEY (thesis_id)
);

CREATE TABLE favorites (
    user_id     varchar(20)     not null,
    thesis_id           varchar(50)     not null,
    PRIMARY KEY (user_id, thesis_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (thesis_id) REFERENCES thesis(thesis_id)
)
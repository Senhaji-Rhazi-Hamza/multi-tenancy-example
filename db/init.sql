CREATE TABLE IF NOT EXISTS users (
  id varchar not null,
  creation_timestamp timestamp,
  name varchar not null,
  password varchar not null,
  mail varchar not null,
  organization_id varchar not null,
  PRIMARY KEY (id)
);


CREATE SCHEMA IF NOT EXISTS client1;

CREATE TABLE IF NOT EXISTS client1.items (
  id varchar not null,
  creation_timestamp timestamp,
  description varchar not null,
  price float not null,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS client1.orders (
  id varchar not null,
  creation_timestamp timestamp,
  quantity integer,
  user_id varchar not null,
  item_id varchar not null,
  CONSTRAINT fk_user
      FOREIGN KEY(user_id) 
	  REFERENCES users(id),
  CONSTRAINT fk_item
      FOREIGN KEY(item_id) 
	  REFERENCES client1.items(id),
  PRIMARY KEY (id)
);

CREATE SCHEMA IF NOT EXISTS client2;

CREATE TABLE IF NOT EXISTS client2.items (
  id varchar not null,
  creation_timestamp timestamp,
  quantity integer,
  description varchar not null,
  price float not null,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS client2.orders (
  id varchar not null,
  creation_timestamp timestamp,
  quantity integer,
  user_id varchar not null,
  item_id varchar not null,
  CONSTRAINT fk_user
      FOREIGN KEY(user_id) 
	  REFERENCES users(id),
  CONSTRAINT fk_item
      FOREIGN KEY(item_id) 
	  REFERENCES client2.items(id),
  PRIMARY KEY (id)
);

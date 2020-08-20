INSERT INTO
  public.users (id, "name", "password", mail, organization_id)
VALUES
  (
    '1',
    'rich_dude',
    'ovious_password1',
    'h@gmail.com',
    'client1'
  );

INSERT INTO
  public.users (id, "name", "password", mail, organization_id)
VALUES
  (
    '2',
    'poor_dude',
    'ovious_password2',
    'p@gmail.com',
    'client2'
  );

INSERT INTO
  client1.items (id, description, price)
VALUES
  ('1', 'Tesla', 5000);

INSERT INTO
  client2.items (id, description, price)
VALUES
  ('1', 'Tesla', 1000);

INSERT INTO
  client1.items (id, description, price)
VALUES
  ('2', 'Huawei', 2000);

INSERT INTO
  client2.items (id, description, price)
VALUES
  ('2', 'Huawei', 100);


INSERT INTO
  client1.orders (id, user_id, item_id, quantity)
VALUES
('1', '1', '1',10);

INSERT INTO
  client1.orders (id, user_id, item_id, quantity)
VALUES
('2', '1', '2', 5);

INSERT INTO
  client2.orders (id, user_id, item_id, quantity)
VALUES
('1', '2', '1', 10);

INSERT INTO
  client2.orders (id, user_id, item_id, quantity)
VALUES
('2', '2', '2', 5);

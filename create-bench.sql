create table if not exists Bench (
  Workout integer primary key,
  Day Text not null,
  Weight integer default 0
);

CREATE DATABASE IF NOT EXISTS dm
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE dm;

CREATE TABLE IF NOT EXISTS tb_user (
  id         INT          NOT NULL AUTO_INCREMENT,
  user_name      VARCHAR(100) NOT NULL,
  user_email     VARCHAR(150) NOT NULL UNIQUE,
  user_password     VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS tb_caracteristics (
  id          INT          NOT NULL AUTO_INCREMENT,
  habitat     VARCHAR(100),
  region      VARCHAR(100),
  practice    TEXT,
  habits      TEXT,
  location    JSON,
  location_description VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tb_animal (
  id               INT          NOT NULL AUTO_INCREMENT,
  animal_name             VARCHAR(100) NOT NULL,
  animal_imagem_url       VARCHAR(500),
  animal_color            VARCHAR(50),
  animal_height           DECIMAL(5,2),
  animal_weight           DECIMAL(7,2),
  caracteristics_id INT        NOT NULL UNIQUE,
  PRIMARY KEY (id),
  FOREIGN KEY (caracteristics_id) REFERENCES tb_caracteristics(id)
);


CREATE TABLE IF NOT EXISTS tb_question (
  id                        INT		       NOT NULL AUTO_INCREMENT,
  question_statement        TEXT	       NOT NULL,
  question_possibilities    JSON         NOT NULL,
  answer_id                 INT          NOT NULL,
  answer_details            TEXT,
  animal_id                 INT          NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (animal_id) REFERENCES tb_animal(id)  
);

CREATE TABLE IF NOT EXISTS tb_user_answer (
  id                   INT      NOT NULL AUTO_INCREMENT,
  date_time            DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  was_correct_answer   TINYINT(1) NOT NULL DEFAULT 0,
  user_id              INT      NOT NULL,
  question_id          INT      NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES tb_user(id),
  FOREIGN KEY (question_id) REFERENCES tb_question(id)
);

CREATE INDEX idx_user_email ON tb_user(user_email);

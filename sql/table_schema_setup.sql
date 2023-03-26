CREATE TABLE platform (
  id INT(10) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255),
  url VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE program (
  id INT(10) NOT NULL AUTO_INCREMENT,
  platform_id INT REFERENCES platform(id),
  name VARCHAR(255),
  directory VARCHAR(255),
  expl_level INT(10),
  priority INT(10),
  private BOOL NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
);


CREATE TABLE domain (
  id INT(10) NOT NULL AUTO_INCREMENT,
  program_id INT REFERENCES program(id),
  directories MEDIUMTEXT,
  url VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE subdomain (
  id INT(10) NOT NULL AUTO_INCREMENT,
  domain_id INT REFERENCES domain(id),
  url VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE ip (
  id INT(10) NOT NULL AUTO_INCREMENT,
  domain_id INT REFERENCES domain(id),
  address INT(4) UNSIGNED NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE port (
  id INT(10) NOT NULL,
  ip_id INT REFERENCES ip(id),
  service_name VARCHAR(255),
  directories MEDIUMTEXT,
  PRIMARY KEY (id)
);

CREATE TABLE vulnerability (
  domain_id INT(10) REFERENCES domain(id),
  ip_id INT REFERENCES ip(id),
  label varchar(255),
  criticality varchar(255)
);



CREATE DATABASE IF NOT EXISTS `flask-db`;
USE `flask-db`;

SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS;
SET FOREIGN_KEY_CHECKS = 0;


CREATE TABLE IF NOT EXISTS portfolio
             (
                          id    INTEGER NOT NULL AUTO_INCREMENT,
                          pname  VARCHAR(50) NOT NULL,
                          PRIMARY   KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS stock
             (
                          id            INTEGER NOT NULL AUTO_INCREMENT,
                          portfolio_id  VARCHAR(30) NOT NULL,
                          stock         VARCHAR(50) NOT NULL,
                          position      INTEGER NOT NULL,
                          PRIMARY KEY (id),
                        CONSTRAINT FK_PortfolioStock FOREIGN KEY (portfolio_id) REFERENCES portfolio(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
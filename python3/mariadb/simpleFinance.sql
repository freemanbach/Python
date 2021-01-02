
-- DB design
-- CI/CD process of this DB
-- USE: mysql -u YOUR_USER_NAME -p < simplefinance.sql

-- KISS ACID
-- https://database.guide/what-is-acid-in-databases/

drop database if exists simplefinance;
create database if not exists simplefinance;
USE simplefinance;


-- alphavantage.co (Overview partly)
-- https://www.alphavantage.co/documentation/
-- https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
drop table if exists `company`;
CREATE TABLE `company` (
                           `id`          int(10) not null auto_increment,
                           `ticker`      varchar(10) NULL,
                           `assettype`   varchar(40)  NULL,
                           `name`        varchar(100)  NULL,
                           `description` varchar(2000) NULL,
                           `exchange`    varchar(10) NULL,
                           `currency`    varchar(10) NULL,
                           `country`     varchar(10) NULL,
                           `sector`      varchar(100) NULL,
                           `industry`    varchar(100) NULL,
                           PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 
drop table if exists `ticker`;
CREATE TABLE `ticker` (
                            `id`        int(11) not null auto_increment,
                            `ticker_id` int(10) NULL,
                            `ticker`    varchar(10) NULL,
                            PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


-- timestamp,open,high,low,close,volume
drop table if exists `stock_price`;
CREATE TABLE `stock_price` (
                          `id`         int(11) not null auto_increment,
                          `ticker_id`  int(10) NULL,
                          `datepull`   date NULL,
                          `time`       timestamp NULL,
                          `date`       date NULL,
                          `open`       decimal(12,4)  NULL,
                          `high`       decimal(12,4) NULL,
                          `low`        decimal(12,4) NULL,
                          `close`      decimal(12,4) NULL,
                          `volume`     decimal(20,4) NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- alter table stock_price add constraint fk_stock_price_company foreign key (`ticker_id`) references company(`id`) on update cascade on delete cascade;



-- alphavantage.co (Overview partly)
-- https://www.alphavantage.co/documentation/
-- https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
drop table if exists `stock_overview`;
CREATE TABLE `stock_overview` (
                            `id`                         int(11) not null auto_increment,
                            `ticker_id`                  int(10) NULL,
                            `datepull`                   date NULL,
                            `PEratio`                    decimal(12,4) NULL,
                            `PEGratio`                   decimal(12,4) NULL,
                            `bookvalue`                  decimal(12,4) NULL,
                            `dividendpershare`           decimal(12,4) NULL,
                            `dividendyield`              decimal(12,4) NULL,
                            `EPS`                        decimal(12,4) NULL,
                            `profitmargin`               decimal(12,4) NULL,
                            `quarterlyearningsgrowthYOY` decimal(12,4) NULL,
                            `quarterlyrevenuegrowthYOY`  decimal(12,4) NULL,
                            `returnonequityTTM`          decimal(12,4) NULL,
                            `revenueTTM`                 decimal(12,4) NULL,
                            `grossprofitTTM`             decimal(12,4) NULL,
                            `beta`                       decimal(12,4) NULL,
                            `52weekhigh`                 decimal(12,4) NULL,
                            `52weeklow`                  decimal(12,4) NULL,
                            `dividend`                   decimal(12,4) NULL,
                            `payoutratio`                decimal(12,4) NULL,
                            PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- alter table stock_overview add constraint fk_stock_overview_company foreign key (`ticker_id`) references company(`id`) on update cascade on delete cascade;
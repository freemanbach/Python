
drop database if exists simplefinance;
create database if not exists simplefinance;
USE simplefinance;

-- nasdaq screen app
-- https://www.nasdaq.com/market-activity/stocks/screener
drop table if exists `company`;
CREATE TABLE `company` (
                           `id` int(10) not null auto_increment,
                           `name` varchar(100)  NULL,
                           `ticker` varchar(10) NULL,
                           `description` varchar(1000) NULL ,
                           `sector` varchar(100) NULL ,
                           `industry` varchar(200) NULL,
                           PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

drop table if exists `daily_price`;
CREATE TABLE `daily_price` (
                          `id` int(11) not null auto_increment,
                          `ticker_id` int(10) NULL,
                          `ticker` varchar(10) NULL,
                          `date` date NULL,
                          `time` timestamp NULL,
                          `open` decimal(12,4)  NULL,
                          `high` decimal(12,4) NULL,
                          `low` decimal(12,4) NULL,
                          `close` decimal(12,4) NULL,
                          `volume` decimal(12,4) NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
alter table daily_price add constraint fk_daily_price_company foreign key (`ticker_id`) references company(`id`) on update cascade on delete cascade;


drop table if exists `stock_adjust`;
CREATE TABLE `stock_adjust` (
                                    `id` int(11) not null auto_increment,
                                    `ticker_id` int(10) NULL,
                                    `ticker` varchar(10) NULL,
                                    `date` date NULL,
                                    `factor` decimal(12,4)  NULL,
                                    `dividend` decimal(12,4)  NULL,
                                    `split_ratio` decimal(12,4) NULL,
                                    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
alter table stock_adjust add constraint fk_stock_adjust_company foreign key (`ticker_id`) references company(`id`) on update cascade on delete cascade;
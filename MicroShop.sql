DROP DATABASE IF EXISTS `MicroShop`;

CREATE DATABASE `MicroShop`;

USE `MicroShop`;

DROP TABLE IF EXISTS `Customer`;
CREATE TABLE `Customer`(
	customer_id INT,
	name VARCHAR(100),
	primary key(customer_id)
);

DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order`(
	order_id INT,
	date VARCHAR(100),
	total INT,
	customer_id INT,
	primary key(order_id)
);

DROP TABLE IF EXISTS `OrderLine`;
CREATE TABLE `OrderLine`(
	orderline_id INT,
	order_id INT,
	product_id INT,
	count INT,
	total INT,
	primary key(orderline_id)
);

DROP TABLE IF EXISTS `Product`;
CREATE TABLE `Product`(
	product_id INT,
	name VARCHAR(100),
	price INT,
	primary key(product_id)
);


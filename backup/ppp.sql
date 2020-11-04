-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2020 at 11:28 PM
-- Server version: 8.0.13
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ppp`
--
CREATE DATABASE IF NOT EXISTS `ppp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ppp`;

-- --------------------------------------------------------

--
-- Table structure for table `loans`
--

CREATE TABLE IF NOT EXISTS `loans` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `description` text COLLATE utf8mb4_general_ci,
  `type` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `sector` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `employees` int(10) UNSIGNED NOT NULL,
  `date_approved` timestamp NOT NULL,
  `loan_amount` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `lender` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=COMPACT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

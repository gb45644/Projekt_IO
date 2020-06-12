-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 12, 2020 at 03:01 PM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `io`
--

-- --------------------------------------------------------

--
-- Table structure for table `calendar`
--

CREATE TABLE `calendar` (
  `id` int(11) NOT NULL,
  `Datagr` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `calendar`
--

INSERT INTO `calendar` (`id`, `Datagr`) VALUES
(1, '2020-05-01'),
(2, '2020-05-02'),
(3, '2020-05-03'),
(4, '2020-05-04'),
(5, '2020-05-05'),
(6, '2020-05-06'),
(7, '2020-05-07'),
(8, '2020-05-08'),
(9, '2020-05-09'),
(10, '2020-05-10'),
(11, '2020-05-11'),
(12, '2020-05-12'),
(13, '2020-05-13'),
(14, '2020-05-14'),
(15, '2020-05-15'),
(16, '2020-05-16'),
(17, '2020-05-17'),
(18, '2020-05-18'),
(19, '2020-05-19'),
(20, '2020-05-20'),
(21, '2020-05-21'),
(22, '2020-05-22'),
(23, '2020-05-23'),
(24, '2020-05-24'),
(25, '2020-05-25'),
(26, '2020-05-26'),
(27, '2020-05-27'),
(28, '2020-05-28'),
(29, '2020-05-29'),
(30, '2020-05-30'),
(31, '2020-05-31'),
(32, '2020-06-01'),
(33, '2020-06-02'),
(34, '2020-06-03'),
(35, '2020-06-04'),
(36, '2020-06-05'),
(37, '2020-06-06'),
(38, '2020-06-07'),
(39, '2020-06-08'),
(40, '2020-06-09'),
(41, '2020-06-10'),
(42, '2020-06-11'),
(43, '2020-06-12'),
(44, '2020-06-13'),
(45, '2020-06-14'),
(46, '2020-06-15'),
(47, '2020-06-16'),
(48, '2020-06-17'),
(49, '2020-06-18'),
(50, '2020-06-19'),
(51, '2020-06-20'),
(52, '2020-06-21'),
(53, '2020-06-22'),
(54, '2020-06-23'),
(55, '2020-06-24'),
(56, '2020-06-25'),
(57, '2020-06-26'),
(58, '2020-06-27'),
(59, '2020-06-28'),
(60, '2020-06-29'),
(61, '2020-06-30');

-- --------------------------------------------------------

--
-- Table structure for table `credentials`
--

CREATE TABLE `credentials` (
  `id` int(11) NOT NULL,
  `login` varchar(11) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `access` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `credentials`
--

INSERT INTO `credentials` (`id`, `login`, `pass`, `access`) VALUES
(1, 'kierownik', '1234', 4),
(2, 'planista', '4321', 2);

-- --------------------------------------------------------

--
-- Table structure for table `emploee_list`
--

CREATE TABLE `emploee_list` (
  `id` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `emploee_list`
--

INSERT INTO `emploee_list` (`id`, `Name`) VALUES
(1, 'Andrzej Długopis'),
(2, 'Gamon Raf'),
(3, 'Damian Dar');

-- --------------------------------------------------------

--
-- Table structure for table `graphic`
--

CREATE TABLE `graphic` (
  `id` int(11) NOT NULL,
  `calendar_fk` int(11) NOT NULL,
  `emploee_list_fk` int(11) NOT NULL,
  `work` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `graphic`
--

INSERT INTO `graphic` (`id`, `calendar_fk`, `emploee_list_fk`, `work`) VALUES
(2, 1, 1, 1),
(3, 2, 1, 1),
(4, 3, 1, 1),
(5, 4, 1, 1),
(6, 5, 1, 1),
(7, 6, 1, 1),
(8, 7, 1, 1),
(9, 8, 1, 1),
(10, 9, 1, 1),
(11, 10, 1, 1),
(12, 11, 1, 1),
(13, 12, 1, 1),
(14, 13, 1, 1),
(15, 14, 1, 1),
(16, 15, 1, 1),
(17, 16, 1, 1),
(18, 17, 1, 1),
(19, 18, 1, 1),
(20, 19, 1, 1),
(21, 20, 1, 1),
(22, 21, 1, 1),
(23, 22, 1, 1),
(24, 23, 1, 1),
(25, 24, 1, 1),
(26, 25, 1, 1),
(27, 26, 1, 1),
(28, 27, 1, 1),
(29, 28, 1, 1),
(30, 29, 1, 1),
(31, 30, 1, 1),
(32, 31, 1, 1),
(33, 32, 1, 1),
(34, 33, 1, 1),
(35, 34, 1, 1),
(36, 35, 1, 1),
(37, 36, 1, 1),
(38, 37, 1, 1),
(39, 38, 1, 1),
(40, 39, 1, 1),
(41, 40, 1, 1),
(42, 41, 1, 1),
(43, 42, 1, 1),
(44, 43, 1, 1),
(45, 44, 1, 1),
(46, 45, 1, 1),
(47, 46, 1, 1),
(48, 47, 1, 1),
(49, 48, 1, 1),
(50, 49, 1, 1),
(51, 50, 1, 1),
(52, 51, 1, 1),
(53, 52, 1, 1),
(54, 53, 1, 1),
(55, 54, 1, 1),
(56, 55, 1, 1),
(57, 56, 1, 1),
(58, 57, 1, 1),
(59, 58, 1, 1),
(60, 59, 1, 1),
(61, 60, 1, 1),
(62, 61, 1, 1),
(124, 1, 3, 1),
(125, 2, 3, 1),
(126, 3, 3, 1),
(127, 4, 3, 1),
(128, 5, 3, 1),
(129, 6, 3, 1),
(130, 7, 3, 1),
(131, 8, 3, 1),
(132, 9, 3, 1),
(133, 10, 3, 1),
(134, 11, 3, 1),
(135, 12, 3, 1),
(136, 13, 3, 1),
(137, 14, 3, 1),
(138, 15, 3, 1),
(139, 16, 3, 1),
(140, 17, 3, 1),
(141, 18, 3, 1),
(142, 19, 3, 1),
(143, 20, 3, 1),
(144, 21, 3, 1),
(145, 22, 3, 1),
(146, 23, 3, 1),
(147, 24, 3, 1),
(148, 25, 3, 1),
(149, 26, 3, 1),
(150, 27, 3, 1),
(151, 28, 3, 1),
(152, 29, 3, 1),
(153, 30, 3, 1),
(154, 31, 3, 1),
(155, 32, 3, 1),
(156, 33, 3, 1),
(157, 34, 3, 1),
(158, 35, 3, 1),
(159, 36, 3, 1),
(160, 37, 3, 1),
(161, 38, 3, 1),
(162, 39, 3, 1),
(163, 40, 3, 1),
(164, 41, 3, 1),
(165, 42, 3, 1),
(166, 43, 3, 1),
(167, 44, 3, 1),
(168, 45, 3, 1),
(169, 46, 3, 1),
(170, 47, 3, 1),
(171, 48, 3, 1),
(172, 49, 3, 1),
(173, 50, 3, 1),
(174, 51, 3, 1),
(175, 52, 3, 1),
(176, 53, 3, 1),
(177, 54, 3, 1),
(178, 55, 3, 1),
(179, 56, 3, 1),
(180, 57, 3, 1),
(181, 58, 3, 1),
(182, 59, 3, 1),
(183, 60, 3, 1),
(184, 61, 3, 1),
(185, 1, 2, 1),
(186, 2, 2, 1),
(187, 3, 2, 1),
(188, 4, 2, 1),
(189, 5, 2, 1),
(190, 6, 2, 1),
(191, 7, 2, 1),
(192, 8, 2, 1),
(193, 9, 2, 1),
(194, 10, 2, 1),
(195, 11, 2, 1),
(196, 12, 2, 1),
(197, 13, 2, 1),
(198, 14, 2, 1),
(199, 15, 2, 1),
(200, 16, 2, 1),
(201, 17, 2, 1),
(202, 18, 2, 1),
(203, 19, 2, 1),
(204, 20, 2, 1),
(205, 21, 2, 1),
(206, 22, 2, 1),
(207, 23, 2, 1),
(208, 24, 2, 1),
(209, 25, 2, 1),
(210, 26, 2, 1),
(211, 27, 2, 1),
(212, 28, 2, 1),
(213, 29, 2, 1),
(214, 30, 2, 1),
(215, 31, 2, 1),
(216, 32, 2, 1),
(217, 33, 2, 1),
(218, 34, 2, 1),
(219, 35, 2, 1),
(220, 36, 2, 1),
(221, 37, 2, 1),
(222, 38, 2, 1),
(223, 39, 2, 1),
(224, 40, 2, 1),
(225, 41, 2, 1),
(226, 42, 2, 1),
(227, 43, 2, 1),
(228, 44, 2, 1),
(229, 45, 2, 1),
(230, 46, 2, 1),
(231, 47, 2, 1),
(232, 48, 2, 1),
(233, 49, 2, 1),
(234, 50, 2, 1),
(235, 51, 2, 1),
(236, 52, 2, 1),
(237, 53, 2, 1),
(238, 54, 2, 1),
(239, 55, 2, 1),
(240, 56, 2, 1),
(241, 57, 2, 1),
(242, 58, 2, 1),
(243, 59, 2, 1),
(244, 60, 2, 1),
(245, 61, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `Description` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `Description`) VALUES
(1, '82_ECO BLACK'),
(2, '66_RTS RED');

-- --------------------------------------------------------

--
-- Table structure for table `item_std`
--

CREATE TABLE `item_std` (
  `id` int(11) NOT NULL,
  `std_op_fk` int(11) NOT NULL,
  `item_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `item_std`
--

INSERT INTO `item_std` (`id`, `std_op_fk`, `item_fk`) VALUES
(2, 1, 1),
(1, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `std_op`
--

CREATE TABLE `std_op` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `line` varchar(20) NOT NULL,
  `size` int(11) NOT NULL,
  `speed` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `std_op`
--

INSERT INTO `std_op` (`id`, `name`, `line`, `size`, `speed`) VALUES
(1, '82_ECO', 'CP01', 82, 15000),
(2, '66_RTS', 'CP02', 66, 18000);

-- --------------------------------------------------------

--
-- Table structure for table `wo`
--

CREATE TABLE `wo` (
  `id` int(11) NOT NULL,
  `item_fk` int(11) NOT NULL,
  `quantity` double NOT NULL,
  `start_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `wo`
--

INSERT INTO `wo` (`id`, `item_fk`, `quantity`, `start_date`) VALUES
(1, 1, 200000, '2020-05-18'),
(2, 1, 300000, '2020-05-03'),
(3, 2, 700000, '2020-05-03'),
(4, 1, 1000000, '2020-05-10'),
(5, 2, 500000, '2020-05-12');

-- --------------------------------------------------------

--
-- Table structure for table `wo_item`
--

CREATE TABLE `wo_item` (
  `ide` int(11) NOT NULL,
  `wo_fk` int(11) NOT NULL,
  `item_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `wo_item`
--

INSERT INTO `wo_item` (`ide`, `wo_fk`, `item_fk`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 1),
(5, 5, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `calendar`
--
ALTER TABLE `calendar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `credentials`
--
ALTER TABLE `credentials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `emploee_list`
--
ALTER TABLE `emploee_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `graphic`
--
ALTER TABLE `graphic`
  ADD PRIMARY KEY (`id`),
  ADD KEY `calendar_fk` (`calendar_fk`,`emploee_list_fk`),
  ADD KEY `emploee_list_fk` (`emploee_list_fk`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `item_std`
--
ALTER TABLE `item_std`
  ADD PRIMARY KEY (`id`),
  ADD KEY `std_op_fk` (`std_op_fk`,`item_fk`),
  ADD KEY `item_fk` (`item_fk`);

--
-- Indexes for table `std_op`
--
ALTER TABLE `std_op`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wo`
--
ALTER TABLE `wo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `item_fk` (`item_fk`);

--
-- Indexes for table `wo_item`
--
ALTER TABLE `wo_item`
  ADD PRIMARY KEY (`ide`),
  ADD KEY `wo_fk` (`wo_fk`,`item_fk`),
  ADD KEY `item_fk` (`item_fk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `calendar`
--
ALTER TABLE `calendar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `credentials`
--
ALTER TABLE `credentials`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `emploee_list`
--
ALTER TABLE `emploee_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `graphic`
--
ALTER TABLE `graphic`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=307;

--
-- AUTO_INCREMENT for table `wo`
--
ALTER TABLE `wo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `graphic`
--
ALTER TABLE `graphic`
  ADD CONSTRAINT `graphic_ibfk_1` FOREIGN KEY (`calendar_fk`) REFERENCES `calendar` (`id`),
  ADD CONSTRAINT `graphic_ibfk_2` FOREIGN KEY (`emploee_list_fk`) REFERENCES `emploee_list` (`id`);

--
-- Constraints for table `item_std`
--
ALTER TABLE `item_std`
  ADD CONSTRAINT `item_std_ibfk_1` FOREIGN KEY (`item_fk`) REFERENCES `items` (`id`),
  ADD CONSTRAINT `item_std_ibfk_2` FOREIGN KEY (`std_op_fk`) REFERENCES `std_op` (`id`);

--
-- Constraints for table `wo_item`
--
ALTER TABLE `wo_item`
  ADD CONSTRAINT `wo_item_ibfk_1` FOREIGN KEY (`wo_fk`) REFERENCES `wo` (`id`),
  ADD CONSTRAINT `wo_item_ibfk_2` FOREIGN KEY (`item_fk`) REFERENCES `items` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

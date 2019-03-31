-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.3.12-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- movie 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `movie`;
CREATE DATABASE IF NOT EXISTS `movie` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `movie`;

-- 테이블 movie.board 구조 내보내기
DROP TABLE IF EXISTS `board`;
CREATE TABLE IF NOT EXISTS `board` (
  `b_no` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `b_title` varchar(100) NOT NULL,
  `b_content` longtext DEFAULT NULL,
  `m_no` int(11) NOT NULL,
  `writer` varchar(100) NOT NULL,
  `b_date` timestamp NULL DEFAULT NULL,
  `good` int(11) DEFAULT NULL,
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 테이블 데이터 movie.board:~8 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
INSERT INTO `board` (`b_no`, `b_title`, `b_content`, `m_no`, `writer`, `b_date`, `good`) VALUES
	(1, 'ㅂㄼㄹ', 'ㅂㅈㄼㅈㄼㅈ', 4, 'ㅂㅈㄼㅈㄹ', NULL, 4),
	(2, 'ㅁㅎㅁㅎ', 'ㅎㄷㅈㅎㅈㄷㅎㅁㅈㅎ', 4, 'ㅎㅈㅁㅇㅎㅁㅂㅎ', NULL, 3),
	(3, 'ㅂㅈㄼㅈㄹ', 'ㅂㅈㄹㅈㅂㄼㅈ', 4, 'ㅂㅈㄹㅈㅂㄹ', '2019-03-03 13:35:00', 1),
	(4, 'ㅈㅎㅈㄷㅎ', 'ㅠ헝허ㅏㅏㄴ회회횧니ㅗ밓ㄴㅁㅎㅈㄷㅎㄷㅈㅎㄷㅈㅎㅈ', 4, 'ㄷㅈㅎ', '2019-03-03 14:15:56', 5),
	(5, 'ㅂㅎ', 'ㅗ고고더ㅜㄳ헣agfwefnrtnqrtw', 2, 'ㅗㅈ고좆보', '2019-03-03 14:16:31', 1),
	(6, 'etheh', 'vfmnbdfg,ngahbga.gawhhh', 2, 'eheh', '2019-03-03 14:16:39', 5),
	(7, 'yjkr', 'rkrkrkrjrhdhrjjrjr', 2, 'kkeky', '2019-03-03 14:16:47', 4),
	(8, 'af', 'asfsaf', 3, 'asfa', '2019-03-31 14:41:35', 5);
/*!40000 ALTER TABLE `board` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

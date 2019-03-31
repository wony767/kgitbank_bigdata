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

-- 테이블 movie.movie 구조 내보내기
DROP TABLE IF EXISTS `movie`;
CREATE TABLE IF NOT EXISTS `movie` (
  `m_no` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '기본키',
  `m_title` varchar(100) NOT NULL COMMENT '제목',
  `m_dir` varchar(50) DEFAULT NULL COMMENT '감독',
  `m_act` varchar(50) DEFAULT NULL COMMENT '배우',
  `m_content` longtext DEFAULT NULL COMMENT '내용',
  `m_grade` varchar(50) DEFAULT 'all',
  `m_img` varchar(50) DEFAULT NULL,
  `m_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`m_no`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 테이블 데이터 movie.movie:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` (`m_no`, `m_title`, `m_dir`, `m_act`, `m_content`, `m_grade`, `m_img`, `m_date`) VALUES
	(2, '사바하', 'jang', '이정재,유지태, 박정민', '줄거리\r\n사람들은 말했다\r\n그때, 그냥, 그것이 죽었어야 한다고…\r\n한 시골 마을에서 쌍둥이 자매가 태어난다. \r\n 온전치 못한 다리로 태어난 ‘금화’(이재인)와 모두가 오래 살지 못할 것이라고 했던 언니 ‘그것’. \r\n 하지만 그들은 올해로 16살이 되었다. \r\n \r\n 신흥 종교 비리를 찾아내는 종교문제연구소 ‘박목사’(이정재)는 \r\n 사슴동산이라는 새로운 종교 단체를 조사 중이다. \r\n 영월 터널에서 여중생이 사체로 발견되는 사건이 발생하고 \r\n 이를 쫓던 경찰과 우연히 사슴동산에서 마주친 박목사는 이번 건이 심상치 않음을 직감한다. \r\n \r\n 하지만 진실이 밝혀지기 전 터널 사건의 용의자는 자살하고, \r\n 그가 죽기 전 마지막으로 만난 실체를 알 수 없는 정비공 ‘나한’(박정민)과 \r\n 16년 전 태어난 쌍둥이 동생 금화의 존재까지 \r\n 사슴동산에 대해 파고들수록 박목사는 점점 더 많은 미스터리와 마주하게 되는데…!\r\n \r\n 그것이 태어나고 모든 사건이 시작되었다', '15세', 'sababa.jpg', '2019-02-20'),
	(3, '극한직업', '이병헌', '류승룡,이하늬,진선규', '낮에는 치킨장사! 밤에는 잠복근무!\r\n지금까지 이런 수사는 없었다!\r\n불철주야 달리고 구르지만 실적은 바닥, 급기야 해체 위기를 맞는 마약반!\r\n 더 이상 물러설 곳이 없는 팀의 맏형 고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고\r\n 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다.\r\n 마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되고,\r\n 뜻밖의 절대미각을 지닌 마형사의 숨은 재능으로 치킨집은 일약 맛집으로 입소문이 나기 시작한다.\r\n 수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아오는데…\r\n \r\n 범인을 잡을 것인가, 닭을 잡을 것인가!', '15세', 'kukhan.jpg', '2019-01-23'),
	(4, '신데렐라:마법 반지의 비밀', '린 사우더랜드', '사문영,김혜성,남도형', '“주문을 풀 수 있는 반지가 마법의 숲에 있어!”\r\n새어머니와 두 언니들의 구박에도 늘 씩씩하고 당찬 신데렐라는 왕궁 무도회에 가보고 싶다는 생쥐 친구들의 소원을 들어주기 위해 무도회 참석을 결정하지만 누더기 옷 때문에 고민에 빠지고 꼬꼬마 마법사 크리스탈을 찾아가 도움을 청한다. \r\n 이에 마법사 크리스탈은 신데렐라를 아름답게 치장하고, 생쥐 친구들을 화려한 황금 마차를 모는 멋진 말들로 변신시키는데… \r\n 화려한 폭죽과 함께 시작된 왕궁 무도회. \r\n 모두의 시선을 한눈에 사로잡을 만큼 우아하고 아름다운 여인으로 변신한 신데렐라는 왕자와 춤을 추며 무도회를 빛낸다. \r\n 그러던 중 휴식을 위해 무도회장에서 잠시 벗어나 있던 신데렐라는 우연히 진짜 왕자는 마녀의 주문에 걸려 있고, 이 왕자를 구하기 위해서는 요정의 책에 전해 내려오는 전설 속 마법 반지가 필요하다는 사실을 알게 된다. \r\n 진짜 왕자를 구하기 위해 무시무시한 괴물과 위험이 가득한 마법의 숲으로 환상적인 모험을 시작하는 신데렐라와 친구들. \r\n  \r\n 신데렐라와 친구들은 과연 위험천만한 그곳에서 사악한 마녀의 방해를 물리치고, 전설 속 마법 반지를 찾아 진짜 왕자를 구할 수 있을까?', '전체관람가', 'sinde.jpg', '2019-02-20'),
	(5, '자전차왕 엄복동', '김유성', '비,강소라,이법수', '일제강점기, 일본에서는 조선의 민족의식을 꺾고 \r\n 그들의 지배력을 과시하기 위해 전조선자전차대회를 개최한다. \r\n  \r\n 하지만 일본 최고의 선수들을 제치고 \r\n 조선인 최초로 우승을 차지한 엄복동의 등장으로 \r\n 일본의 계략은 실패로 돌아가고, \r\n 계속되는 무패행진으로 ‘민족 영웅’으로 떠오른 \r\n 그의 존재에 조선 전역은 들끓기 시작한다. \r\n  \r\n 때맞춰 애국단의 활약까지 거세지자 위기감을 느낀 일본은 \r\n 엄복동의 우승을 막고 조선인들의 사기를 꺾기 위해 \r\n 최후의 자전차 대회를 개최하는데... \r\n  \r\n 일제강점기, 그 어느 때보다 뜨거웠던 한일전이 시작된다!', '12세', 'ajajaj.jpg', '2019-02-27');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

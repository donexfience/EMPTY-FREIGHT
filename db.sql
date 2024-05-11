/*
SQLyog Community v13.1.2 (64 bit)
MySQL - 5.5.20-log : Database - empty_freight
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`empty_freight` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `empty_freight`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rid` int(11) DEFAULT NULL,
  `Did` bigint(20) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`id`,`rid`,`Did`,`date`,`status`) values 
(1,2,4,'2023-03-20','pending'),
(2,3,4,'2023-03-21','pending'),
(3,5,13,'2023-03-21','pending'),
(4,6,13,'2023-03-22','pending'),
(5,4,7,'2023-03-28','pending'),
(6,9,7,'2023-03-28','accepted'),
(7,10,13,'2023-03-29','pending'),
(8,11,4,'2023-04-05','pending');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rt_id` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`id`,`rt_id`,`uid`,`date`,`status`) values 
(1,11,10,'2023-04-03','pending'),
(2,8,10,'2023-04-03','accepted');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fromid` int(11) DEFAULT NULL,
  `toid` int(11) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`id`,`fromid`,`toid`,`message`,`date`) values 
(1,5,8,'hii','2023-03-20'),
(2,5,8,'','2023-03-20'),
(3,5,9,'hii..iam user','2023-03-20'),
(4,10,8,'hi','2023-03-21'),
(5,13,6,'hi','2023-03-22'),
(6,10,18,'hlo','2023-03-22'),
(7,20,5,'hi ','2023-03-22'),
(8,10,19,'hy','2023-03-22'),
(9,5,18,'hkoo','2023-03-28'),
(10,5,18,'good','2023-03-28'),
(11,5,4,'hlo','2023-03-28'),
(12,10,17,'hi','2023-03-29'),
(13,10,18,'fttguu','2023-03-29'),
(14,10,18,'fttguu','2023-03-29'),
(15,10,18,'fttguu','2023-03-29'),
(16,10,18,'fttguu','2023-03-29'),
(17,10,18,'fttguu','2023-03-29'),
(18,10,18,'','2023-03-29'),
(19,10,18,'hai','2023-03-29'),
(20,10,21,'hlo','2023-03-29'),
(21,13,6,'hi','2023-04-07'),
(22,8,11,'hi','2023-04-07'),
(23,8,6,'hi','2023-04-07'),
(24,10,17,'hi','2023-04-07'),
(25,10,4,'h','2023-04-07');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `toid` int(11) DEFAULT NULL,
  `complaint` varchar(400) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `reply` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`id`,`uid`,`toid`,`complaint`,`date`,`reply`) values 
(1,5,2,'very bad','2023-03-20','ok...'),
(2,5,3,'ddd','2023-03-20','ok, we will consider it.'),
(3,6,3,'lag','2023-03-21','oky '),
(4,5,3,'very bad','2023-03-28','ok....'),
(5,10,3,'bad','2023-03-29','GOOD'),
(6,10,3,'laging','2023-03-29','pending'),
(7,10,2,'tooo bad','2023-03-29','pending'),
(8,10,13,'lagging problem','2023-03-29','sry'),
(9,10,7,'hhh','2023-04-06','pending'),
(10,10,16,'jj','2023-04-07','pending');

/*Table structure for table `driver` */

DROP TABLE IF EXISTS `driver`;

CREATE TABLE `driver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `vtype` varchar(100) DEFAULT NULL,
  `vnumber` varchar(100) DEFAULT NULL,
  `i number` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `driver` */

insert  into `driver`(`id`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`,`vtype`,`vnumber`,`i number`) values 
(1,4,'Donex','fience','kondacherri','thiruvambadi',678904,9835086536,'donex6fience@gmail.com','truck','KL-11-2876',NULL),
(2,7,'linto','emmanuel','adivaram','puduppadi',678956,8778494090,'lintoemmanuellinto@gmail.com','lorry','KL-12-2628',NULL),
(3,13,'ravi','pv','kollam','puduppadi',678909,98778494090,'ravi@gmail.com','truck','KL-11-2876',NULL),
(4,21,'feyz','feyz','kollam','kollam',675676,8898765678,'feyz34gmail.com','lorry','KL-11-2809',NULL),
(5,25,'MC','manu','KOZHIKODE','PAROPADY',673573,9987899865,'manu23@gmail.com','lorry','KL-11- 3084',NULL),
(6,26,'aleena','mariya','kollam','kollam',677687,8987678965,'aleena23@gmail.com','truck','KL-11-4355',NULL),
(7,30,'cvbcvb','cbcb','bcb','bcbc',0,8787878787,'cbc@gmail.com','bcb','bcvbcv','ghhghh');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `toid` int(11) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`uid`,`toid`,`feedback`,`date`) values 
(1,6,3,'nice','2023-03-21'),
(2,10,8,'Palco industries - very bad experience ','2023-03-29'),
(3,10,4,'hhhh','2023-04-07'),
(4,10,13,'hhh','2023-04-07'),
(5,10,1,'hhh','2023-04-07');

/*Table structure for table `local_owners` */

DROP TABLE IF EXISTS `local_owners`;

CREATE TABLE `local_owners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `idproof` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `local_owners` */

insert  into `local_owners`(`id`,`lid`,`name`,`place`,`post`,`pin`,`email`,`phone`,`idproof`) values 
(1,8,'ravi','kollam','kollam',673567,'ravi@gmail.com',7890876567,NULL),
(2,17,'jadeera ','mylellampara ','mmylellampara ',678767,'jadeera@gmail.com',7898765678,NULL),
(3,18,'shiju','Puduppady ','Puduppady ',673586,'shiju12@gmail.com',9947035193,NULL),
(4,19,'Amal','kochi','kochi',678768,'amal25@gmail.com',7898767898,NULL),
(5,20,'kavitha','kottayam','kottayam',678765,'kavi@gmail.com',7887678798,NULL),
(6,24,'ahalya ','kunnamagalam ','kunnamagalam ',678767,'ahalya2@gmail.com',7898765678,NULL),
(7,31,'sbbs','mvnv','hchv',787677,'shs@gmail.com',953675556,'storage_emulated_0_DCIM_Camera_IMG_20230407_094317.jpg'),
(8,32,'sbbs','mvnv','hchv',787677,'shs@gmail.com',953675556,'storage_emulated_0_DCIM_Camera_IMG_20230407_094317.jpg');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `did` int(11) DEFAULT NULL,
  `latitude` varchar(200) DEFAULT NULL,
  `longitude` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`did`,`latitude`,`longitude`) values 
(1,10,'11.4939068','76.0161613'),
(2,13,'11.5194915','76.0219644'),
(3,21,'11.48640382','75.99266924'),
(4,4,'11.48624114','75.99283897'),
(5,26,'11.48633303','75.99275671'),
(6,8,'11.2577844','75.7845308');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(90) DEFAULT NULL,
  `pwd` varchar(90) DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`uname`,`pwd`,`type`) values 
(1,'admin','admin','admin'),
(2,'Muhammad K','muhammad','Trading_Company'),
(3,'Ammu','ammu','Trading_Company'),
(4,'Donex Fience','donu','driver'),
(5,'shilu','shi','pending'),
(6,'anjana','anju','user'),
(7,'Linto Emmanuel','linto','driver'),
(8,'athira','athi','local_owners'),
(9,'jadeera','jade','local_owners'),
(10,'anju','anju','user'),
(11,'anju','anju','user'),
(12,'anju','anju','user'),
(13,'123','123','driver'),
(14,'maya','maya','local_owners'),
(15,'abish','abish','local_owners'),
(16,'ravi','ravi','local_owners'),
(17,'jadeera','jadeera','local_owners'),
(18,'shiju','shiju','driver'),
(19,'amal','amal ','local_owners'),
(20,'kavi','kavi','local_owners'),
(21,'feyz','feyz','driver'),
(22,'manu','manu','Trading_Company'),
(23,'vafa','vafa','pending'),
(24,'ahalya','ahalya ','pending'),
(25,'MANU','MANU','driver'),
(26,'aleena','aleena','driver'),
(27,'Vismaya','vis','us'),
(28,'vismaya','vismaya','pending'),
(29,'hff','hff','pending'),
(30,'assign.PNG','vbcvb','driver'),
(31,'aaa','aaa','pending'),
(32,'aaa','aaa','pending');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `toid` int(11) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `review` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`id`,`uid`,`toid`,`rating`,`review`,`date`) values 
(1,6,3,'3.0','good','2023-03-21'),
(2,5,13,'3.5','dcsc','2023-03-21'),
(3,10,25,'5.0','hhh','2023-04-06');

/*Table structure for table `request_for_load` */

DROP TABLE IF EXISTS `request_for_load`;

CREATE TABLE `request_for_load` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `tid` int(11) DEFAULT NULL,
  `load` varchar(500) DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `request_for_load` */

insert  into `request_for_load`(`id`,`uid`,`tid`,`load`,`details`,`date`,`status`) values 
(1,5,2,'banana','today','2023-03-20','rejected'),
(2,5,2,'cotton','2kg material','2023-03-20','assigned'),
(3,10,3,'cotton','tight ','2023-03-21','assigned'),
(4,10,2,'carrot','immediate ','2023-03-21','assigned'),
(5,10,3,'banana','immediately ','2023-03-21','assigned'),
(6,10,3,'banana','immediately ','2023-03-21','assigned'),
(7,10,2,'apple','today','2023-03-28','pending'),
(8,10,2,'apple','tonight ','2023-03-28','pending'),
(9,5,3,'apple','urgent ','2023-03-28','assigned'),
(10,10,3,'apple','urgent','2023-03-29','assigned'),
(11,10,3,'wool','immediately ','2023-03-29','assigned'),
(12,10,3,'bricks ','40kg of bricks','2023-03-29','pending'),
(13,10,27,'hh','hh','2023-04-06','pending');

/*Table structure for table `request_for_trip` */

DROP TABLE IF EXISTS `request_for_trip`;

CREATE TABLE `request_for_trip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `from` varchar(200) DEFAULT NULL,
  `to` varchar(100) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `request_for_trip` */

insert  into `request_for_trip`(`id`,`uid`,`lid`,`from`,`to`,`date`,`status`) values 
(1,5,4,'kozhikode','kannur','2023-03-20','pending'),
(2,5,4,'kochi','aluva','2023-03-20','pending'),
(3,5,13,'kollam','Kozhikode ','2023-03-21','accepted'),
(4,10,13,'kozhikkode ','kochi','2023-03-22','pending'),
(5,10,7,'kochii','kKozhikode ','2023-03-22','pending'),
(6,10,20,'kottayam ','kochii ','2023-03-22','pending'),
(7,10,19,'trivandram','kozhikkode ','2023-03-22','return'),
(8,10,13,'kozhikkode ','kalpetta','2023-03-28','return'),
(9,13,13,'kozhikkode ','kalpetta','2023-03-28','pending'),
(10,5,17,'kottayam','palakkad','2023-03-28','pending'),
(11,5,19,'kollam','kottayam ','2023-03-28','return'),
(12,5,17,'kochi ','kottayam','2023-03-29','pending'),
(13,10,19,'kollam','kottayam','2023-03-29','return'),
(14,10,20,'alapuzha','kollam','2023-03-29','pending'),
(15,10,4,'kollam','Kozhikode ','2023-03-29','return'),
(16,10,13,'Tamil Nadu ','Kozhikode ','2023-03-29','pending');

/*Table structure for table `trading_company` */

DROP TABLE IF EXISTS `trading_company`;

CREATE TABLE `trading_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `proof` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `trading_company` */

insert  into `trading_company`(`id`,`lid`,`name`,`place`,`post`,`pin`,`phone`,`email`,`proof`) values 
(1,2,'palco industries','malapuram','puduppadi',678077,8778494090,'palcoindustries@gmail.com',NULL),
(2,3,'Ammu','kochi','aluva',678859,7890907674,'ammu123@gmail.com',NULL),
(3,22,'manu','kollam','kollam',678767,9987899865,'manu23@gmail.com',NULL),
(4,23,'vafa','vavad','koduvally',678904,9754378954,'vafapv45@gmail.com',NULL),
(5,27,'Vismaya','kollam','kollam',678956,7894506694,'vismayapv@gmil.com',NULL),
(6,28,'vismaya','kochi','kochi',678956,7687656787,'vismayapv@gmail.com',NULL),
(7,29,'hngbnb','bnbvnb','nbnbnb',878787,8787878787,'bncvncn@gmail.com','assign.PNG');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,5,'Shilu ',' Jazz','puduppadi ','puduppadi ',678976,7898765456,'shilujastsy@gmail.com'),
(2,6,'Anjana ','shiju','mylellampara','mylellampara',673586,7898765456,'anjanashij28@gmail.com'),
(3,10,'anju','shiju','mukam','mukam',6789876,7898767898,'anju@gmail.com'),
(4,11,'anju','shiju','mukam','mukam',6789876,7898767898,'anju@gmail.com'),
(5,12,'anju','shiju','mukam','mukam',6789876,7898767898,'anju@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- MySQL dump 10.13  Distrib 8.4.8, for Win64 (x86_64)
--
-- Host: localhost    Database: smartcity
-- ------------------------------------------------------
-- Server version	8.4.8

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Admin'),(3,'Authority'),(2,'User');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',3,'add_permission'),(6,'Can change permission',3,'change_permission'),(7,'Can delete permission',3,'delete_permission'),(8,'Can view permission',3,'view_permission'),(9,'Can add group',2,'add_group'),(10,'Can change group',2,'change_group'),(11,'Can delete group',2,'delete_group'),(12,'Can view group',2,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add request_table',10,'add_request_table'),(26,'Can change request_table',10,'change_request_table'),(27,'Can delete request_table',10,'delete_request_table'),(28,'Can view request_table',10,'view_request_table'),(29,'Can add authority',8,'add_authority'),(30,'Can change authority',8,'change_authority'),(31,'Can delete authority',8,'delete_authority'),(32,'Can view authority',8,'view_authority'),(33,'Can add assign_authority',7,'add_assign_authority'),(34,'Can change assign_authority',7,'change_assign_authority'),(35,'Can delete assign_authority',7,'delete_assign_authority'),(36,'Can view assign_authority',7,'view_assign_authority'),(37,'Can add user_table',11,'add_user_table'),(38,'Can change user_table',11,'change_user_table'),(39,'Can delete user_table',11,'delete_user_table'),(40,'Can view user_table',11,'view_user_table'),(41,'Can add feedback',9,'add_feedback'),(42,'Can change feedback',9,'change_feedback'),(43,'Can delete feedback',9,'delete_feedback'),(44,'Can view feedback',9,'view_feedback');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1200000$sNMrmZu4OjJCKTRd78s2hu$hN72989VbECSf/9qhOF9L1HtQnqh23/lCgoPPaA39LQ=','2026-04-17 05:48:26.998286',1,'admin','','','admin@gmail.com',1,1,'2026-03-31 09:18:42.970794'),(2,'pbkdf2_sha256$1200000$LK6K1CBcQk1dBmCX7Od41s$Km1ZVuZ86tWDs/o9mcg4DiDtSLV9hzzCAZuV0CmqOXE=',NULL,0,'mammu112','','','',0,1,'2026-03-31 10:16:51.617922'),(5,'pbkdf2_sha256$1200000$AUmoqDR9ApRBw5qpcUXK5W$jZSjvVTPfLsAL8gMQlzBZrmyX6D+4T75t8deSugIlRA=',NULL,0,'ju','','','',0,1,'2026-03-31 10:43:52.037500'),(6,'pbkdf2_sha256$1200000$rYJhhrSzgIxQ4mksa5yOEw$V5woaGoHHcLyUsD7YDFsD3C2BDvko4qH4ckFKRBvQLs=',NULL,0,'mimmi','','','',0,1,'2026-03-31 11:57:31.640608'),(7,'pbkdf2_sha256$1200000$jUZfFQe4wVfAkoslTgFguP$W1MuWYg0B2tjg0KeVu2DCVtFMRiJ0OqPMdorscfjLLk=',NULL,0,'mimmi1','','','',0,1,'2026-03-31 11:59:08.486859'),(9,'pbkdf2_sha256$1200000$qNfnWrgXeaBlM9omBhpe3B$ut0JLCYYAQFHlekcu66bm7yuXs24Zz9QHVUo/Zso7aI=',NULL,0,'mimmi3','','','',0,1,'2026-03-31 12:01:46.367533'),(10,'pbkdf2_sha256$1200000$Ygu0BoQXcEQu085fEgxdiD$GvWDeVNiNdb500+yrweDWdSxfSVKESQIaDujAShaV4o=',NULL,0,'mimmi4','','','',0,1,'2026-03-31 12:02:05.641333'),(11,'pbkdf2_sha256$1200000$55lW4Fac422HJXYmt4O54X$iJao5/TizI/DFvxAIGFa0p6Y1LldbhRRwKUyABPFjU0=',NULL,0,'mimmi5','','','',0,1,'2026-03-31 12:04:54.834995'),(13,'pbkdf2_sha256$1200000$4LJpTSIPTqwlQOcOjs0jHY$FjL9HCgKyGOHljFTxHItfDSWcBajAfVxbfKDYnT7U0A=',NULL,0,'mimmi8','','','',0,1,'2026-03-31 12:06:54.656650'),(15,'pbkdf2_sha256$1200000$YVwifCeFdCHeP0BxiWQ5ms$C+1St0yIZxPsCsBPgR21G4WVG/qJtG19RgtA98ivfEs=','2026-04-01 10:56:39.661313',0,'razee','','','',0,1,'2026-04-01 10:56:18.097377'),(16,'pbkdf2_sha256$1200000$BwC3J2EKL8TUIAFIMDGcD9$iVbM359f6Mm1d0SLzxL3NBPJEZNdDHJ1FJu37ICLk84=',NULL,0,'aman','','','',0,1,'2026-04-01 11:34:25.725581'),(17,'pbkdf2_sha256$1200000$qIy2SdrLcKdzhsk5d8Y9ae$wgeVwl6kawv4XiX0STL5is6QUwdBVG/RMg1eJeJJsts=',NULL,0,'kiiki','','','',0,1,'2026-04-01 11:36:47.869436'),(20,'pbkdf2_sha256$1200000$bQYJc1WqRdyUPqzhZ6idfe$jvS/RZHVCFEsy/kptZTm9bvPLCUtbDT0f5ylizASAKg=','2026-04-17 06:36:41.291539',0,'kooko','','','',0,1,'2026-04-13 05:38:46.247520'),(21,'pbkdf2_sha256$1200000$CmCu5FwNzQknwDTJ4emn1e$sd3EA0deqJCRt10Pc10FYRPa9H9yDsG4lJaBHWhADnU=','2026-04-17 05:49:37.736744',0,'water','','','',0,1,'2026-04-17 05:42:11.127141'),(22,'pbkdf2_sha256$1200000$e3CXyL2LwTPOjF5laI2GJ4$QeWuL6DKQ42ik6uP8vQftTdZTZe86Q3kgoz2MYJJDh4=','2026-04-17 05:49:57.259688',0,'kseb','','','',0,1,'2026-04-17 05:42:53.994079');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,1,1),(3,5,3),(4,6,2),(5,7,2),(6,9,2),(7,10,2),(8,11,2),(9,13,2),(11,15,2),(12,16,2),(13,17,2),(14,20,2),(15,21,3),(16,22,3);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'myapp','assign_authority'),(8,'myapp','authority'),(9,'myapp','feedback'),(10,'myapp','request_table'),(11,'myapp','user_table'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-03-27 09:53:40.325553'),(2,'auth','0001_initial','2026-03-27 09:53:41.364059'),(3,'admin','0001_initial','2026-03-27 09:53:41.667009'),(4,'admin','0002_logentry_remove_auto_add','2026-03-27 09:53:41.690343'),(5,'admin','0003_logentry_add_action_flag_choices','2026-03-27 09:53:41.719393'),(6,'contenttypes','0002_remove_content_type_name','2026-03-27 09:53:42.029118'),(7,'auth','0002_alter_permission_name_max_length','2026-03-27 09:53:42.198558'),(8,'auth','0003_alter_user_email_max_length','2026-03-27 09:53:42.277687'),(9,'auth','0004_alter_user_username_opts','2026-03-27 09:53:42.300161'),(10,'auth','0005_alter_user_last_login_null','2026-03-27 09:53:42.526266'),(11,'auth','0006_require_contenttypes_0002','2026-03-27 09:53:42.529821'),(12,'auth','0007_alter_validators_add_error_messages','2026-03-27 09:53:42.549687'),(13,'auth','0008_alter_user_username_max_length','2026-03-27 09:53:42.673317'),(14,'auth','0009_alter_user_last_name_max_length','2026-03-27 09:53:42.879431'),(15,'auth','0010_alter_group_name_max_length','2026-03-27 09:53:42.949981'),(16,'auth','0011_update_proxy_permissions','2026-03-27 09:53:42.977230'),(17,'auth','0012_alter_user_first_name_max_length','2026-03-27 09:53:43.196520'),(18,'myapp','0001_initial','2026-03-27 09:53:44.458508'),(19,'sessions','0001_initial','2026-03-27 09:53:44.552929'),(20,'myapp','0002_request_table_status','2026-04-01 08:52:22.749488'),(21,'myapp','0003_user_table_status','2026-04-01 11:19:33.142252'),(22,'myapp','0004_user_table_type','2026-04-17 05:04:31.913856'),(23,'myapp','0005_alter_user_table_type','2026-04-17 05:04:31.936374');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8en8nu0i4ani3pmdoxzff5azbzrsyzwb','.eJxVjMsOgjAQAP9lz6ZZlmJbjt75hma3D4uaklA4Gf_dkHDQ68xk3uB534rfW1r9HGEEQrj8QuHwTPUw8cH1vqiw1G2dRR2JOm1T0xLT63a2f4PCrcAIiZn7wBJCj10Wm_toOusGQSd8NTTkSDY7cTo6RMJAlkRrl9GgJc3w-QIulzgl:1wDcoj:FXTcC-c5DAKSaCQMdE25aIdBd8633GXdunidXJt5Vfc','2026-05-01 06:36:41.307986'),('pmt8ebyhc15r7xopaiu8i7b670r1opa0','.eJxVjDsOAiEUAO9CbcjjK1jaewby4IGsGkiW3cp4d0OyhbYzk3mzgPtWwz7yGhZiFybY6ZdFTM_cpqAHtnvnqbdtXSKfCT_s4LdO-XU92r9BxVHnVhgdrY7SqgIeAb0zYNBRAuU0AEjU1tszJFGINBhSIB2mIjVkScg-X6_GNuc:1w7tqM:BXlj1N0MlN5CA0ssUUNX468Gm_AQDgMEPc1WkjlgRGQ','2026-04-15 11:34:42.234471'),('r6gv3s2q7op8vm9h3syxurii4kkkkkw5','.eJxVjDsOAiEUAO9CbcjjK1jaewby4IGsGkiW3cp4d0OyhbYzk3mzgPtWwz7yGhZiFybY6ZdFTM_cpqAHtnvnqbdtXSKfCT_s4LdO-XU92r9BxVHnVhgdrY7SqgIeAb0zYNBRAuU0AEjU1tszJFGINBhSIB2mIjVkScg-X6_GNuc:1wCAlc:_gsLKnai0DW-o2iLrd3oYnhB-AUgDRSR8Dq4Mt0d9xg','2026-04-27 06:27:28.467285'),('xysdlr1kr2p8eo0tg0109jweoc77knyt','.eJxVjMsOgjAQAP9lz6ZZlmJbjt75hma3D4uaklA4Gf_dkHDQ68xk3uB534rfW1r9HGEEQrj8QuHwTPUw8cH1vqiw1G2dRR2JOm1T0xLT63a2f4PCrcAIiZn7wBJCj10Wm_toOusGQSd8NTTkSDY7cTo6RMJAlkRrl9GgJc3w-QIulzgl:1wDc6C:i4ZYIoGWvCsEVowe7xm-qUQeK8b4OqPesYr-TRSqKjQ','2026-05-01 05:50:40.984629');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_assign_authority`
--

DROP TABLE IF EXISTS `myapp_assign_authority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_assign_authority` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `AUTHORITY_id` bigint NOT NULL,
  `REQUEST_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_assign_authori_AUTHORITY_id_d00ccbb6_fk_myapp_aut` (`AUTHORITY_id`),
  KEY `myapp_assign_authori_REQUEST_id_625bb9f0_fk_myapp_req` (`REQUEST_id`),
  CONSTRAINT `myapp_assign_authori_AUTHORITY_id_d00ccbb6_fk_myapp_aut` FOREIGN KEY (`AUTHORITY_id`) REFERENCES `myapp_authority` (`id`),
  CONSTRAINT `myapp_assign_authori_REQUEST_id_625bb9f0_fk_myapp_req` FOREIGN KEY (`REQUEST_id`) REFERENCES `myapp_request_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_assign_authority`
--

LOCK TABLES `myapp_assign_authority` WRITE;
/*!40000 ALTER TABLE `myapp_assign_authority` DISABLE KEYS */;
INSERT INTO `myapp_assign_authority` VALUES (5,'2026-04-17','completed',5,7);
/*!40000 ALTER TABLE `myapp_assign_authority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_authority`
--

DROP TABLE IF EXISTS `myapp_authority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_authority` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `type` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `LOGIN_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_authority_LOGIN_id_edd5b446_fk_auth_user_id` (`LOGIN_id`),
  CONSTRAINT `myapp_authority_LOGIN_id_edd5b446_fk_auth_user_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_authority`
--

LOCK TABLES `myapp_authority` WRITE;
/*!40000 ALTER TABLE `myapp_authority` DISABLE KEYS */;
INSERT INTO `myapp_authority` VALUES (4,'water','water',45646454646,'water@gmail.com',21),(5,'kseb','electricty',23456789,'kseb@gmail.com',22);
/*!40000 ALTER TABLE `myapp_authority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_feedback`
--

DROP TABLE IF EXISTS `myapp_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) NOT NULL,
  `ratings` double NOT NULL,
  `date` date NOT NULL,
  `ASSIGN_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_ASSIGN_id_5dedea49_fk_myapp_assign_authority_id` (`ASSIGN_id`),
  KEY `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_ASSIGN_id_5dedea49_fk_myapp_assign_authority_id` FOREIGN KEY (`ASSIGN_id`) REFERENCES `myapp_assign_authority` (`id`),
  CONSTRAINT `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_feedback`
--

LOCK TABLES `myapp_feedback` WRITE;
/*!40000 ALTER TABLE `myapp_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_request_table`
--

DROP TABLE IF EXISTS `myapp_request_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_request_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `descreption` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `title` varchar(50) NOT NULL,
  `USER_id` bigint NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_request_table_USER_id_8ef558ea_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_request_table_USER_id_8ef558ea_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_request_table`
--

LOCK TABLES `myapp_request_table` WRITE;
/*!40000 ALTER TABLE `myapp_request_table` DISABLE KEYS */;
INSERT INTO `myapp_request_table` VALUES (1,'data.jpg','hfhffyfy','2026-04-13','water',10,'completed'),(2,'data_TlgkCbI.jpg','khkhh','2026-04-13','water',10,'send'),(3,'data_d5DLB9A.jpg','wdwdwdwd','2026-04-13','dwwdwd',10,'send'),(4,'sslc_certificate_CDrcsFI.jpeg','sdsdsdsd','2026-04-13','ssasasasass',10,'send'),(5,'sslc_certificate_P2JzCgj.jpeg','hhhjh','2026-04-13','water',10,'send'),(6,'ibm.png','no water in pipe','2026-04-17','water',10,'completed'),(7,'ibm_H96SV9k.png','current is not availble in kasargod','2026-04-17','electricity',10,'completed'),(8,'WhatsApp_Image_2026-04-16_at_10.15.41_PM.jpeg','kajsdska','2026-04-17','this is a isuue',10,'pending');
/*!40000 ALTER TABLE `myapp_request_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user_table`
--

DROP TABLE IF EXISTS `myapp_user_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `ward` int NOT NULL,
  `place` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `post` varchar(50) NOT NULL,
  `LOGIN_id` int NOT NULL,
  `status` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_table_LOGIN_id_76a60eb1_fk_auth_user_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_table_LOGIN_id_76a60eb1_fk_auth_user_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user_table`
--

LOCK TABLES `myapp_user_table` WRITE;
/*!40000 ALTER TABLE `myapp_user_table` DISABLE KEYS */;
INSERT INTO `myapp_user_table` VALUES (10,'kooko',4353421,'kooki@gmail.com','Exam_Admit_card_2.pdf',76543,'sdfghjk',876543,'76w',20,'accepted','1');
/*!40000 ALTER TABLE `myapp_user_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-17 12:07:05

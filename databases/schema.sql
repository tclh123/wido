drop schema if exists `widodb`;
CREATE SCHEMA `widodb`;
use `widodb`;

drop table if exists `tag`;
drop table if exists `user_tag`;

CREATE TABLE `tag` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `parent_id` int(11) unsigned NOT NULL,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_name_parent_id` (`name`, `parent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_tag` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `user_id` int(11) unsigned NOT NULL,
    `user_name` varchar(100) NOT NULL,
    `tag_id` int(11) unsigned NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_user_tag` (`user_id`, `tag_id`),
    UNIQUE KEY `uk_user_tag_2` (`user_name`, `tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

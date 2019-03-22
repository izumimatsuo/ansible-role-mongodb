# ansible-role-mongodb [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-mongodb.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-mongodb)

CentOS 7 に mongodb を構築する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

項目名            |デフォルト値|説明
------------------|------------|------------------
mongod_listen_port|27017       |ポート番号
mongod_bind_ip    |127.0.0.1   |アクセス許可リスト
